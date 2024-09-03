import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Power")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
speed = 10

# Speed boost
speed_boost = 1
max_boost = 100

# Mini-map
map_width, map_height = 200, 150
mini_map = pygame.Rect(WIDTH - map_width - 10, HEIGHT - map_height - 10, map_width, map_height)

# Joystick position
joystick_pos = [50, HEIGHT - 100]

# Game variables
score = 0
game_over = False

# Font
font = pygame.font.SysFont('Arial', 25)

# Clock
clock = pygame.time.Clock()

# Leaderboard
leaderboard = []

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def show_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

def game_over_message():
    over_text = font.render('Game Over!', True, RED)
    screen.blit(over_text, [WIDTH // 2 - 50, HEIGHT // 2 - 10])
    pygame.display.flip()
    pygame.time.sleep(2)

def update_leaderboard(score):
    leaderboard.append(score)
    leaderboard.sort(reverse=True)

def draw_leaderboard():
    y_offset = 50
    for index, score in enumerate(leaderboard[:5]):
        text = font.render(f'{index + 1}. {score}', True, BLACK)
        screen.blit(text, [WIDTH - 200, y_offset])
        y_offset += 30

def main():
    global snake_pos, snake_body, snake_direction, change_to, speed_boost, score, game_over

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake_direction != 'DOWN':
                        change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    if snake_direction != 'UP':
                        change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    if snake_direction != 'RIGHT':
                        change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    if snake_direction != 'LEFT':
                        change_to = 'RIGHT'

                if event.key == pygame.K_SPACE:
                    if speed_boost > 0:
                        speed_boost -= 10
                        speed = 20
                    else:
                        speed = 10

        # If game is over, restart on key press
        if game_over:
            game_over_message()
            update_leaderboard(score)
            main()

        # Update direction
        if change_to == 'UP':
            snake_direction = 'UP'
        if change_to == 'DOWN':
            snake_direction = 'DOWN'
        if change_to == 'LEFT':
            snake_direction = 'LEFT'
        if change_to == 'RIGHT':
            snake_direction = 'RIGHT'

        # Move snake
        if snake_direction == 'UP':
            snake_pos[1] -= 10
        if snake_direction == 'DOWN':
            snake_pos[1] += 10
        if snake_direction == 'LEFT':
            snake_pos[0] -= 10
        if snake_direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()

        # Check if snake hits the borders (outskirts)
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
            game_over = True

        screen.fill(WHITE)

        # Draw mini-map outskirts
        pygame.draw.rect(screen, RED, mini_map, 2)

        # Draw snake and leaderboard
        draw_snake(snake_body)
        show_score()
        draw_leaderboard()

        pygame.display.update()
        clock.tick(speed)

if __name__ == "__main__":
    main()
