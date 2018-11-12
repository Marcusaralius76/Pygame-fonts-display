import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the height and width of the screen
size = (500, 200)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('sghdgfh')

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

all_fonts = pygame.font.get_fonts()
i = 0

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    i = i + 1
    
    if i >= len(all_fonts):
        i = 0

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    screen.fill(WHITE)
    
    font = pygame.font.SysFont(all_fonts[i], 24, False, False)
    text = font.render(all_fonts[i], True, BLACK)
    
    text2 = font.render(str(i), True, BLACK)

    screen.blit(text, [100, 100])
    screen.blit(text2, [100, 70])

    pygame.display.flip()


    clock.tick(1)


pygame.quit()