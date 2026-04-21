# import pygame, sys
# from pygame.locals import *
# import random, time
# from coin import Coin 

# pygame.init()
 
# FPS = 60
# FramePerSec = pygame.time.Clock()

# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
# SPEED = 5
# SCORE = 0

# font = pygame.font.SysFont("Verdana", 60)
# font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("Game Over", True, BLACK)

# background = pygame.image.load("AnimatedStreet.png")

# DISPLAYSURF = pygame.display.set_mode((400,600))
# DISPLAYSURF.fill(WHITE)
# pygame.display.set_caption("Game")


# class Enemy(pygame.sprite.Sprite):
#       def __init__(self):
#         super().__init__() 
#         self.image = pygame.image.load("Enemy.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

#       def move(self):
#         global SCORE
#         self.rect.move_ip(0,SPEED)
#         if (self.rect.bottom > 600):
#             SCORE += 1
#             self.rect.top = 0
#             self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__() 
#         self.image = pygame.image.load("Player.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (160, 520)
       
#     def move(self):
#         pressed_keys = pygame.key.get_pressed()
        
#         if self.rect.left > 0:
#               if pressed_keys[K_a]:
#                   self.rect.move_ip(-5, 0)
#         if self.rect.right < SCREEN_WIDTH:        
#               if pressed_keys[K_d]:
#                   self.rect.move_ip(5, 0)
#         if self.rect.bottom < SCREEN_HEIGHT:
#             if pressed_keys[K_s]:
#                 self.rect.move_ip(0,5)
#         if self.rect.top > 0:
#             if pressed_keys[K_w]:
#                 self.rect.move_ip(0,-5)     
                
# class Coin:
#     def __init__(self, x, y, radius, screen_width, screen_height):
#         self.x = random.randint(0,400)
#         self.y = random.randint(0,600)
#         self.radius = radius
#         self.screen_width = screen_width
#         self.screen_height = screen_height
    
#     def draw(self, screen):
#         pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)                     
                       
# P1 = Player()
# E1 = Enemy()

# enemies = pygame.sprite.Group()
# enemies.add(E1)
# all_sprites = pygame.sprite.Group()
# all_sprites.add(P1)
# all_sprites.add(E1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# coin = Coin(
#     x=SCREEN_WIDTH // 2,
#     y=SCREEN_HEIGHT // 2,
#     radius=10,
#     screen_width=SCREEN_WIDTH,
#     screen_height=SCREEN_HEIGHT
# )

# while True:
      
#     for event in pygame.event.get():
#         if event.type == INC_SPEED:
#               SPEED += 0.5      
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()


#     DISPLAYSURF.blit(background, (0,0))
#     scores = font_small.render(str(SCORE), True, BLACK)
#     DISPLAYSURF.blit(scores, (10,10))

#     for entity in all_sprites:
#         entity.move()
#         DISPLAYSURF.blit(entity.image, entity.rect)
        

#     if pygame.sprite.spritecollideany(P1, enemies):
#           pygame.mixer.Sound('crash.wav').play()
#           time.sleep(1)
                   
#           DISPLAYSURF.fill(RED)
#           DISPLAYSURF.blit(game_over, (30,250))
          
#           pygame.display.update()
#           for entity in all_sprites:
#                 entity.kill() 
#           time.sleep(2)
#           pygame.quit()
#           sys.exit()        
    
#     coin.draw(DISPLAYSURF)
#     pygame.display.update()
#     FramePerSec.tick(FPS)
    
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_d]:
                self.rect.move_ip(5, 0)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 5)
        if self.rect.top > 0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -5)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (self.radius, self.radius), self.radius)
        
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
         self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
         
    def move(self):
        pass     

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}  Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollide(P1, coins, False):
        COIN_SCORE += 1
        C1.spawn() 

    if pygame.sprite.spritecollideany(P1, enemies):
        
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill() 
            
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    pygame.display.update()
    FramePerSec.tick(FPS)
   