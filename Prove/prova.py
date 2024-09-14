import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sine Wave Animation")

# Create a surface (a blue circle for this example)
surface_radius = 20
surface = pygame.Surface((surface_radius * 2, surface_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, BLUE, (surface_radius, surface_radius), surface_radius)

# Main loop variables
clock = pygame.time.Clock()
angle = 0  # Angle for the sine function

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the new y position using the sine function
    y_position = SCREEN_HEIGHT // 2 + int(100 * math.sin(math.radians(angle)))

    # Increment the angle to animate the movement
    angle += 2
    if angle >= 360:
        angle -= 360

    # Clear the screen
    screen.fill(WHITE)

    # Draw the surface at the new position
    screen.blit(surface, (SCREEN_WIDTH // 2 - surface_radius, y_position - surface_radius))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
