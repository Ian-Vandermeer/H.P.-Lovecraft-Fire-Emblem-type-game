import pygame
import random
# Initialize the game engine
pygame.init()
size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("<--- Python")

def main(): 

 # BRogram variables
    jumpscare = False
    fnafbear = pygame.image.load('Pictures\puppet.jpg')

    hexRowNum = 13
    hexColNum = 10

    #make a 2d array
    grid = []
    for row in range(hexRowNum):
        grid.append([])
        for column in range(hexColNum):
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
    infoSelect = False
    moveSelect = False

    #Create the pieces
    piece_stuff = [["Bingus", 'Pictures\Manlet.png'], ["AllahCat", 'Pictures\Pixel_char.png']]
    #bingus = GamePiece(random.randint(0,2), random.randint(0,9), "Bingus", pygame.image.load('Pictures\cthulhu.jpg'), hexRowNum, hexColNum)
    #allahCat = GamePiece(random.randint(7,9), random.randint(0,9), "AllahCat", pygame.image.load('Pictures\Allahcat.jpg'), hexRowNum, hexColNum)
    player1PieceList = []
    player2PieceList = []
    for i in range(7):
        player1PieceList.append(GamePiece(random.randint(0,2), random.randint(0,9), piece_stuff[i%2][0], pygame.image.load(piece_stuff[i%2][1]), hexRowNum, hexColNum))
        player2PieceList.append(GamePiece(random.randint(6,9), random.randint(0,9), piece_stuff[i%2][0], pygame.image.load(piece_stuff[i%2][1]), hexRowNum, hexColNum))
    #player1PieceList.append(bingus)
    #player1PieceList.append(allahCat)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

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
                    if row < hexRowNum - 1:
                        grid[row][column] = 0
                        row+=1
                        grid[row][column] = 1
                elif event.key == pygame.K_w:
                    if column > 0:
                        grid[row][column] = 0
                        column-=1
                        grid[row][column] = 1
                elif event.key == pygame.K_s:
                    if column < hexColNum - 1:
                        grid[row][column] = 0
                        column+=1
                        grid[row][column] = 1
                elif event.key == pygame.K_SPACE:
                    infoSelect = not infoSelect
                elif event.key == pygame.K_e:
                    if not moveSelect:
                        piece_val = checkMobility(grid, row, column, player2PieceList)
                        if piece_val > -1:
                            moveSelect = not moveSelect
                    else:
                        player2PieceList[piece_val].change_pos(row, column)
                        moveSelect = not moveSelect
                elif event.key == pygame.K_p:
                    pass # this later should end the players turn
                elif event.key == pygame.K_h:
                    jumpscare = not jumpscare
                   
        # Clear the screen and set the screen background
        screen.fill(GREEN)

        drawDaHexies(screen, grid, infoSelect, moveSelect, hexRowNum, hexColNum)

        # loops through the active piece list and passes the contents into the draw function
        for i in range(len(player2PieceList)):
            drawPieces(screen, player1PieceList[i])
            drawPieces(screen, player2PieceList[i])

        #infoSelectCurrent(grid, row, column, bingus, infoSelect)
        
        if jumpscare:
            screen.blit(fnafbear, (0, 0))

        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)
    pygame.quit()
#  #end of main lol

def drawDaHexies(screen, grid, infoSelect, moveSelect, hexRowNum, hexColNum):
    # Draws centred portion of hexagonal grid
    for x_pos in range(hexRowNum):
        for y_pos in range(hexColNum):
            color = (0,0,0)
            thickness = 1
            #offset hexagons
            if y_pos % 2 == 1 and grid[x_pos][y_pos] == 1:
                color = (0, 0, 255)
                thickness = 3
                if moveSelect:
                    color = (255, 0, 0)
                elif infoSelect:
                    color = (255, 255, 0)
                pygame.draw.polygon(screen, color, [[(79.8) + x_pos * 80, (88.8) + y_pos * 68.4], [(41.3) + x_pos * 80, (66.6) + y_pos * 68.4], [(41.3) + x_pos * 80, (22.2) + y_pos * 68.4], [(79.8) + x_pos * 80, 0 + y_pos * 68.4], [(118.3) + x_pos * 80, (22.2) + y_pos * 68.4], [(118.3) + x_pos * 80, (66.6) + y_pos * 68.4]], thickness)
            elif y_pos % 2 == 1:
                color = (0,0,0)
                thickness = 1
                pygame.draw.polygon(screen, color, [[(79.8) + x_pos * 80, (88.8) + y_pos * 68.4], [(41.3) + x_pos * 80, (66.6) + y_pos * 68.4], [(41.3) + x_pos * 80, (22.2) + y_pos * 68.4], [(79.8) + x_pos * 80, 0 + y_pos * 68.4], [(118.3) + x_pos * 80, (22.2) + y_pos * 68.4], [(118.3) + x_pos * 80, (66.6) + y_pos * 68.4]], thickness)
            #Regular Hexagons    
            if y_pos % 2 == 0 and grid[x_pos][y_pos] == 1:
                color = (0, 0, 255)
                thickness = 3
                if moveSelect:
                    color = (255, 0, 0)
                elif infoSelect:
                    color = (255, 255, 0)
                pygame.draw.polygon(screen, color, [[(40.4) + x_pos * 80, (88.8) + y_pos * 68.4], [(1.95) + x_pos * 80, (66.6) + y_pos * 68.4], [(1.95) + x_pos * 80, (22.2) + y_pos * 68.4], [(40.4) + x_pos * 80, 0 + y_pos * 68.4], [(78.9) + x_pos * 80, (22.2) + y_pos * 68.4], [(78.9) + x_pos * 80, (66.6) + y_pos * 68.4]], thickness)
            elif y_pos % 2 == 0:
                color = (0,0,0)
                thickness = 1
                pygame.draw.polygon(screen, color, [[(40.4) + x_pos * 80, (88.8) + y_pos * 68.4], [(1.95) + x_pos * 80, (66.6) + y_pos * 68.4], [(1.95) + x_pos * 80, (22.2) + y_pos * 68.4], [(40.4) + x_pos * 80, 0 + y_pos * 68.4], [(78.9) + x_pos * 80, (22.2) + y_pos * 68.4], [(78.9) + x_pos * 80, (66.6) + y_pos * 68.4]], thickness)

def drawPieces(screen, aPiece):
    #makes the point in the upper left corner of the hexagon
    if aPiece.col % 2 == 0:
        screen.blit(aPiece.IMG, ([aPiece.row * 80 + 7, aPiece.col * 68.4 + (22.2)]))
    elif aPiece.col % 2 == 1:
        screen.blit(aPiece.IMG, ([aPiece.row * 80 + 52, aPiece.col * 68.4 + (22.2)]))
      
def infoSelectCurrent (grid, row, column, aPiece, infoSelect):
    if infoSelect:
        if grid[row][column] == 1 and aPiece.row == row and aPiece.col == column:                    
            pygame.draw.rect(screen, (0,0,0), [800, 0, 340, 600])
            font = pygame.font.SysFont('Times', 16, True, False)
            text = font.render("Connection terminated. I'm sorry to interrupt",True, (255, 255, 255),)
            screen.blit(text, [810, 10])
                    
def checkMobility (grid, row, column, activePiecelist):
    for i in range(len(activePiecelist)):
        if grid[row][column] == 1 and activePiecelist[i].row == row and activePiecelist[i].col == column:
            return i
    return -1

class GamePiece:
    def __init__(self, row, col, name, IMG, hexRowNum, hexColNum):
        self.row = row
        self.col = col
        self.name = name
        self.IMG = IMG
        self.can_move = True
        self.row_max = hexRowNum
        self.col_max = hexColNum
    def change_pos(self, new_row, new_col):
        if new_row <= (self.row_max) and new_row >= 0 and new_col <= (self.col_max) and new_col >= 0:
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid Instance")
    def moved(self):
        self.can_move = False
    def new_turn(self):
        self.can_move = True
    def check_row(self):
        return self.row
    def check_col(self):
        return self.col

main()


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
