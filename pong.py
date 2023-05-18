import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
#if you change this please increase/dreacse pong and paddle speed and size or itll be chaotic
WIDTH = 1920
HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
FPS = 60   #this also effects game speed
BALL_RADIUS = 10  #ball size
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED_X = 9
BALL_SPEED_Y = 9
PADDLE_SPEED = 10

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

def reset_ball():
    return WIDTH // 2, HEIGHT // 2, random.choice([-1, 1]), random.choice([-1, 1])

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def main():
    # Paddle positions
    player_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    opponent_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

    # Ball position and direction
    ball_x, ball_y, ball_dx, ball_dy = reset_ball()

    # Player and opponent scores
    player_score = 0
    opponent_score = 0

    # Load fonts
    font_name = pygame.font.match_font('arial')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle_y > 0:
            player_paddle_y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_paddle_y < HEIGHT - PADDLE_HEIGHT:
            player_paddle_y += PADDLE_SPEED

        # AI opponent movement
        if opponent_paddle_y + PADDLE_HEIGHT // 2 < ball_y:
            opponent_paddle_y += PADDLE_SPEED
        if opponent_paddle_y + PADDLE_HEIGHT // 2 > ball_y:
            opponent_paddle_y -= PADDLE_SPEED

        # Update ball position
        ball_x += ball_dx * BALL_SPEED_X
        ball_y += ball_dy * BALL_SPEED_Y

        # Ball collisions with walls
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
            ball_dy *= -1

        # Ball collisions with paddles
        if ball_x <= PADDLE_WIDTH and player_paddle_y <= ball_y <= player_paddle_y + PADDLE_HEIGHT:
            ball_dx *= -1
        if ball_x >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and opponent_paddle_y <= ball_y <= opponent_paddle_y + PADDLE_HEIGHT:
            ball_dx *= -1

        # Ball out of bounds
        if ball_x < 0:
            opponent_score += 1
            ball_x, ball_y, ball_dx, ball_dy = reset_ball()
        if ball_x > WIDTH - BALL_RADIUS:
            player_score += 1
            ball_x, ball_y, ball_dx, ball_dy = reset_ball()

        # Clear the screen
        window.fill(BLACK)

        # Draw paddles
                # Draw paddles
        pygame.draw.rect(window, WHITE, pygame.Rect(0, player_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(window, WHITE, pygame.Rect(WIDTH - PADDLE_WIDTH, opponent_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

        # Draw the ball
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)

        # Draw scores
        font = pygame.font.Font(font_name, 36)
        draw_text(str(player_score), font, WHITE, WIDTH // 4, 50)
        draw_text(str(opponent_score), font, WHITE, WIDTH - WIDTH // 4, 50)

        # Update the display
        pygame.display.flip()

        # Set the desired FPS
        clock.tick(FPS)

    # Quit the game
    pygame.quit()

# Start the game
if __name__ == '__main__':
    main()

