import pygame
import math
from collections import deque
 
 
def draw_right_triangle(surface, color, start_pos, end_pos, line_width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    p1 = (x1, y1)
    p2 = (x2, y1)
    p3 = (x1, y2)
    pygame.draw.polygon(surface, color, [p1, p2, p3], line_width)
 
 
def draw_equilateral_triangle(surface, color, start_pos, end_pos, line_width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    base_len = x2 - x1
    height = (math.sqrt(3) / 2) * abs(base_len)
    direction = 1 if y2 >= y1 else -1
    p1 = (x1, y1)
    p2 = (x2, y1)
    p3 = (x1 + base_len / 2, y1 + direction * height)
    pygame.draw.polygon(surface, color, [p1, p2, p3], line_width)
 
 
def draw_rhombus(surface, color, start_pos, end_pos, line_width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    top    = (mid_x, y1)
    right  = (x2,    mid_y)
    bottom = (mid_x, y2)
    left   = (x1,    mid_y)
    pygame.draw.polygon(surface, color, [top, right, bottom, left], line_width)
 
 
def draw_square(surface, color, start_pos, end_pos, line_width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    side = min(abs(x2 - x1), abs(y2 - y1))
    sign_x = 1 if x2 >= x1 else -1
    sign_y = 1 if y2 >= y1 else -1
    pygame.draw.rect(surface, color, (x1, y1, sign_x * side, sign_y * side), line_width)
 
 
def draw_line(surface, color, start_pos, end_pos, line_width=2):
    pygame.draw.line(surface, color, start_pos, end_pos, line_width)
 
 
def draw_rectangle(surface, color, start_pos, end_pos, line_width=2):
    w = end_pos[0] - start_pos[0]
    h = end_pos[1] - start_pos[1]
    pygame.draw.rect(surface, color, (start_pos[0], start_pos[1], w, h), line_width)
 
 
def draw_circle(surface, color, start_pos, end_pos, line_width=2):
    r = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.circle(surface, color, start_pos, r, line_width)
 
 
def draw_brush(surface, color, prev_pos, curr_pos, radius):
    if prev_pos is not None:
        pygame.draw.line(surface, color, prev_pos, curr_pos, radius * 2)
    pygame.draw.circle(surface, color, curr_pos, radius)
 
 
def draw_eraser(surface, bg_color, prev_pos, curr_pos, radius):
    if prev_pos is not None:
        pygame.draw.line(surface, bg_color, prev_pos, curr_pos, radius * 2)
    pygame.draw.circle(surface, bg_color, curr_pos, radius)
 
 
def flood_fill(surface, pos, fill_color):
    x, y = pos
    w, h = surface.get_size()
    if x < 0 or x >= w or y < 0 or y >= h:
        return
 
    target_color = surface.get_at((x, y))[:3]
    fill_rgb = fill_color[:3]
 
    if target_color == fill_rgb:
        return
 
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))
 
    while queue:
        cx, cy = queue.popleft()
        if surface.get_at((cx, cy))[:3] != target_color:
            continue
        surface.set_at((cx, cy), fill_color)
 
        for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                if surface.get_at((nx, ny))[:3] == target_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
 
 
def render_text(surface, font, text, pos, color):
    text_surf = font.render(text, True, color)
    surface.blit(text_surf, pos)
 
 
def render_text_preview(surface, font, text, pos, color):
    preview_surf = font.render(text + '|', True, color)
    surface.blit(preview_surf, pos)
    
def draw_toolbar(screen, mode, current_color, thickness_level, toolbar_rect, font_small):
    TOOLBAR_BG   = (30,  30,  30)
    ACTIVE_BG    = (70,  70, 130)
    INACTIVE_BG  = (50,  50,  50)
    BORDER_ACT   = (120, 120, 220)
    BORDER_INACT = (80,  80,  80)
    TEXT_COLOR   = (220, 220, 220)
    DIM_COLOR    = (130, 130, 130)

    TOOL_BUTTONS = [
        ('brush', 'B', 'Brush'), ('eraser', 'E', 'Eraser'),
        ('line', 'L', 'Line'), ('rectangle', 'R', 'Rect'),
        ('square', 'S', 'Square'), ('circle', 'C', 'Circle'),
        ('eq_triangle', 'T', 'EqTri'), ('right_triangle', 'Y', 'RTri'),
        ('rhombus', 'D', 'Rhombus'), ('fill', 'F', 'Fill'), ('text', 'X', 'Text'),
    ]

    pygame.draw.rect(screen, TOOLBAR_BG, toolbar_rect)
    
    tx = toolbar_rect.x + 8
    ty = toolbar_rect.y + 6
    btn_h = toolbar_rect.height - 12
    btn_w = 60

    for tool_mode, key, label in TOOL_BUTTONS:
        is_active = (mode == tool_mode)
        bg = ACTIVE_BG if is_active else INACTIVE_BG
        border = BORDER_ACT if is_active else BORDER_INACT
        rect = pygame.Rect(tx, ty, btn_w, btn_h)

        pygame.draw.rect(screen, bg, rect, border_radius=4)
        pygame.draw.rect(screen, border, rect, 1, border_radius=4)

        key_surf = font_small.render(key, True, BORDER_ACT if is_active else DIM_COLOR)
        label_surf = font_small.render(label, True, TEXT_COLOR)
        screen.blit(key_surf, (rect.x + 5, rect.y + 2))
        screen.blit(label_surf, (rect.x + 5, rect.y + 15))
        tx += btn_w + 4

    tx += 10
    colors = [((0,0,0), '0'), ((255,0,0), '1'), ((0,255,0), '2'), ((0,0,255), '3')]
    for col, key in colors:
        is_active = (current_color == col)
        rect = pygame.Rect(tx, ty, btn_h, btn_h)
        pygame.draw.rect(screen, col, rect, border_radius=3)
        if is_active:
            pygame.draw.rect(screen, (255, 255, 255), rect, 2, border_radius=3)
        tx += btn_h + 4    