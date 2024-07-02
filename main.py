import pygame
import random

# Initialize the pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the speed and block size
SNAKE_BLOCK = 10
INITIAL_SPEED = 15

# Create the window
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Initialize the clock
clock = pygame.time.Clock()

# Define the font for displaying the score
font_style = pygame.font.SysFont(None, 35)


def display_score(score):
    value = font_style.render(f"Score: {score}", True, WHITE)
    win.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    obstacles = []
    score = 0
    speed = INITIAL_SPEED

    while not game_over:

        while game_close:
            win.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(score)
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
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        for obstacle in obstacles:
            pygame.draw.rect(win, BLUE, [obstacle[0], obstacle[1], SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1
            score += 1

            if score % 20 == 0 and score <= 100:
                obstacle_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
                obstacle_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
                obstacles.append((obstacle_x, obstacle_y))

            if score > 100:
                speed += 1

        clock.tick(speed)

    pygame.quit()
    quit()


gameLoop()
