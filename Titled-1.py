# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()
# Set the height and width of the screen
size = (1150, 810)
pygame.RESIZABLE
screen = pygame.display.set_mode((size), pygame.RESIZABLE)


pygame.display.set_caption("<--- Python")

def main(): 
    #ancient god list
    #greaterGods = [Hastur, Cthulhu, Nyarlathotep, ]
    #lesserGods = [Hypnos, ]



    # BRogram variables
    #make a 2d array
    grid = []
    for row in range(12):
        grid.append([])
        for column in range(10):
            grid[row].append(0)

    row = 0
    column = 0
    grid[row][column] = 1
    

    # some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    NICEGREEN = (6, 84, 4)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    #Main vrogram loop
    #loop = True
    #while loop:

    # Game logic

    # Loop until the user clicks the close button.
     # Loop as long as done == False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_a:
                    if row > 0:
                        grid[row][column] = 0
                        row-=1
                        grid[row][column] = 1
                elif event.key == pygame.K_d:
                    if row < 11:
                        grid[row][column] = 0
                        row+=1
                        grid[row][column] = 1
                elif event.key == pygame.K_w:
                    if column > 0:
                        grid[row][column] = 0
                        column-=1
                        grid[row][column] = 1
                elif event.key == pygame.K_s:
                    if column < 9:
                        grid[row][column] = 0
                        column+=1
                        grid[row][column] = 1
            
        # Clear the screen and set the screen background
        screen.fill(GREEN)
            
        drawDaHexies(screen, grid, BLACK, BLUE)
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)
    # Be IDLE friendly
    pygame.quit()
#  #end of main lol

#fixed B)
def drawDaHexies(screen, grid, BLACK, BLUE):
# Draws centred portion of hexagonal grid
    for x_pos in range(12):
        for y_pos in range(10):
            color = BLACK
            thickness = 1
            #offset hexagons
            if y_pos % 2 == 1 and grid[x_pos][y_pos] == 1:
                color = BLUE
                thickness = 3
                pygame.draw.polygon(screen, color, [[94.3 + x_pos * 90, 100 + y_pos * 77], [51 + x_pos * 90, 75 + y_pos * 77], [51 + x_pos * 90, 25 + y_pos * 77], [94.3 + x_pos * 90, 0 + y_pos * 77], [137.6 + x_pos * 90, 25 + y_pos * 77], [137.6 + x_pos * 90, 75 + y_pos * 77]], thickness)
            elif y_pos % 2 == 1:
                color = BLACK
                thickness = 1
                pygame.draw.polygon(screen, color, [[94.3 + x_pos * 90, 100 + y_pos * 77], [51 + x_pos * 90, 75 + y_pos * 77], [51 + x_pos * 90, 25 + y_pos * 77], [94.3 + x_pos * 90, 0 + y_pos * 77], [137.6 + x_pos * 90, 25 + y_pos * 77], [137.6 + x_pos * 90, 75 + y_pos * 77]], thickness)
            #Regular Hexagons    
            if y_pos % 2 == 0 and grid[x_pos][y_pos] == 1:
                color = BLUE
                thickness = 3
                pygame.draw.polygon(screen, color, [[50 + x_pos * 90, 100 + y_pos * 77], [6.7 + x_pos * 90, 75 + y_pos * 77], [6.7 + x_pos * 90, 25 + y_pos * 77], [50 + x_pos * 90, 0 + y_pos * 77], [93.3 + x_pos * 90, 25 + y_pos * 77], [93.3 + x_pos * 90, 75 + y_pos * 77]], thickness)
            elif y_pos % 2 == 0:
                color = BLACK
                thickness = 1
                pygame.draw.polygon(screen, color, [[50 + x_pos * 90, 100 + y_pos * 77], [6.7 + x_pos * 90, 75 + y_pos * 77], [6.7 + x_pos * 90, 25 + y_pos * 77], [50 + x_pos * 90, 0 + y_pos * 77], [93.3 + x_pos * 90, 25 + y_pos * 77], [93.3 + x_pos * 90, 75 + y_pos * 77]], thickness)

main()