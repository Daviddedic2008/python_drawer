import pygame
import sys
import random

# Function to generate random float color components
def generate_random_color():
    r = random.uniform(0.0, 1.0)
    g = random.uniform(0.0, 1.0)
    b = random.uniform(0.0, 1.0)
    return f"{r:.6f}, {g:.6f}, {b:.6f}"

# Number of colors to generate (512 * 512)
num_colors = 512 * 512

def read_colors(filename):
    colors = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Parse each line and convert string values to floats
            r, g, b = map(float, line.strip().split(','))
            # Convert float values (0.0-1.0) to integer RGB values (0-255)
            colors.append((int(r * 255), int(g * 255), int(b * 255)))
    return colors

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 512, 512

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Pixels from Array")

# Read colors from file
colors = read_colors('C:\\Users\\david\\OneDrive\\Documents\\pythonColorRet.txt.txt')

# Assuming we have one color per pixel for a width*height screen
if len(colors) != width * height:
    print(f"Error: Expected {width * height} colors, but found {len(colors)}")
    sys.exit(1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw each pixel
    for y in range(height):
        for x in range(width):
            color = colors[y * width + x]
            screen.set_at((x, y), color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
