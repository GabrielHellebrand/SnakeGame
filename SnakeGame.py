import pygame
import random

def main():
    # Initialize the game
    pygame.init()

    # Set up the game window
    width, height = 640, 480
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    # Define colors
    black = pygame.Color(0, 0, 0)
    green = pygame.Color(0, 255, 0)
    red = pygame.Color(255, 0, 0)

    # Set up the snake and food
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawned = True

    # Set up initial game variables
    direction = 'RIGHT'
    change_to = direction
    score = 0

    # Set up game clock
    clock = pygame.time.Clock()

    # Function to display the score
    def display_score():
        font = pygame.font.Font('freesansbold.ttf', 24)
        score_surface = font.render(f'Score: {score}', True, black)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (width // 2, 10)
        window.blit(score_surface, score_rect)

    # Function to handle game over
    def game_over():
        font = pygame.font.Font('freesansbold.ttf', 48)
        game_over_surface = font.render('Game Over!', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (width // 2, height // 4)
        window.fill(black)
        window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Validate the direction change
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        elif change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Update snake position
        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body mechanics
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_spawned = False
        else:
            snake_body.pop()

        # Respawn food
        if not food_spawned:
            food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawned = True

        # Game over conditions
        if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
            game_over()
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Drawing the snake and food
        window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

        # Display the score
        display_score()

        # Update the display and control game speed
        pygame.display.flip()
        clock.tick(20)

main()