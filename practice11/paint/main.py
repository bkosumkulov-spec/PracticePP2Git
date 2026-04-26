import pygame
import math
 
 
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
 
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock  = pygame.time.Clock()
 
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    RED   = (255, 0,   0)
    GREEN = (0,   255, 0)
    BLUE  = (0,   0,   255)
 
    radius        = 15
    current_color = BLUE
    mode          = 'brush'
 
    SHAPE_MODES = {'rectangle', 'circle', 'square',
                   'right_triangle', 'eq_triangle', 'rhombus'}
 
    start_pos = None
 
    screen.fill(WHITE)
 
    while True:
        pygame.display.set_caption(
            f"Mode: {mode} | Color: {current_color} | "
            "R-Rect  S-Square  C-Circle  T-EqTriangle  Y-RightTri  D-Rhombus  "
            "B-Brush  E-Eraser | 0-Black  1-Red  2-Green  3-Blue"
        )
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'rectangle'
                if event.key == pygame.K_s: mode = 'square'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_t: mode = 'eq_triangle'
                if event.key == pygame.K_y: mode = 'right_triangle'
                if event.key == pygame.K_d: mode = 'rhombus'
                if event.key == pygame.K_b: mode = 'brush'
                if event.key == pygame.K_e: mode = 'eraser'
                if event.key == pygame.K_0: current_color = BLACK
                if event.key == pygame.K_1: current_color = RED
                if event.key == pygame.K_2: current_color = GREEN
                if event.key == pygame.K_3: current_color = BLUE
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode in SHAPE_MODES:
                    start_pos = event.pos
 
            if event.type == pygame.MOUSEBUTTONUP:
                if start_pos is None:
                    continue
 
                end_pos = event.pos
 
                if mode == 'rectangle':
                    w = end_pos[0] - start_pos[0]
                    h = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, current_color,
                                     (start_pos[0], start_pos[1], w, h), 2)
 
                elif mode == 'square':
                    draw_square(screen, current_color, start_pos, end_pos)
 
                elif mode == 'circle':
                    r = int(math.hypot(end_pos[0] - start_pos[0],
                                       end_pos[1] - start_pos[1]))
                    pygame.draw.circle(screen, current_color, start_pos, r, 2)
 
                elif mode == 'right_triangle':
                    draw_right_triangle(screen, current_color, start_pos, end_pos)
 
                elif mode == 'eq_triangle':
                    draw_equilateral_triangle(screen, current_color, start_pos, end_pos)
 
                elif mode == 'rhombus':
                    draw_rhombus(screen, current_color, start_pos, end_pos)
 
                start_pos = None
 
        if pygame.mouse.get_pressed()[0]:
            curr_pos = pygame.mouse.get_pos()
            if mode == 'brush':
                pygame.draw.circle(screen, current_color, curr_pos, radius)
            elif mode == 'eraser':
                pygame.draw.circle(screen, WHITE, curr_pos, radius)
 
        pygame.display.flip()
        clock.tick(60)
 
 
if __name__ == '__main__':
    main()