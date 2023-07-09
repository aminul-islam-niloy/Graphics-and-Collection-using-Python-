import pygame
from pygame.locals import *

# Define the dimensions of the window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Initialize Pygame
pygame.init()

# Create the display surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hidden Surface Elimination")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Define the vertices and colors of the stars
stars = [
    {
        'vertices': [(400, 150), (425, 250), (525, 250), (450, 325), (475, 425), (400, 350), (325, 425), (350, 325), (275, 250), (375, 250)],
        'color': WHITE
    },
    {
        'vertices': [(600, 100), (625, 200), (725, 250), (650, 225), (675, 325), (600, 275), (525, 325), (550, 225), (475, 200), (575, 175)],
        'color': CYAN
    },
    {
        'vertices': [(200, 100), (300, 150), (325, 50), (350, 150), (450, 100), (375, 175), (425, 250), (350, 200), (275, 250), (325, 175)],
        'color': GREEN
    },
    {
        'vertices': [(200, 100), (600, 100), (400, 400), (400, 400)],
        'color': RED
    }
    
]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the stars using the Painter's algorithm
    for star in stars:
        pygame.draw.polygon(screen, star['color'], star['vertices'])

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
