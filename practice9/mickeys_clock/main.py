import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey's Clock")

from clock import draw_clock

fps_clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock(screen)
    pygame.display.flip()
    fps_clock.tick(60)

pygame.quit()