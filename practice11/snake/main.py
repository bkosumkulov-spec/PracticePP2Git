import pygame
import random
import time
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
ORANGE = (255, 165, 0)
PURPLE = (180, 0, 255)
 
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
 
# Food types: (color, points, lifetime_seconds)
# None lifetime = food stays forever
FOOD_TYPES = [
    {"color": RED,    "points": 1,  "lifetime": None},   # normal food
    {"color": ORANGE, "points": 3,  "lifetime": 5.0},    # rare food, disappears in 5s
    {"color": PURPLE, "points": 5,  "lifetime": 3.0},    # epic food, disappears in 3s
]
 
# Spawn weights — normal food is most common
FOOD_WEIGHTS = [70, 20, 10]
 
 
def spawn_food(snake_list):
    food_type = random.choices(FOOD_TYPES, weights=FOOD_WEIGHTS, k=1)[0]
    while True:
        fx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        fy = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
        if [fx, fy] not in snake_list:
            break
    return {
        "x": fx,
        "y": fy,
        "color": food_type["color"],
        "points": food_type["points"],
        "lifetime": food_type["lifetime"],
        "spawned_at": time.time(),
    }
 
 
def draw_food(food):
    pygame.draw.rect(dis, food["color"], [food["x"], food["y"], snake_block, snake_block])
 
    # Draw countdown bar for timed food
    if food["lifetime"] is not None:
        elapsed = time.time() - food["spawned_at"]
        remaining = max(0, food["lifetime"] - elapsed)
        ratio = remaining / food["lifetime"]
        bar_width = int(snake_block * ratio)
        pygame.draw.rect(dis, YELLOW, [food["x"], food["y"] - 4, bar_width, 3])
 
 
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
 
    # List of active food items on the field
    foods = [spawn_food(snake_List)]
 
    # Timer to spawn additional food occasionally
    last_extra_spawn = time.time()
    extra_spawn_interval = 6.0   # spawn a bonus food every 6 seconds
 
    while not game_over:
 
        while game_close:
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
                        return
 
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
 
        # Remove expired timed foods
        now = time.time()
        foods = [
            f for f in foods
            if f["lifetime"] is None or (now - f["spawned_at"]) < f["lifetime"]
        ]
 
        # Always keep at least one food on the field
        if not foods:
            foods.append(spawn_food(snake_List))
 
        # Periodically spawn an extra bonus food (max 3 foods at once)
        if now - last_extra_spawn >= extra_spawn_interval and len(foods) < 3:
            foods.append(spawn_food(snake_List))
            last_extra_spawn = now
 
        # Draw all food items
        for food in foods:
            draw_food(food)
 
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
 
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        draw_snake(snake_block, snake_List)
        display_info(score, level)
        pygame.display.update()
 
        # Check if snake ate any food
        eaten = None
        for food in foods:
            if x1 == food["x"] and y1 == food["y"]:
                eaten = food
                break
 
        if eaten:
            score += eaten["points"]
            Length_of_snake += eaten["points"]
            foods.remove(eaten)
            foods.append(spawn_food(snake_List))
 
            if score % 5 == 0:
                level += 1
                speed += 2
 
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()