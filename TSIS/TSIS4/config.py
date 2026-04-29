# config.py
WIDTH, HEIGHT = 600, 600
CELL = 20
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

FPS_BASE = 8
FPS_MAX  = 20
FOOD_TO_LEVEL = 5

# Түстер
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GREEN  = (0, 200, 0)
RED    = (200, 0, 0)
DARK_RED = (120, 0, 0)
YELLOW = (255, 220, 0)
ORANGE = (255, 140, 0)
BLUE   = (50, 100, 255)
PURPLE = (150, 0, 220)
GRAY   = (80, 80, 80)
CYAN   = (0, 200, 220)

# Дерекқор — өз мәліметтеріңді жаз
DB = {
    "dbname":   "snake_game",
    "user":     "postgres",
    "password": "1234",
    "host":     "localhost"
}