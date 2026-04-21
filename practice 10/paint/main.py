import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Paint Extension")
    
    clock = pygame.time.Clock()
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    radius = 15
    current_color = BLUE
    mode = 'brush' 
    
    points = [] 

    start_pos = None

    screen.fill(WHITE)

    while True:
        
        pygame.display.set_caption(f"Mode: {mode} | Color: {current_color} | Press: R-Rect, C-Circle, B-Brush, E-Eraser, 1-Red, 2-Green, 3-Blue")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'rectangle'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_b: mode = 'brush'
                if event.key == pygame.K_e: mode = 'eraser'
                if event.key == pygame.K_1: current_color = RED
                if event.key == pygame.K_2: current_color = GREEN
                if event.key == pygame.K_3: current_color = BLUE
                if event.key == pygame.K_0: current_color = BLACK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode in ['rectangle', 'circle']:
                    start_pos = event.pos
                
            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rectangle' and start_pos:
                    end_pos = event.pos
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), 2)
                    start_pos = None
                
                elif mode == 'circle' and start_pos:
                    end_pos = event.pos
                    r = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, current_color, start_pos, r, 2)
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