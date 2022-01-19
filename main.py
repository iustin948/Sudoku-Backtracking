import pygame
import time
pygame.init()
WIDTH = 759
screen = pygame.display.set_mode((WIDTH, WIDTH))
SIZE = 83
MID = 42
running = True
WHITE = (255, 255, 255)
RED =   (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
GAPX = 1
GAPY = 0
clock = pygame.time.Clock()
class Node():
    def __init__(self, row, col, width):
        self.map = 0
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = WHITE
    def get_pos(self):
        return self.row, self.col
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.coordy, self.coordx, self.width, self.width))
        #pygame.display.update()

def make_Grid(rows, width):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range (rows):
            node = Node(i, j, SIZE)
            grid[i].append(node)
    return grid

def draw(screen,grid, rows, width):
    screen.fill(CYAN)
    for row in grid:
        global GAPY
        global GAPX
        GAPY = 1
        for Node in row:
            Node.coordx = Node.x + GAPX
            Node.coordy = Node.y + GAPY
            Node.draw()
            GAPY = GAPY + 1
        GAPX = GAPX + 1

    for i in range (9):
        for j in range (9):
            if INPUT[i][j] != 0:
                Draw_number(INPUT[i][j], i, j)

def draw_lines(color):
    pygame.draw.line(screen, color, (253, 1), (253, 774), 3)
    pygame.draw.line(screen, color, (505, 1), (505, 774), 3)

    pygame.draw.line(screen, color, (1, 253), (774, 253), 3)
    pygame.draw.line(screen, color, (1, 505), (774, 505), 3)

    pygame.draw.line(screen, color, (0,0), (0, 777), 4)
    pygame.draw.line(screen, color, (0,0), (777, 0), 4)
    pygame.draw.line(screen, color, (758,758), (758, 0), 5)
    pygame.draw.line(screen, color, (758,758), (0, 758), 5)

INPUT = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def Draw_number(x ,j ,i):
    font = pygame.font.SysFont('arial', 30)
    text = font.render(str(x), True, (0, 0, 0))
    rect = text.get_rect()
    rect.center = (i*SIZE+MID, j*SIZE+MID)
    screen.blit(text, rect)
    pygame.display.update()

vertical = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
horizontal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]


def Check(i, j, k):
    for d in range (9):
        if INPUT[i][d] == k:
            return False

    for d in range (9):
        if INPUT[d][j] == k:
            return False

    box_x = i // 3
    box_y = j // 3
    box_x = box_x * 3
    box_y = box_y * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if INPUT[i][j] == k:
                return False

    return True

def _find():
    for i in range(9):
        for j in range(9):
            if INPUT[i][j] == 0:
                return i ,j


def Backtracking():
   find = _find()
   if not find:
        return True
   else:
        i, j = find
   for k in range (1,10):
      if Check(i , j , k):
         INPUT[i][j] = k
         Draw_number(k, i , j)
         pygame.display.update()
         #clock.tick(50)
         if Backtracking():
            return True
         INPUT[i][j] = 0
         grid[i][j].draw()
         pygame.display.update()
         #clock.tick(200)
   return False



grid = make_Grid(9,SIZE)
draw(screen,grid,9,SIZE)
draw_lines(BLACK)
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
             if (event.key == pygame.K_SPACE):
                 Backtracking()
                 draw_lines(GREEN)
                 pygame.display.update()

