# import pygame
# import os
# pygame.init()
# pygame.mixer.init()

# base_dir = os.path.dirname(__file__)
# image_dir = os.path.join(base_dir,"imaages")
# music_dir = os.path.join(base_dir,"music")
# screen = pygame.display.set_mode((800, 640))

# image = pygame.image.load(os.path.join(image_dir,"just-a-steve-head.jpeg"))

# playlist = []
# for file in os.listdir(music_dir):
#         if file.lower().endswith(('.mp3','.wav')):
#                 playlist.append(os.path.join(music_dir,file))       
#         if not playlist:
#                 print("theres no music")
#                 playlist = []         

# x = 100
# y = 100
# done = False
# clock = pygame.time.Clock()

# current_track = 0
# if playlist:
#         pygame.mixer.music.load(playlist[current_track])
#         pygame.mixer.music.play()
#         pygame.mixer.music.set_endevent(pygame.USEREVENT)
#         current_track += 1

# while not done:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                         done = True
                        
#         if event.type == pygame.USEREVENT and playlist:
#                 if current_track < len(playlist):
#                         pygame.mixer.music.queue(playlist[current_track])
#                         current_track += 1
#                 else:
#                         current_track = 0
#                         pygame.mixer.music.queue(playlist[current_track])
#                         current_track += 1        
                                
#         pressed = pygame.key.get_pressed()
#         if pressed[pygame.K_UP]: y -= 5
#         if pressed[pygame.K_DOWN]: y += 5
#         if pressed[pygame.K_LEFT]: x -= 5
#         if pressed[pygame.K_RIGHT]: x += 5
        
#         screen.fill((255, 255, 255))
#         screen.blit(image,(x,y))  
        
#         pygame.display.flip()
#         clock.tick(60)   
                                    
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 640))

# done = False
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

    
#     screen.fill((255,255,255))    
    
# #     points = [
# #         (400, 100),
# #         (500, 250),   
# #         (450, 400),   
# #         (350, 400),   
# #         (300, 250)    
# #     ]
            
# #     pygame.draw.polygon(screen,(0,0,0),points)    
#     pygame.draw.line(screen,(0,0,0), (100, 100), (100, 200), width=4)  
#     pygame.draw.line(screen,(0,0,0), (100, 200), (200, 200), width=4)
#     pygame.draw.line(screen,(0,0,0), (200, 200), (200, 100), width=4)
#     pygame.draw.line(screen,(0,0,0), (100, 100), (200, 100), width=4)
#     pygame.draw.line(screen,(0,0,0), (150, 150), (250, 150), width=4)
#     pygame.draw.line(screen,(0,0,0), (150, 150), (150, 50), width=4)
#     pygame.draw.line(screen,(0,0,0), (150, 50), (250, 50), width=4)
#     pygame.draw.line(screen,(0,0,0), (250, 50), (250, 150), width=4)
#     pygame.draw.line(screen,(0,0,0), (150, 50), (100, 100), width=4)
#     pygame.draw.line(screen,(0,0,0), (250, 50), (200, 100), width=4)
#     pygame.draw.line(screen,(0,0,0), (150, 150), (100, 200), width=4)
#     pygame.draw.line(screen,(0,0,0), (250, 150), (200, 200), width=4)
        
        
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# import pygame
# import math
# import time

# # Ignore these 3 functions. Scroll down for the relevant code.

# def create_background(width, height):
#         colors = [(255, 255, 255), (212, 212, 212)]
#         background = pygame.Surface((width, height))
#         tile_width = 20
#         y = 0
#         while y < height:
#                 x = 0
#                 while x < width:
#                         row = y // tile_width
#                         col = x // tile_width
#                         pygame.draw.rect(
#                                 background, 
#                                 colors[(row + col) % 2],
#                                 pygame.Rect(x, y, tile_width, tile_width))
#                         x += tile_width
#                 y += tile_width
#         return background

# def is_trying_to_quit(event):
#         pressed_keys = pygame.key.get_pressed()
#         alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
#         x_button = event.type == pygame.QUIT
#         altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
#         escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
#         return x_button or altF4 or escape

# def run_demos(width, height, fps):
#         pygame.init()
#         screen = pygame.display.set_mode((width, height))
#         pygame.display.set_caption('press space to see next demo')
#         background = create_background(width, height)
#         clock = pygame.time.Clock()
#         demos = [
#                 do_rectangle_demo,
#                 do_circle_demo,
#                 do_horrible_outlines,
#                 do_nice_outlines,
#                 do_polygon_demo,
#                 do_line_demo
#                 ]
#         the_world_is_a_happy_place = 0
#         while True:
#                 the_world_is_a_happy_place += 1
#                 for event in pygame.event.get():
#                         if is_trying_to_quit(event):
#                                 return
#                         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                                 demos = demos[1:]
#                 screen.blit(background, (0, 0))
#                 if len(demos) == 0:
#                         return
#                 demos[0](screen, the_world_is_a_happy_place)
#                 pygame.display.flip()
#                 clock.tick(fps)

# # Everything above this line is irrelevant to this tutorial.

# def do_rectangle_demo(surface, counter):
#         left = (counter // 2) % surface.get_width()
#         top = (counter // 3) % surface.get_height()
#         width = 30
#         height = 30
#         color = (128, 0, 128) # purple
        
#         # Draw a rectangle
#         pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

# def do_circle_demo(surface, counter):
#         x = surface.get_width() // 2
#         y = surface.get_height() // 2
#         max_radius = min(x, y) * 4 // 5
#         radius = abs(int(math.sin(counter * 3.14159 * 2 / 200) * max_radius)) + 1
#         color = (0, 140, 255) # aquamarine
        
#         # Draw a circle
#         pygame.draw.circle(surface, color, (x, y), radius)

# def do_horrible_outlines(surface, counter):
#         color = (255, 0, 0) # red
        
#         # draw a rectangle
#         pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 100), 10)

#         # draw a circle
#         pygame.draw.circle(surface, color, (300, 60), 50, 10)
        
# def do_nice_outlines(surface, counter):
#         color = (0, 128, 0) # green
        
#         # draw a rectangle
#         pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 10))
#         pygame.draw.rect(surface, color, pygame.Rect(10, 10, 10, 100))
#         pygame.draw.rect(surface, color, pygame.Rect(100, 10, 10, 100))
#         pygame.draw.rect(surface, color, pygame.Rect(10, 100, 100, 10))
        
#         # draw a circle
#         center_x = 300
#         center_y = 60
#         radius = 45
#         iterations = 150
#         for i in range(iterations):
#                 ang = i * 3.14159 * 2 / iterations
#                 dx = int(math.cos(ang) * radius)
#                 dy = int(math.sin(ang) * radius)
#                 x = center_x + dx
#                 y = center_y + dy
#                 pygame.draw.circle(surface, color, (x, y), 5)


# def do_polygon_demo(surface, counter):
#         color = (255, 255, 0) # yellow
        
#         num_points = 8
#         point_list = []
#         center_x = surface.get_width() // 2
#         center_y = surface.get_height() // 2
#         for i in range(num_points * 2):
#                 radius = 100
#                 if i % 2 == 0:
#                         radius = radius // 2
#                 ang = i * 3.14159 / num_points + counter * 3.14159 / 60
#                 x = center_x + int(math.cos(ang) * radius)
#                 y = center_y + int(math.sin(ang) * radius)
#                 point_list.append((x, y))
#         pygame.draw.polygon(surface, color, point_list)

# def rotate_3d_points(points, angle_x, angle_y, angle_z):
#         new_points = []
#         for point in points:
#                 x = point[0]
#                 y = point[1]
#                 z = point[2]
#                 new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
#                 new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
#                 y = new_y
#                 # isn't math fun, kids?
#                 z = new_z
#                 new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
#                 new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
#                 x = new_x
#                 z = new_z
#                 new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
#                 new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
#                 x = new_x
#                 y = new_y
#                 new_points.append([x, y, z])
#         return new_points

# def do_line_demo(surface, counter):
#         color = (0, 0, 0) # black
#         cube_points = [
#                 [-1, -1, 1],
#                 [-1, 1, 1],
#                 [1, 1, 1],
#                 [1, -1, 1],
#                 [-1, -1, -1],
#                 [-1, 1, -1],
#                 [1, 1, -1],
#                 [1, -1, -1]]
                
#         connections = [
#                 (0, 1),
#                 (1, 2),
#                 (2, 3),
#                 (3, 0),
#                 (4, 5),
#                 (5, 6),
#                 (6, 7),
#                 (7, 4),
#                 (0, 4),
#                 (1, 5),
#                 (2, 6),
#                 (3, 7)
#                 ]
                
#         t = counter * 2 * 3.14159 / 60 # this angle is 1 rotation per second
        
#         # rotate about x axis every 2 seconds
#         # rotate about y axis every 4 seconds
#         # rotate about z axis every 6 seconds
#         points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
#         flattened_points = []
#         for point in points:
#                 flattened_points.append(
#                         (point[0] * (1 + 1.0 / (point[2] + 3)),
#                          point[1] * (1 + 1.0 / (point[2] + 3))))
        
#         for con in connections:
#                 p1 = flattened_points[con[0]]
#                 p2 = flattened_points[con[1]]
#                 x1 = p1[0] * 60 + 200
#                 y1 = p1[1] * 60 + 150
#                 x2 = p2[0] * 60 + 200
#                 y2 = p2[1] * 60 + 150
                
#                 # This is the only line that really matters
#                 pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)
                
        
# run_demos(400, 300, 60)

import pygame
import time
import random

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

WIDTH = 600
HEIGHT = 400

pygame.init()
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game: Levels & Score')

clock = pygame.time.Clock()
snake_block = 10
initial_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

def display_info(score, level):
    value = score_font.render(f"Score: {score}  Level: {level}", True, YELLOW)
    dis.blit(value, [10, 10])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0
    level = 1
    speed = initial_speed

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_info(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, RED, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        display_info(score, level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            score += 1
            Length_of_snake += 1

            while True:
                foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
                if [foodx, foody] not in snake_List:
                    break

            if score % 3 == 0:
                level += 1
                speed += 2

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()