# Import a library of functions called 'pygame'
import pygame
import random
# Initialize the game engine
pygame.init()
size = (1140, 810)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("<--- Python")

def main(): 

    jumpscare = False
    fnafbear = pygame.image.load('Pictures\puppet.jpg')
    

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
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    #start the line somewhere on the grid

    randRow = random.randint(0,11)
    randCol = random.randint(0,9)
    print(getXYGrid(randRow,randCol))
    Piece = GamePiece(randRow, randCol, getXYGrid(randRow, randCol), "Guts")
    infoSelect = False
    moveSelect = False
    #moveable = False
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
            elif event.type == pygame.KEYDOWN:
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
                elif event.key == pygame.K_SPACE:
                    infoSelect = not infoSelect
                elif event.key == pygame.K_e:
                    # !! WEIRD CODE !!
                    if moveSelect:
                        gridX, gridY = moveSelected(grid, gridX, gridY, moveSelect)
                        charXPos,charYPos = getXYGrid(gridX,gridY)
                    if checkMobility(grid, gridX, gridY):
                        moveSelect = not moveSelect
                elif event.key == pygame.K_h:
                    jumpscare = not jumpscare
                   
        # Clear the screen and set the screen background
        screen.fill(GREEN)

        drawDaHexies(screen, grid, infoSelect, moveSelect, BLUE, YELLOW, RED)
        drawChar(screen, Piece.x, Piece.y)

        infoSelectCurrent(grid, gridX, gridY, infoSelect, WHITE)
        if jumpscare:
            screen.blit(fnafbear, (0, 0))
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)
    pygame.quit()
#  #end of main lol

def drawDaHexies(screen, grid, infoSelect, moveSelect, BLUE, YELLOW, RED):
# Draws centred portion of hexagonal grid
    for x_pos in range(12):
        for y_pos in range(10):
            color = (0,0,0)
            thickness = 1
            #offset hexagons
            if y_pos % 2 == 1 and grid[x_pos][y_pos] == 1:
                color = BLUE
                thickness = 3
                if moveSelect:
                    color = RED
                elif infoSelect:
                    color = YELLOW
                pygame.draw.polygon(screen, color, [[94.3 + x_pos * 90, 100 + y_pos * 77], [51 + x_pos * 90, 75 + y_pos * 77], [51 + x_pos * 90, 25 + y_pos * 77], [94.3 + x_pos * 90, 0 + y_pos * 77], [137.6 + x_pos * 90, 25 + y_pos * 77], [137.6 + x_pos * 90, 75 + y_pos * 77]], thickness)
            elif y_pos % 2 == 1:
                color = (0,0,0)
                thickness = 1
                pygame.draw.polygon(screen, color, [[94.3 + x_pos * 90, 100 + y_pos * 77], [51 + x_pos * 90, 75 + y_pos * 77], [51 + x_pos * 90, 25 + y_pos * 77], [94.3 + x_pos * 90, 0 + y_pos * 77], [137.6 + x_pos * 90, 25 + y_pos * 77], [137.6 + x_pos * 90, 75 + y_pos * 77]], thickness)
            #Regular Hexagons    
            if y_pos % 2 == 0 and grid[x_pos][y_pos] == 1:
                color = BLUE
                thickness = 3
                if moveSelect:
                    color = RED
                elif infoSelect:
                    color = YELLOW
                pygame.draw.polygon(screen, color, [[50 + x_pos * 90, 100 + y_pos * 77], [6.7 + x_pos * 90, 75 + y_pos * 77], [6.7 + x_pos * 90, 25 + y_pos * 77], [50 + x_pos * 90, 0 + y_pos * 77], [93.3 + x_pos * 90, 25 + y_pos * 77], [93.3 + x_pos * 90, 75 + y_pos * 77]], thickness)
            elif y_pos % 2 == 0:
                color = (0,0,0)
                thickness = 1
                pygame.draw.polygon(screen, color, [[50 + x_pos * 90, 100 + y_pos * 77], [6.7 + x_pos * 90, 75 + y_pos * 77], [6.7 + x_pos * 90, 25 + y_pos * 77], [50 + x_pos * 90, 0 + y_pos * 77], [93.3 + x_pos * 90, 25 + y_pos * 77], [93.3 + x_pos * 90, 75 + y_pos * 77]], thickness)


def drawPieces(screen, charXPos, charYPos):
    pygame.draw.line(screen, (0,0,0), [charXPos, charYPos], [charXPos + 86, charYPos],2)
    
def getXYGrid (row, column):
    #makes the point in the upper left corner of the hexagon
    if column % 2 == 0:
        row = row * 90 + 7
        column = column * 77 + 25
    elif column % 2 == 1:
        row = row * 90 + 52
        column = column * 77 + 25
    return(row,column)
        
def infoSelectCurrent (grid, gridX, gridY, infoSelect, WHITE):
    if infoSelect:
        for row in range(12):
            for column in range(10):
                if grid[row][column] == 1 and gridX == row and gridY == column:                    
                    pygame.draw.rect(screen, (0,0,0), [800, 0, 340, 600])
                    font = pygame.font.SysFont('Times', 16, True, False)
                    text = font.render("Connection terminated. I'm sorry to interrupt",True,WHITE,)
                    screen.blit(text, [810, 10])

# !! WEIRD CODE WILL NEED MAINTINANCE  !!
def checkMobility (grid, gridX, gridY):
    for row in range(12):
        for column in range(10):
            if grid[row][column] == 1 and gridX == row and gridY == column:
                return True 
# !! WEIRD CODE !!
def moveSelected (grid, gridX, gridY, moveSelect):
    if moveSelect == True: #and other conditions
        for row in range(12):
            for column in range(10):
                if grid[row][column] == 1:
                    gridX = row
                    gridY = column
                    print(gridX, gridY)
                    return gridX, gridY

class GamePiece:
    def __init__(self, rownum, colnum, xpos, ypos, name):
        self.row = rownum
        self.col = colnum
        self.x = xpos
        self.y = ypos
        self.name = name




main()


# hexSize = 1
# hexNum = 12


# font = pygame.font.SysFont('Times', 16, True, False)
# text = font.render("Connection terminated. I'm sorry to interrupt",True,WHITE,)
# screen.blit(text, [810, 10])
# text = font.render("you, Elizabeth. If you still even remember that", True, WHITE)
# screen.blit(text, [810, 25])
# text = font.render("name. But I'm afraid you've been misinformed.", True, WHITE)
# screen.blit(text, [810, 40])
# text = font.render("You are not here to receive a gift. Nor, have you", True, WHITE)
# screen.blit(text, [810, 55])
# text = font.render("been called here by the individual you assume.", True, WHITE)
# screen.blit(text, [810, 70])
# text = font.render("Although, you have indeed been called. You", True, WHITE)
# screen.blit(text, [810, 85])
# text = font.render("have all been called here. Into a labyrinth of", True, WHITE)
# screen.blit(text, [810, 100])
# text = font.render("sounds and smells, misdirection and misfortune.", True, WHITE)
# screen.blit(text, [810, 115])
