import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Breadth First Search")

background = (255, 255, 255)
CellSize = 60
rows, cols = 10, 10

# Set black as path (0), white as walls (1), and ensure start ('A') and end ('B') are on the path
walls = [[0, 1, 1, 1, 1, 0, 1, 0, 0, 0], 
         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],  
         [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],  
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],  
         [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],  
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  
         [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],   
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  

start_position = (0, 0)  
end_position = (9, 9)    
walls[start_position[0]][start_position[1]] = 0 
walls[end_position[0]][end_position[1]] = 0      

WidthBtn, HeightBtn = 180, 50
ColorBtn = (200, 200, 200)
FontColorBtn = (0, 0, 0)
Font = pygame.font.Font(None, 36)

BFSBtnPosition = pygame.Rect(650, 100, WidthBtn, HeightBtn)

# BFS function with Pygame animation
def BFS(grid, start, end):
    visited = []
    queue = [start]
    visited.append(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        vertex = queue.pop(0)
        
        # Visualize the cell being processed
        if vertex != start and vertex != end:
            row, col = vertex
            pygame.draw.rect(screen, (255, 255, 0), (col * CellSize, row * CellSize, CellSize, CellSize))
            pygame.display.flip()
            time.sleep(0.1)

        if vertex == end:
            return visited
        
        for d in directions:
            row, col = vertex[0] + d[0], vertex[1] + d[1]
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and grid[row][col] == 0:
                visited.append((row, col))
                queue.append((row, col))

    return visited


# Main Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if BFSBtnPosition.collidepoint(event.pos):
                BFS(walls, start_position, end_position)

    screen.fill(background)

    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CellSize, row * CellSize, CellSize, CellSize)
            if walls[row][col] == 0:  
                pygame.draw.rect(screen, (0, 0, 0), rect) 
            else:  # Wall
                pygame.draw.rect(screen, (255, 255, 255), rect) 
            
            if (row, col) == start_position:
                text = Font.render('A', True, (0, 0, 255))  
                screen.blit(text, (rect.x + (CellSize // 3), rect.y + (CellSize // 3)))
            elif (row, col) == end_position:
                text = Font.render('B', True, (255, 0, 0))  
                screen.blit(text, (rect.x + (CellSize // 3), rect.y + (CellSize // 3)))

    pygame.draw.rect(screen, ColorBtn, BFSBtnPosition)
    BFSTextBtn = Font.render("BFS", True, FontColorBtn)
    screen.blit(BFSTextBtn, (BFSBtnPosition.x + 65, BFSBtnPosition.y + 15))

    pygame.display.flip()

pygame.quit()
sys.exit()
