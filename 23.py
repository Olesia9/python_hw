import pygame
import random
import time
import os
import json
from enum import Enum

# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)


# Состояния клеток
class CellState(Enum):
    EMPTY = 0
    TREE = 1
    WATER = 2
    BURNING_TREE = 3
    BURNT_TREE = 4
    HOSPITAL = 5
    SHOP = 6


# Класс игрового поля
class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[CellState.EMPTY for _ in range(width)] for _ in range(height)]
        self.generate_rivers()
        self.generate_trees()
        self.generate_special_buildings()

    def generate_rivers(self):
        """Генерация рек на карте"""
        for _ in range(self.width // 5):
            x = random.randint(0, self.width - 1)
            for y in range(self.height):
                if 0 <= x < self.width:
                    self.grid[y][x] = CellState.WATER
                # Добавляем изгибы реки
                if random.random() < 0.3:
                    x += random.choice([-1, 1])

    def generate_trees(self):
        """Генерация деревьев на карте"""
        for _ in range(self.width * self.height // 3):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.grid[y][x] == CellState.EMPTY:
                self.grid[y][x] = CellState.TREE

    def generate_special_buildings(self):
        """Генерация госпиталя и магазина"""
        # Госпиталь
        x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        while self.grid[y][x] != CellState.EMPTY:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        self.grid[y][x] = CellState.HOSPITAL

        # Магазин
        x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        while self.grid[y][x] != CellState.EMPTY:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        self.grid[y][x] = CellState.SHOP

    def is_valid_position(self, x, y):
        """Проверка, что координаты в пределах карты"""
        return 0 <= x < self.width and 0 <= y < self.height

    def start_fire(self):
        """Начало пожара в случайном месте"""
        trees = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == CellState.TREE:
                    trees.append((x, y))

        if trees:
            x, y = random.choice(trees)
            self.grid[y][x] = CellState.BURNING_TREE
            return True
        return False

    def spread_fire(self):
        """Распространение пожара на соседние деревья"""
        new_fires = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == CellState.BURNING_TREE:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if self.is_valid_position(nx, ny) and self.grid[ny][nx] == CellState.TREE:
                            if random.random() < 0.3:  # 30% шанс распространения
                                new_fires.append((nx, ny))

        for x, y in new_fires:
            self.grid[y][x] = CellState.BURNING_TREE

        # Проверяем, сгорели ли деревья
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == CellState.BURNING_TREE:
                    if random.random() < 0.1:  # 10% шанс, что дерево сгорит
                        self.grid[y][x] = CellState.BURNT_TREE

    def extinguish_fire(self, x, y):
        """Тушение пожара в указанной клетке"""
        if self.is_valid_position(x, y) and self.grid[y][x] == CellState.BURNING_TREE:
            self.grid[y][x] = CellState.TREE
            return True
        return False


# Класс вертолета
class Helicopter:
    def __init__(self, x, y, game_map):
        self.x = x
        self.y = y
        self.game_map = game_map
        self.water_tanks = 1
        self.water_amount = 0
        self.max_water = 1
        self.score = 0
        self.lives = 3
        self.last_fire_time = time.time()
        self.fire_interval = 10  # секунд между пожарами

    def move(self, dx, dy):
        """Перемещение вертолета"""
        new_x, new_y = self.x + dx, self.y + dy
        if self.game_map.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.check_cell()

    def check_cell(self):
        """Проверка клетки под вертолетом"""
        cell = self.game_map.grid[self.y][self.x]

        # Набираем воду
        if cell == CellState.WATER:
            self.water_amount = self.max_water

        # Лечение в госпитале
        elif cell == CellState.HOSPITAL and self.lives < 3:
            if self.score >= 50:
                self.score -= 50
                self.lives += 1

        # Магазин улучшений
        elif cell == CellState.SHOP:
            if self.score >= 100 and self.max_water < 3:
                self.score -= 100
                self.max_water += 1

    def extinguish(self):
        """Попытка потушить пожар"""
        if self.water_amount > 0:
            if self.game_map.extinguish_fire(self.x, self.y):
                self.water_amount -= 1
                self.score += 10
                return True
        return False

    def update(self):
        """Обновление состояния вертолета"""
        current_time = time.time()
        if current_time - self.last_fire_time > self.fire_interval:
            if self.game_map.start_fire():
                self.last_fire_time = current_time
            self.fire_interval = max(5, self.fire_interval * 0.95)  # Уменьшаем интервал между пожарами


# Класс игры
class FireHelicopterGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Пожарный вертолет")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.game_map = GameMap(width, height)
        self.helicopter = Helicopter(width // 2, height // 2, self.game_map)
        self.running = True
        self.game_over = False
        self.weather = "sunny"
        self.last_weather_change = time.time()

    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if not self.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.helicopter.move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.helicopter.move(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.helicopter.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.helicopter.move(1, 0)
                    elif event.key == pygame.K_SPACE:
                        self.helicopter.extinguish()
                    elif event.key == pygame.K_s:
                        self.save_game()
                    elif event.key == pygame.K_l:
                        self.load_game()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__init__(self.width, self.height)

    def update_weather(self):
        """Обновление погодных условий"""
        current_time = time.time()
        if current_time - self.last_weather_change > 30:  # Меняем погоду каждые 30 секунд
            self.weather = random.choice(["sunny", "rainy", "cloudy", "stormy"])
            self.last_weather_change = current_time

            # Шторм увеличивает вероятность пожара
            if self.weather == "stormy":
                self.helicopter.fire_interval *= 0.7

    def update(self):
        """Обновление состояния игры"""
        if not self.game_over:
            self.helicopter.update()
            self.game_map.spread_fire()
            self.update_weather()

            # Проверка на проигрыш
            if self.helicopter.lives <= 0:
                self.game_over = True

    def draw(self):
        """Отрисовка игры"""
        self.screen.fill(WHITE)

        # Отрисовка карты
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                cell = self.game_map.grid[y][x]

                if cell == CellState.EMPTY:
                    pygame.draw.rect(self.screen, WHITE, rect)
                elif cell == CellState.TREE:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif cell == CellState.WATER:
                    pygame.draw.rect(self.screen, BLUE, rect)
                elif cell == CellState.BURNING_TREE:
                    pygame.draw.rect(self.screen, RED, rect)
                elif cell == CellState.BURNT_TREE:
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif cell == CellState.HOSPITAL:
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)  # Ярко-зеленый для госпиталя
                elif cell == CellState.SHOP:
                    pygame.draw.rect(self.screen, YELLOW, rect)

                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Границы клеток

        # Отрисовка вертолета
        heli_rect = pygame.Rect(
            self.helicopter.x * CELL_SIZE + CELL_SIZE // 4,
            self.helicopter.y * CELL_SIZE + CELL_SIZE // 4,
            CELL_SIZE // 2,
            CELL_SIZE // 2
        )
        pygame.draw.ellipse(self.screen, GRAY, heli_rect)

        # Отрисовка информации
        info_y = self.height * CELL_SIZE + 10
        score_text = self.font.render(f"Очки: {self.helicopter.score}", True, BLACK)
        self.screen.blit(score_text, (10, info_y))

        lives_text = self.font.render(f"Жизни: {self.helicopter.lives}", True, BLACK)
        self.screen.blit(lives_text, (200, info_y))

        water_text = self.font.render(f"Вода: {self.helicopter.water_amount}/{self.helicopter.max_water}", True, BLACK)
        self.screen.blit(water_text, (400, info_y))

        weather_text = self.font.render(f"Погода: {self.weather}", True, BLACK)
        self.screen.blit(weather_text, (600, info_y))

        # Инструкции
        info_y += 40
        controls_text = self.font.render(
            "Управление: Стрелки - движение, Пробел - тушить, S - сохранить, L - загрузить", True, BLACK)
        self.screen.blit(controls_text, (10, info_y))

        # Сообщение о конце игры
        if self.game_over:
            game_over_text = self.font.render("Игра окончена! Нажмите R для перезапуска", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def save_game(self):
        """Сохранение игры в файл"""
        save_data = {
            "width": self.width,
            "height": self.height,
            "helicopter": {
                "x": self.helicopter.x,
                "y": self.helicopter.y,
                "water_tanks": self.helicopter.water_tanks,
                "water_amount": self.helicopter.water_amount,
                "max_water": self.helicopter.max_water,
                "score": self.helicopter.score,
                "lives": self.helicopter.lives,
                "last_fire_time": self.helicopter.last_fire_time,
                "fire_interval": self.helicopter.fire_interval
            },
            "game_map": [[cell.value for cell in row] for row in self.game_map.grid],
            "weather": self.weather,
            "last_weather_change": self.last_weather_change
        }

        with open("helicopter_save.json", "w") as f:
            json.dump(save_data, f)

    def load_game(self):
        """Загрузка игры из файла"""
        try:
            with open("helicopter_save.json", "r") as f:
                save_data = json.load(f)

                self.width = save_data["width"]
                self.height = save_data["height"]
                self.game_map = GameMap(self.width, self.height)

                # Восстанавливаем карту
                for y in range(self.height):
                    for x in range(self.width):
                        self.game_map.grid[y][x] = CellState(save_data["game_map"][y][x])

                # Восстанавливаем вертолет
                heli_data = save_data["helicopter"]
                self.helicopter = Helicopter(heli_data["x"], heli_data["y"], self.game_map)
                self.helicopter.water_tanks = heli_data["water_tanks"]
                self.helicopter.water_amount = heli_data["water_amount"]
                self.helicopter.max_water = heli_data["max_water"]
                self.helicopter.score = heli_data["score"]
                self.helicopter.lives = heli_data["lives"]
                self.helicopter.last_fire_time = heli_data["last_fire_time"]
                self.helicopter.fire_interval = heli_data["fire_interval"]

                # Восстанавливаем погоду
                self.weather = save_data["weather"]
                self.last_weather_change = save_data["last_weather_change"]

                self.game_over = False
        except FileNotFoundError:
            print("Файл сохранения не найден")

    def run(self):
        """Основной игровой цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # 10 FPS

        pygame.quit()


# Запуск игры
if __name__ == "__main__":
    print("Добро пожаловать в игру 'Пожарный вертолет'!")
    print("Правила:")
    print("- Тушите горящие деревья (красные клетки), пролетая над ними и нажимая Пробел")
    print("- Набирайте воду, пролетая над рекой (синие клетки)")
    print("- Посещайте госпиталь (зеленые клетки) для лечения (стоит 50 очков)")
    print("- Посещайте магазин (желтые клетки) для улучшения вертолета (стоит 100 очков)")
    print("- Управление: стрелки - движение, Пробел - тушить, S - сохранить, L - загрузить")

    width = int(input("Введите ширину карты (рекомендуется 20): ") or 20)
    height = int(input("Введите высоту карты (рекомендуется 15): ") or 15)

    game = FireHelicopterGame(width, height)
    game.run()