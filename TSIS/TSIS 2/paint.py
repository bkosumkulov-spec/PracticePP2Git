import pygame
import datetime

from tools import (
    draw_right_triangle, draw_equilateral_triangle, draw_rhombus,
    draw_square, draw_line, draw_rectangle, draw_circle,
    draw_brush, draw_eraser, flood_fill,
    render_text, render_text_preview, draw_toolbar
)

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 1000, 600
    TOOLBAR_HEIGHT = 50
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT + TOOLBAR_HEIGHT))
    clock  = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    RED   = (255, 0,   0)
    GREEN = (0,   255, 0)
    BLUE  = (0,   0,   255)

    THICKNESS_MAP = {1: 2, 2: 5, 3: 10}
    thickness_level = 1
    current_color   = BLUE
    mode            = 'brush'

    SHAPE_MODES = {'rectangle', 'circle', 'square',
                   'right_triangle', 'eq_triangle', 'rhombus', 'line'}

    start_pos    = None
    prev_pos     = None
    line_preview = None

    text_mode  = False
    text_pos   = None
    text_input = ''
    font       = pygame.font.SysFont('Arial', 20)
    font_small = pygame.font.SysFont('Arial', 12) 

    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(WHITE)
    
    toolbar_rect = pygame.Rect(0, 0, WIDTH, TOOLBAR_HEIGHT)

    while True:
        lw = THICKNESS_MAP[thickness_level]
        
        raw_mouse_pos = pygame.mouse.get_pos()
        mouse_on_canvas = (raw_mouse_pos[0], raw_mouse_pos[1] - TOOLBAR_HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if text_mode:
                    if event.key == pygame.K_RETURN:
                        if text_pos and text_input:
                            render_text(canvas, font, text_input, text_pos, current_color)
                        text_mode, text_pos, text_input = False, None, ''
                    elif event.key == pygame.K_ESCAPE:
                        text_mode, text_pos, text_input = False, None, ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        if event.unicode: text_input += event.unicode
                else:
                    mods = pygame.key.get_mods()
                    if event.key == pygame.K_s and (mods & pygame.KMOD_CTRL):
                        ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                        pygame.image.save(canvas, f'canvas_{ts}.png')

                    keys_to_modes = {
                        pygame.K_r: 'rectangle', pygame.K_s: 'square', pygame.K_c: 'circle',
                        pygame.K_t: 'eq_triangle', pygame.K_y: 'right_triangle',
                        pygame.K_d: 'rhombus', pygame.K_l: 'line', pygame.K_b: 'brush',
                        pygame.K_e: 'eraser', pygame.K_f: 'fill', pygame.K_x: 'text'
                    }
                    if event.key in keys_to_modes:
                        mode = keys_to_modes[event.key]
                        if mode == 'text': text_mode = False

                    if event.key == pygame.K_1: current_color = BLACK
                    elif event.key == pygame.K_2: current_color = RED
                    elif event.key == pygame.K_3: current_color = GREEN
                    elif event.key == pygame.K_4: current_color = BLUE
                    
                    if event.key in [pygame.K_KP1, pygame.K_5]: thickness_level = 1
                    if event.key in [pygame.K_KP2, pygame.K_6]: thickness_level = 2
                    if event.key in [pygame.K_KP3, pygame.K_7]: thickness_level = 3

            if event.type == pygame.MOUSEBUTTONDOWN:
                if raw_mouse_pos[1] > TOOLBAR_HEIGHT:
                    if mode == 'text':
                        text_mode, text_pos, text_input = True, mouse_on_canvas, ''
                    elif mode == 'fill':
                        flood_fill(canvas, mouse_on_canvas, current_color)
                    elif mode in SHAPE_MODES:
                        start_pos = mouse_on_canvas

            if event.type == pygame.MOUSEMOTION:
                if mode == 'line' and start_pos is not None:
                    line_preview = mouse_on_canvas

            if event.type == pygame.MOUSEBUTTONUP:
                if mode in SHAPE_MODES and start_pos is not None:
                    end_pos = mouse_on_canvas
                    if mode == 'rectangle': draw_rectangle(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'square': draw_square(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'circle': draw_circle(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'right_triangle': draw_right_triangle(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'eq_triangle': draw_equilateral_triangle(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'rhombus': draw_rhombus(canvas, current_color, start_pos, end_pos, lw)
                    elif mode == 'line': draw_line(canvas, current_color, start_pos, end_pos, lw)
                    
                    start_pos, line_preview = None, None

        if pygame.mouse.get_pressed()[0] and raw_mouse_pos[1] > TOOLBAR_HEIGHT:
            if mode == 'brush':
                draw_brush(canvas, current_color, prev_pos, mouse_on_canvas, lw)
                prev_pos = mouse_on_canvas
            elif mode == 'eraser':
                draw_eraser(canvas, WHITE, prev_pos, mouse_on_canvas, lw)
                prev_pos = mouse_on_canvas
        else:
            prev_pos = None

        screen.fill((50, 50, 50))
        screen.blit(canvas, (0, TOOLBAR_HEIGHT))

        if mode == 'line' and start_pos and line_preview:
            p1 = (start_pos[0], start_pos[1] + TOOLBAR_HEIGHT)
            p2 = (line_preview[0], line_preview[1] + TOOLBAR_HEIGHT)
            draw_line(screen, current_color, p1, p2, lw)

        if text_mode and text_pos:
            p_text = (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT)
            render_text_preview(screen, font, text_input, p_text, current_color)

        draw_toolbar(screen, mode, current_color, thickness_level, toolbar_rect, font_small)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()