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
    hexColNum = 9

    #make a 2d array
    grid = []
    for row in range(hexRowNum):
        grid.append([])
        for column in range(hexColNum):
            grid[row].append(0)

    row = 0
    column = 0
    grid[row][column] = 1

    moveSelect = False
    attackSelect = False
    player1Turn = False

    #Create the pieces     Move Range| HP | Damage | Attack Range | Action Total
    piece_stuff = [["Bingus", 'Pictures\Manlet.png', 1, 8, 3, 1, 2], ["AllahCat", 'Pictures\Pixel_char.png', 2, 5, 3, 1, 1], ["Doggie", 'Pictures\Doggie.png', 3, 3, 2, 1, 2]]
   
    player1PieceList = []
    player2PieceList = []
    for i in range(3):
        player1PieceList.append(GamePiece(random.randint(0,2), random.randint(0,8), piece_stuff[i%3][0], pygame.image.load(piece_stuff[i%3][1]), piece_stuff[i%3][2], piece_stuff[i%3][3], piece_stuff[i%3][4], piece_stuff[i%3][5], piece_stuff[i%3][6], hexRowNum, hexColNum))
        player2PieceList.append(GamePiece(random.randint(6,9), random.randint(0,8), piece_stuff[i%3][0], pygame.image.load(piece_stuff[i%3][1]), piece_stuff[i%3][2], piece_stuff[i%3][3], piece_stuff[i%3][4], piece_stuff[i%3][5], piece_stuff[i%3][6], hexRowNum, hexColNum))
    
        #print(player1PieceList[1])
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
                elif event.key == pygame.K_e:
                    #Player two ifs ands and buts :)
                    if not player1Turn:
                        if not moveSelect and not attackSelect:
                            piece_val = checkMobility(grid, row, column, player2PieceList)
                            if piece_val > -1:
                                moveSelect = not moveSelect
                        elif not attackSelect:
                            if checkValidMovement(row, column, player2PieceList[piece_val], player1PieceList):
                                player2PieceList[piece_val].change_pos(row, column)
                                moveSelect = not moveSelect
                                player2PieceList[piece_val].change_action_count(1)
                            else:
                                moveSelect = not moveSelect
                    #Player one ifs ands and buts :)
                    elif player1Turn:
                        if not moveSelect and not attackSelect:
                            piece_val = checkMobility(grid, row, column, player1PieceList)
                            if piece_val > -1:
                                moveSelect = not moveSelect
                        elif not attackSelect:
                            if checkValidMovement(row, column, player1PieceList[piece_val], player2PieceList):
                                player1PieceList[piece_val].change_pos(row, column)
                                moveSelect = not moveSelect
                                player1PieceList[piece_val].change_action_count(1)
                            else:
                                moveSelect = not moveSelect
                elif event.key == pygame.K_r:
                    if not player1Turn:
                        if not attackSelect and not moveSelect:
                            piece_val = checkMobility(grid, row, column, player2PieceList)
                            if piece_val > -1:
                                attackSelect = not attackSelect
                        elif not moveSelect:
                            target_piece = checkValidAttack(row, column, player2PieceList[piece_val], player1PieceList)
                            if target_piece > -1:
                                player1PieceList[target_piece].change_health(player2PieceList[piece_val].damage)
                                print ("yeowch")
                                attackSelect = not attackSelect
                                player2PieceList[piece_val].change_action_count(1)
                            elif target_piece < 0:
                                attackSelect = not attackSelect
                    elif player1Turn:
                        if not attackSelect and not moveSelect:
                            piece_val = checkMobility(grid, row, column, player1PieceList)
                            if piece_val > -1:
                                attackSelect = not attackSelect
                        elif not moveSelect:
                            target_piece = checkValidAttack(row, column, player1PieceList[piece_val], player2PieceList)
                            if target_piece > -1:
                                player2PieceList[target_piece].change_health(player1PieceList[piece_val].damage)
                                print ("yeowch")
                                attackSelect = not attackSelect
                                player1PieceList[piece_val].change_action_count(1)
                            elif target_piece < 0:
                                attackSelect = not attackSelect           
                elif event.key == pygame.K_p:
                    moveSelect = False
                    attackSelect = False
                    if player1Turn:
                        for i in range(len(player1PieceList)):
                            player1PieceList[i].change_action_count(-player1PieceList[i].check_action_total())
                    elif not player1Turn:
                        for i in range(len(player2PieceList)):
                            player2PieceList[i].change_action_count(-player1PieceList[i].check_action_total())
                    #changes the turn
                    player1Turn = not player1Turn
                elif event.key == pygame.K_h:
                    jumpscare = not jumpscare
                   
        # Clear the screen and set the screen background
        screen.fill((52, 204, 235))

        drawDaHexies(screen, grid, moveSelect, hexRowNum, hexColNum)
        if moveSelect or attackSelect:
            if player1Turn:
                drawMovableHex(screen, player1PieceList[piece_val], hexColNum, hexRowNum, moveSelect, attackSelect)
            elif not player1Turn:
                drawMovableHex(screen, player2PieceList[piece_val], hexColNum, hexRowNum, moveSelect, attackSelect)

        # loops through the active piece list and passes the contents into the draw function
        for i in range(len(player2PieceList)):
            drawPieces(screen, player1PieceList[i])
            drawPieces(screen, player2PieceList[i])
        # Displays info about the piece on the cursor
        for i in range (len(player1PieceList)):
            infoDisplayCurrent(grid, row, column, player1PieceList[i], player1Turn)
        for i in range (len(player2PieceList)):
            infoDisplayCurrent(grid, row, column, player2PieceList[i], player1Turn)
        
        if jumpscare:
            screen.blit(fnafbear, (0, 0))

        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)
    pygame.quit()
#  #end of main lol

def drawDaHexies(screen, grid, moveSelect, hexRowNum, hexColNum):
    # Draws centred portion of hexagonal grid
    for x_pos in range(hexRowNum):
        for y_pos in range(hexColNum):
            #offset hexagons
            if y_pos % 2 == 1 and grid[x_pos][y_pos] == 1:
                color = (0, 0, 255)
                thickness = 3
                if moveSelect:
                    thickness = 4
                    color = (255, 0, 0)
                pygame.draw.polygon(screen, color, [[(79.8) + x_pos * 80, (168.8) + y_pos * 68.4], [(41.3) + x_pos * 80, (146.6) + y_pos * 68.4], [(41.3) + x_pos * 80, (102.2) + y_pos * 68.4], [(79.8) + x_pos * 80, 80 + y_pos * 68.4], [(118.3) + x_pos * 80, (102.2) + y_pos * 68.4], [(118.3) + x_pos * 80, (146.6) + y_pos * 68.4]], thickness)
            elif y_pos % 2 == 1:
                color = (0,0,0)
                thickness = 1

                # font = pygame.font.SysFont('Times', 16, True, False)
                # text = font.render(str(x_pos) + ", " + str(y_pos),True, (0, 0, 0))
                # screen.blit(text, [x_pos * 80 + 52, y_pos * 68.4 + (100)])

                pygame.draw.polygon(screen, color, [[(79.8) + x_pos * 80, (168.8) + y_pos * 68.4], [(41.3) + x_pos * 80, (146.6) + y_pos * 68.4], [(41.3) + x_pos * 80, (102.2) + y_pos * 68.4], [(79.8) + x_pos * 80, 80 + y_pos * 68.4], [(118.3) + x_pos * 80, (102.2) + y_pos * 68.4], [(118.3) + x_pos * 80, (146.6) + y_pos * 68.4]], thickness)
            #Regular Hexagons    
            if y_pos % 2 == 0 and grid[x_pos][y_pos] == 1:
                color = (0, 0, 255)
                thickness = 3
                if moveSelect:
                    thickness = 4
                    color = (255, 0, 0)
                pygame.draw.polygon(screen, color, [[(40.4) + x_pos * 80, (168.8) + y_pos * 68.4], [(1.95) + x_pos * 80, (146.6) + y_pos * 68.4], [(1.95) + x_pos * 80, (102.2) + y_pos * 68.4], [(40.4) + x_pos * 80, 80 + y_pos * 68.4], [(78.9) + x_pos * 80, (102.2) + y_pos * 68.4], [(78.9) + x_pos * 80, (146.6) + y_pos * 68.4]], thickness)
            elif y_pos % 2 == 0:
                color = (0,0,0)
                thickness = 1

                # font = pygame.font.SysFont('Times', 16, True, False)
                # text = font.render(str(x_pos) + ", " + str(y_pos),True, (0, 0, 0))
                # screen.blit(text, [x_pos * 80 + 7, y_pos * 68.4 + (100)])

                pygame.draw.polygon(screen, color, [[(40.4) + x_pos * 80, (168.8) + y_pos * 68.4], [(1.95) + x_pos * 80, (146.6) + y_pos * 68.4], [(1.95) + x_pos * 80, (102.2) + y_pos * 68.4], [(40.4) + x_pos * 80, 80 + y_pos * 68.4], [(78.9) + x_pos * 80, (102.2) + y_pos * 68.4], [(78.9) + x_pos * 80, (146.6) + y_pos * 68.4]], thickness)

def drawMovableHex(screen, aPiece, hexColNum, hexRowNum, moveSelect, attackSelect):
    if moveSelect:
        thickness = 2
        color = (163, 250, 255)
        x = aPiece.row
        y = aPiece.col
        z = -aPiece.row-aPiece.col
        for x in range(-aPiece.move ,1 + aPiece.move):
            for y in range(-aPiece.move, 1 + aPiece.move):
                for z in range(-aPiece.move, 1 + aPiece.move):
                    if x + y + z == 0:
                        q = x + (y - (y&1)) / 2
                        if aPiece.col + y >=0 and aPiece.col + y < hexColNum and aPiece.row + q < hexRowNum:
                            if (aPiece.col + y) % 2 == 0:
                                if aPiece.col % 2 == 1:
                                    q += 1
                                pygame.draw.polygon(screen, color, [[(40.4) + (aPiece.row + q) * 80, (168.8) + (aPiece.col + y) * 68.4], [(1.95) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4], [(1.95) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(40.4) + (aPiece.row + q) * 80, 80 + (aPiece.col + y) * 68.4], [(78.9) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(78.9) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4]], thickness)
                            elif (aPiece.col + y) % 2 == 1:
                                pygame.draw.polygon(screen, color, [[(79.8) + (aPiece.row + q) * 80, (168.8) + (aPiece.col + y) * 68.4], [(41.3) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4], [(41.3) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(79.8) + (aPiece.row + q) * 80, 80 + (aPiece.col + y) * 68.4], [(118.3) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(118.3) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4]], thickness)
    elif attackSelect:
        thickness = 2
        color = (230, 160, 146)
        x = aPiece.row
        y = aPiece.col
        z = -aPiece.row-aPiece.col
        for x in range(-aPiece.attack_range ,1 + aPiece.attack_range):
            for y in range(-aPiece.attack_range, 1 + aPiece.attack_range):
                for z in range(-aPiece.attack_range, 1 + aPiece.attack_range):          
                    if x + y + z == 0:
                        q = x + (y - (y&1)) / 2
                        if aPiece.col + y >=0 and aPiece.col + y < hexColNum and aPiece.row + q < hexRowNum:
                            if (aPiece.col + y) % 2 == 0:
                                if aPiece.col % 2 == 1:
                                    q += 1
                                pygame.draw.polygon(screen, color, [[(40.4) + (aPiece.row + q) * 80, (168.8) + (aPiece.col + y) * 68.4], [(1.95) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4], [(1.95) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(40.4) + (aPiece.row + q) * 80, 80 + (aPiece.col + y) * 68.4], [(78.9) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(78.9) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4]], thickness)
                            elif (aPiece.col + y) % 2 == 1:
                                pygame.draw.polygon(screen, color, [[(79.8) + (aPiece.row + q) * 80, (168.8) + (aPiece.col + y) * 68.4], [(41.3) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4], [(41.3) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(79.8) + (aPiece.row + q) * 80, 80 + (aPiece.col + y) * 68.4], [(118.3) + (aPiece.row + q) * 80, (102.2) + (aPiece.col + y) * 68.4], [(118.3) + (aPiece.row + q) * 80, (146.6) + (aPiece.col + y) * 68.4]], thickness)
    
def drawPieces(screen, aPiece):
    #makes the point in the upper left corner of the hexagon
    if aPiece.col % 2 == 0:
        screen.blit(aPiece.IMG, ([aPiece.row * 80 + 7, aPiece.col * 68.4 + (100)]))
    elif aPiece.col % 2 == 1:
        screen.blit(aPiece.IMG, ([aPiece.row * 80 + 52, aPiece.col * 68.4 + (100)]))
      
def checkValidMovement(row, column, aPiece, aPieceList):
    for i in range(len(aPieceList)):
        if (row == aPieceList[i].row and column == aPieceList[i].col):
            return False
    for x in range(-aPiece.move, 1 + aPiece.move):
        for y in range(-aPiece.move, 1 + aPiece.move):
            for z in range(-aPiece.move, 1 + aPiece.move):
                if x + y + z == 0:
                    if not (x == 0 and y == 0 and z == 0):
                        q = x + (y - (y&1)) / 2
                        if aPiece.col % 2 == 1:
                            if (aPiece.col + y) % 2 == 0:
                                if row == aPiece.row + q + 1 and column == aPiece.col + y:
                                    return True
                            else:
                                if row == aPiece.row + q and column == aPiece.col + y:
                                    return True
                        elif row == aPiece.row + q and column == aPiece.col + y:
                            return True 
    
    return False

def checkValidAttack(row, column, aPiece, aPieceList):
    for i in range(len(aPieceList)):
        if (row == aPieceList[i].row and column == aPieceList[i].col):
            for x in range(-aPiece.attack_range, 1 + aPiece.attack_range):
                for y in range(-aPiece.attack_range, 1 + aPiece.attack_range):
                    for z in range(-aPiece.attack_range, 1 + aPiece.attack_range):
                        if x + y + z == 0:
                            if not (x == 0 and y == 0 and z == 0):
                                q = x + (y - (y&1)) / 2
                                if aPiece.col % 2 == 1:
                                    if (aPiece.col + y) % 2 == 0:
                                        if row == aPiece.row + q + 1 and column == aPiece.col + y:
                                            return i
                                    else:
                                        if row == aPiece.row + q and column == aPiece.col + y:
                                            return i
                                elif row == aPiece.row + q and column == aPiece.col + y:
                                    return i 
    return -1

def infoDisplayCurrent (grid, row, column, aPiece, player1Turn):
    
    font = pygame.font.SysFont('Times', 16, True, False)
    if player1Turn:
        text = font.render(("It is Player 1's turn ATM *_*" ) ,True, (0, 0, 0))
        screen.blit(text, [450, 20])
    else:
        text = font.render(("It is Player 2's turn rn :O" ) ,True, (0, 0, 0))
        screen.blit(text, [450, 20])

    if grid[row][column] == 1 and aPiece.row == row and aPiece.col == column:
                            
        font = pygame.font.SysFont('Times', 16, True, False)
        text = font.render("Hai " + aPiece.name + ", you have " + str(aPiece.health) + " hp left and " + str(aPiece.action_count) + " actions(s) left O_O" ,True, (0, 0, 0))
        screen.blit(text, [10, 10])

def attackAndKillBingus(grid, row, column, aPiece):
    return False

def checkMobility (grid, row, column, Piecelist):
    for i in range(len(Piecelist)):
        if Piecelist[i].row == row and Piecelist[i].col == column and Piecelist[i].action_count > 0:
            return i
    return -1

class GamePiece:
    def __init__(self, row, col, name, IMG, move, health, damage, attack_range, action_total, hexRowNum, hexColNum):
        self.row = row
        self.col = col
        self.name = name
        self.IMG = IMG
        self.move = move
        self.health = health
        self.damage = damage
        self.attack_range = attack_range
        self.action_count = 0
        self.action_total = action_total
        self.row_max = hexRowNum
        self.col_max = hexColNum
    def change_pos(self, new_row, new_col):
        if new_row <= (self.row_max) and new_row >= 0 and new_col <= (self.col_max) and new_col >= 0:
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid Instance")
    def change_health(self, health_change):
        self.health -= health_change
        if self.health < 1:
            print("piece is dead")
    def change_action_count(self, action_change):
        self.action_count -= action_change
        if self.action_count > self.action_total:
            self.action_count = self.action_total
    def moved(self):
        self.can_move = False
    def new_turn(self):
        self.can_move = True
    def check_action_total(self):
        return self.action_total
    def check_row(self):
        return self.row
    def check_col(self):
        return self.col

main()