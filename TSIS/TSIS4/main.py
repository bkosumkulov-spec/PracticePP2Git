# main.py — экрандар мен бағдарламаның негізгі файлы
import pygame
import sys
import json
import os

from config import *
from db import init_db, get_or_create_player, save_session, get_top10, get_best
from game import Game

SETTINGS_FILE = "settings.json"


def load_settings():
    default = {"snake_color": [0, 200, 0], "grid": True, "sound": False}
    if not os.path.exists(SETTINGS_FILE):
        return default
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def save_settings(s):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(s, f, indent=4)


# ── Жалпы көмекші функциялар ──────────────────────
def draw_text(surf, text, x, y, font, color=WHITE):
    surf.blit(font.render(text, True, color), (x, y))


def draw_button(surf, font, text, rect, hover=False):
    color = (60, 60, 90) if hover else (40, 40, 70)
    pygame.draw.rect(surf, color, rect, border_radius=6)
    pygame.draw.rect(surf, CYAN, rect, 2, border_radius=6)
    t = font.render(text, True, WHITE)
    surf.blit(t, t.get_rect(center=(rect[0]+rect[2]//2, rect[1]+rect[3]//2)))


def mouse_over(rect):
    return pygame.Rect(rect).collidepoint(pygame.mouse.get_pos())


def clicked(event, rect):
    return (event.type == pygame.MOUSEBUTTONDOWN and
            event.button == 1 and
            pygame.Rect(rect).collidepoint(event.pos))


# ══════════════════════════════════════════════════
#  1. БАС МӘЗІР
# ══════════════════════════════════════════════════
def menu_screen(screen, db_ok):
    font_big  = pygame.font.SysFont("consolas", 42, bold=True)
    font      = pygame.font.SysFont("consolas", 22)
    font_sm   = pygame.font.SysFont("consolas", 15)
    clock     = pygame.time.Clock()
    username  = ""

    # Батырмалар: (мәтін, rect)
    cx = WIDTH // 2
    btns = [
        ("ОЙНА",        (cx-110, 290, 220, 44)),
        ("РЕКОРДТАР",   (cx-110, 350, 220, 44)),
        ("БАПТАУЛАР",   (cx-110, 410, 220, 44)),
        ("ШЫҒУ",        (cx-110, 470, 220, 44)),
    ]

    blink = True
    blink_t = pygame.time.get_ticks()

    while True:
        screen.fill(BLACK)
        draw_text(screen, "SNAKE GAME", cx - 140, 60, font_big, GREEN)

        # Username енгізу
        draw_text(screen, "Атыңды енгіз:", cx - 110, 190, font_sm, GRAY)
        inp_rect = (cx - 110, 210, 220, 38)
        pygame.draw.rect(screen, (20, 20, 20), inp_rect, border_radius=5)
        pygame.draw.rect(screen, CYAN, inp_rect, 2, border_radius=5)

        now = pygame.time.get_ticks()
        if now - blink_t > 500:
            blink = not blink
            blink_t = now
        disp = username + ("|" if blink else " ")
        draw_text(screen, disp, cx - 100, 218, font)

        if not db_ok:
            draw_text(screen, "DB жок — offline режим", cx - 110, 260, font_sm, ORANGE)

        for text, rect in btns:
            draw_button(screen, font, text, rect, mouse_over(rect))

        pygame.display.flip()
        clock.tick(60)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN and username.strip():
                    return "play", username.strip()
                elif ev.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif ev.unicode.isprintable() and len(username) < 18:
                    username += ev.unicode
            for i, (text, rect) in enumerate(btns):
                if clicked(ev, rect):
                    if i == 0 and username.strip():
                        return "play", username.strip()
                    elif i == 1:
                        return "leaderboard", username.strip()
                    elif i == 2:
                        return "settings", username.strip()
                    elif i == 3:
                        pygame.quit(); sys.exit()


# ══════════════════════════════════════════════════
#  2. GAME OVER
# ══════════════════════════════════════════════════
def gameover_screen(screen, score, level, best):
    font_big = pygame.font.SysFont("consolas", 40, bold=True)
    font     = pygame.font.SysFont("consolas", 24)
    clock    = pygame.time.Clock()
    cx = WIDTH // 2

    btn_retry = (cx - 110, 360, 220, 44)
    btn_menu  = (cx - 110, 420, 220, 44)

    while True:
        screen.fill(BLACK)
        draw_text(screen, "GAME OVER", cx - 120, 80, font_big, RED)
        draw_text(screen, f"Ұпай:   {score}",          cx - 110, 190, font)
        draw_text(screen, f"Деңгей: {level}",          cx - 110, 230, font)
        draw_text(screen, f"Рекорд: {max(score,best)}", cx - 110, 270, font, YELLOW)

        if score > best:
            draw_text(screen, "Жаңа рекорд!", cx - 80, 315, font, YELLOW)

        draw_button(screen, font, "ҚАЙТА ОЙНА", btn_retry, mouse_over(btn_retry))
        draw_button(screen, font, "БАС МӘЗІР",  btn_menu,  mouse_over(btn_menu))
        pygame.display.flip()
        clock.tick(60)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if clicked(ev, btn_retry): return "retry"
            if clicked(ev, btn_menu):  return "menu"


# ══════════════════════════════════════════════════
#  3. РЕКОРДТАР
# ══════════════════════════════════════════════════
def leaderboard_screen(screen, db_ok):
    font_big = pygame.font.SysFont("consolas", 32, bold=True)
    font     = pygame.font.SysFont("consolas", 18)
    clock    = pygame.time.Clock()
    cx = WIDTH // 2
    rows = get_top10() if db_ok else []
    btn_back = (cx - 80, 530, 160, 40)

    while True:
        screen.fill(BLACK)
        draw_text(screen, "ТОП 10", cx - 70, 20, font_big, YELLOW)
        draw_text(screen, "#   АТЫ          ҰПАЙ  ДЕҢГЕЙ  КҮН", 20, 70, font, CYAN)
        pygame.draw.line(screen, CYAN, (20, 92), (WIDTH-20, 92), 1)

        if not db_ok:
            draw_text(screen, "Дерекқорға қосылу мүмкін болмады", 40, 150, font, ORANGE)
        elif not rows:
            draw_text(screen, "Нәтиже жоқ", cx - 60, 150, font)
        else:
            for i, (name, score, level, date) in enumerate(rows):
                y = 100 + i * 38
                line = f"{i+1:<3} {name:<14} {score:<6} {level:<7} {date}"
                color = YELLOW if i == 0 else WHITE
                draw_text(screen, line, 20, y, font, color)

        draw_button(screen, font, "АРТҚА", btn_back, mouse_over(btn_back))
        pygame.display.flip()
        clock.tick(60)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return
            if clicked(ev, btn_back):
                return


# ══════════════════════════════════════════════════
#  4. БАПТАУЛАР
# ══════════════════════════════════════════════════
def settings_screen(screen, settings):
    font_big = pygame.font.SysFont("consolas", 32, bold=True)
    font     = pygame.font.SysFont("consolas", 22)
    clock    = pygame.time.Clock()
    s = dict(settings)
    cx = WIDTH // 2

    COLORS = [
        ([0, 200, 0],   "Жасыл"),
        ([0, 180, 220], "Көк"),
        ([220, 180, 0], "Сары"),
        ([200, 50, 200],"Күлгін"),
        ([255, 255, 255],"Ақ"),
    ]
    ci = next((i for i, (c, _) in enumerate(COLORS) if c == s["snake_color"]), 0)

    btn_prev  = (cx - 150, 200, 40, 36)
    btn_next  = (cx + 110, 200, 40, 36)
    btn_grid  = (cx - 110, 270, 220, 40)
    btn_sound = (cx - 110, 330, 220, 40)
    btn_save  = (cx - 110, 430, 220, 40)

    while True:
        screen.fill(BLACK)
        draw_text(screen, "БАПТАУЛАР", cx - 100, 30, font_big, CYAN)

        # Жылан түсі
        draw_text(screen, "Жылан түсі:", cx - 110, 165, font)
        color_val, color_name = COLORS[ci]
        pygame.draw.rect(screen, color_val, (cx - 105, 200, 210, 36), border_radius=5)
        draw_text(screen, color_name, cx - 40, 208, font)
        draw_button(screen, font, "<", btn_prev, mouse_over(btn_prev))
        draw_button(screen, font, ">", btn_next, mouse_over(btn_next))

        # Grid
        grid_lbl = "Grid: ҚОСУЛЫ" if s["grid"] else "Grid: ӨШІРУЛІ"
        draw_button(screen, font, grid_lbl, btn_grid, mouse_over(btn_grid))

        # Дыбыс
        sound_lbl = "Дыбыс: ҚОСУЛЫ" if s["sound"] else "Дыбыс: ӨШІРУЛІ"
        draw_button(screen, font, sound_lbl, btn_sound, mouse_over(btn_sound))

        draw_button(screen, font, "САҚТА", btn_save, mouse_over(btn_save))
        pygame.display.flip()
        clock.tick(60)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return settings
            if clicked(ev, btn_prev):
                ci = (ci - 1) % len(COLORS)
                s["snake_color"] = COLORS[ci][0]
            if clicked(ev, btn_next):
                ci = (ci + 1) % len(COLORS)
                s["snake_color"] = COLORS[ci][0]
            if clicked(ev, btn_grid):
                s["grid"] = not s["grid"]
            if clicked(ev, btn_sound):
                s["sound"] = not s["sound"]
            if clicked(ev, btn_save):
                save_settings(s)
                return s


# ══════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game — TSIS 4")

    settings  = load_settings()
    db_ok     = init_db()
    player_id = None
    best      = 0
    state     = "menu"
    score     = 0
    level     = 1
    username  = ""

    while True:
        if state == "menu":
            action, username = menu_screen(screen, db_ok)
            if action == "play":
                if db_ok and username:
                    player_id = get_or_create_player(username)
                    best = get_best(player_id) if player_id else 0
                state = "game"
            elif action == "leaderboard":
                leaderboard_screen(screen, db_ok)
            elif action == "settings":
                settings = settings_screen(screen, settings)

        elif state == "game":
            g = Game(screen, settings, best)
            score, level = g.run()
            if db_ok and player_id:
                save_session(player_id, score, level)
                best = max(best, score)
            state = "gameover"

        elif state == "gameover":
            action = gameover_screen(screen, score, level, best)
            state = "game" if action == "retry" else "menu"


if __name__ == "__main__":
    main()