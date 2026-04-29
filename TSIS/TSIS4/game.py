# game.py — ойын логикасы
import pygame
import random
from config import *


class Snake:
    def __init__(self, color):
        self.body = [(COLS//2, ROWS//2), (COLS//2-1, ROWS//2), (COLS//2-2, ROWS//2)]
        self.dir  = (1, 0)
        self.next_dir = (1, 0)
        self.grow_n = 0
        self.color  = color
        self.shield = False

    def turn(self, d):
        # Кері бағытқа бұрылмайды
        if (d[0] * -1, d[1] * -1) != self.dir:
            self.next_dir = d

    def move(self):
        self.dir = self.next_dir
        x, y = self.body[0]
        head = (x + self.dir[0], y + self.dir[1])
        self.body.insert(0, head)
        if self.grow_n > 0:
            self.grow_n -= 1
        else:
            self.body.pop()

    def grow(self, n=1):
        self.grow_n += n

    def shrink(self, n=2):
        for _ in range(n):
            if len(self.body) > 1:
                self.body.pop()

    def hits_wall(self):
        x, y = self.body[0]
        return not (0 <= x < COLS and 0 <= y < ROWS)

    def hits_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, surf):
        for i, (cx, cy) in enumerate(self.body):
            color = tuple(min(255, c+60) for c in self.color) if i == 0 else self.color
            pygame.draw.rect(surf, color,
                             (cx*CELL+1, cy*CELL+1, CELL-2, CELL-2), border_radius=3)
        if self.shield:
            hx, hy = self.body[0]
            pygame.draw.rect(surf, CYAN,
                             (hx*CELL-1, hy*CELL-1, CELL+2, CELL+2), 2, border_radius=4)


class Food:
    # type: "normal" | "bonus" | "poison"
    COLORS = {"normal": RED, "bonus": YELLOW, "poison": DARK_RED}
    POINTS = {"normal": 1,   "bonus": 3,      "poison": 0}

    def __init__(self, ftype, pos):
        self.type  = ftype
        self.pos   = pos
        self.born  = pygame.time.get_ticks()

    def expired(self):
        # Тек бонус тамақ 7 секундта жоғалады
        if self.type == "bonus":
            return pygame.time.get_ticks() - self.born > 7000
        return False

    def draw(self, surf):
        cx = self.pos[0]*CELL + CELL//2
        cy = self.pos[1]*CELL + CELL//2
        pygame.draw.circle(surf, self.COLORS[self.type], (cx, cy), CELL//2 - 2)
        if self.type == "poison":
            # X белгісі
            d = CELL//2 - 4
            pygame.draw.line(surf, WHITE, (cx-d, cy-d), (cx+d, cy+d), 2)
            pygame.draw.line(surf, WHITE, (cx+d, cy-d), (cx-d, cy+d), 2)


class PowerUp:
    COLORS = {"speed": ORANGE, "slow": BLUE, "shield": PURPLE}
    LABELS = {"speed": "S",    "slow": "~",  "shield": "#"}

    def __init__(self, ptype, pos):
        self.type = ptype
        self.pos  = pos
        self.born = pygame.time.get_ticks()

    def expired(self):
        return pygame.time.get_ticks() - self.born > 8000

    def draw(self, surf, font):
        cx = self.pos[0]*CELL + CELL//2
        cy = self.pos[1]*CELL + CELL//2
        pygame.draw.rect(surf, self.COLORS[self.type],
                         (self.pos[0]*CELL+1, self.pos[1]*CELL+1, CELL-2, CELL-2),
                         border_radius=4)
        t = font.render(self.LABELS[self.type], True, WHITE)
        surf.blit(t, t.get_rect(center=(cx, cy)))


class Game:
    def __init__(self, screen, settings, best=0):
        self.screen   = screen
        self.settings = settings
        self.best     = best
        self.font     = pygame.font.SysFont("consolas", 18)
        self.clock    = pygame.time.Clock()
        self._init()

    def _init(self):
        color = tuple(self.settings["snake_color"])
        self.snake  = Snake(color)
        self.score  = 0
        self.level  = 1
        self.eaten  = 0
        self.fps    = FPS_BASE
        self.foods  = []
        self.powerup = None
        self.obstacles = []        # [(x,y), ...]
        self.effect  = None        # "speed" | "slow" | None
        self.effect_t = 0
        self._spawn_food()

    def _free_cells(self):
        used = set(self.snake.body) | set(self.obstacles)
        if self.powerup:
            used.add(self.powerup.pos)
        for f in self.foods:
            used.add(f.pos)
        return used

    def _rand_pos(self):
        used = self._free_cells()
        for _ in range(500):
            p = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
            if p not in used:
                return p
        return None

    def _spawn_food(self):
        pos = self._rand_pos()
        if pos:
            self.foods.append(Food("normal", pos))
        # 20% — улы, 25% — бонус
        r = random.random()
        pos2 = self._rand_pos()
        if pos2:
            if r < 0.20:
                self.foods.append(Food("poison", pos2))
            elif r < 0.45:
                self.foods.append(Food("bonus", pos2))

    def _spawn_powerup(self):
        if self.powerup:
            return
        if random.random() < 0.4:
            pos = self._rand_pos()
            if pos:
                ptype = random.choice(["speed", "slow", "shield"])
                self.powerup = PowerUp(ptype, pos)

    def _level_up(self):
        self.level += 1
        self.eaten  = 0
        self.fps    = min(FPS_BASE + self.level - 1, FPS_MAX)
        self.foods  = []
        self._spawn_food()
        self._spawn_powerup()
        # Кедергілер Level 3-тен
        if self.level >= 3:
            self._add_obstacles()

    def _add_obstacles(self):
        count = (self.level - 2) * 3  # Level3→3, Level4→6 ...
        hx, hy = self.snake.body[0]
        safe = {(hx+dx, hy+dy) for dx in range(-3,4) for dy in range(-3,4)}
        used = self._free_cells() | safe
        for _ in range(count):
            pos = None
            for _ in range(200):
                p = (random.randint(1, COLS-2), random.randint(1, ROWS-2))
                if p not in used:
                    pos = p
                    break
            if pos:
                self.obstacles.append(pos)
                used.add(pos)

    def _cur_fps(self):
        if self.effect == "speed":
            return int(self.fps * 1.8)
        if self.effect == "slow":
            return int(self.fps * 0.5)
        return self.fps

    def run(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit(); raise SystemExit
                if ev.type == pygame.KEYDOWN:
                    if ev.key in (pygame.K_UP,    pygame.K_w): self.snake.turn((0,-1))
                    if ev.key in (pygame.K_DOWN,  pygame.K_s): self.snake.turn((0, 1))
                    if ev.key in (pygame.K_LEFT,  pygame.K_a): self.snake.turn((-1,0))
                    if ev.key in (pygame.K_RIGHT, pygame.K_d): self.snake.turn((1, 0))
                    if ev.key == pygame.K_ESCAPE:
                        return self.score, self.level

            now = pygame.time.get_ticks()

            # Эффект уақыты аяқталды ма
            if self.effect in ("speed", "slow"):
                if now - self.effect_t > 5000:
                    self.effect = None

            # Мерзімі өткен тамақтарды жою
            self.foods = [f for f in self.foods if not f.expired()]
            if not self.foods:
                self._spawn_food()

            # Power-up алаңнан жоғалу
            if self.powerup and self.powerup.expired():
                self.powerup = None

            # Жылан қозғалуы
            self.snake.move()
            head = self.snake.body[0]

            # Қабырғаға соқтығысу
            if self.snake.hits_wall():
                if self.snake.shield:
                    self.snake.shield = False
                    # Жыланды шекараға қайтару
                    x = max(0, min(COLS-1, head[0]))
                    y = max(0, min(ROWS-1, head[1]))
                    self.snake.body[0] = (x, y)
                else:
                    return self.score, self.level

            # Өзіне соқтығысу
            if self.snake.hits_self():
                if self.snake.shield:
                    self.snake.shield = False
                else:
                    return self.score, self.level

            # Кедергіге соқтығысу
            if head in self.obstacles:
                if self.snake.shield:
                    self.snake.shield = False
                    self.snake.body[0] = self.snake.body[1]
                else:
                    return self.score, self.level

            # Тамақ жеу
            for f in list(self.foods):
                if head == f.pos:
                    self.foods.remove(f)
                    if f.type == "poison":
                        self.snake.shrink(2)
                        if len(self.snake.body) <= 1:
                            return self.score, self.level
                    else:
                        self.snake.grow()
                        self.score += f.POINTS[f.type]
                        self.eaten += 1
                    if not self.foods:
                        self._spawn_food()
                        self._spawn_powerup()
                    if self.eaten >= FOOD_TO_LEVEL:
                        self._level_up()
                    break

            # Power-up жинау
            if self.powerup and head == self.powerup.pos:
                p = self.powerup
                self.powerup = None
                if p.type == "shield":
                    self.snake.shield = True
                else:
                    self.effect   = p.type
                    self.effect_t = now

            self._draw()
            self.clock.tick(self._cur_fps())

    def _draw(self):
        self.screen.fill(BLACK)

        # Grid
        if self.settings.get("grid"):
            for x in range(0, WIDTH, CELL):
                pygame.draw.line(self.screen, (20,20,20), (x,0), (x,HEIGHT))
            for y in range(0, HEIGHT, CELL):
                pygame.draw.line(self.screen, (20,20,20), (0,y), (WIDTH,y))

        # Кедергілер
        for (cx, cy) in self.obstacles:
            pygame.draw.rect(self.screen, GRAY, (cx*CELL, cy*CELL, CELL, CELL))

        # Тамақтар
        for f in self.foods:
            f.draw(self.screen)

        # Power-up
        if self.powerup:
            self.powerup.draw(self.screen, self.font)

        # Жылан
        self.snake.draw(self.screen)

        # HUD
        score_t = self.font.render(f"Score:{self.score}  Lvl:{self.level}  Best:{self.best}", True, WHITE)
        self.screen.blit(score_t, (5, 5))

        if self.effect:
            ef = self.font.render(f"[{self.effect.upper()}]", True, ORANGE)
            self.screen.blit(ef, (5, 25))
        if self.snake.shield:
            sh = self.font.render("[SHIELD]", True, PURPLE)
            self.screen.blit(sh, (5, 25))

        pygame.display.flip()