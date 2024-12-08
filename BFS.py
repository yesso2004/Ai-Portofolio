import pygame
import sys
import time
from queue import PriorityQueue


pygame.init() # Intialize pygame
screen = pygame.display.set_mode((900, 600)) # Set screen width and Height
pygame.display.set_caption("Breadth First Search and A* Algorithm") # Set caption for game


background = (255, 255, 255) # Background Color
CellSize = 60 # Size of each node
rows, cols = 10, 10 # Creating a 10 by 10 Grid


walls = [[1, 0, 0, 0, 0, 1, 0, 1, 1, 1], 
         [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],  
         [0, 1, 0, 1, 0, 1, 1, 1, 0, 1],  
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],  
         [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],  
         [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],  
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],   
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],  
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # Maze Creation

start_position = (0, 0)  # Starting Position
end_position = (9, 9)    # Ending Position    

WidthBtn, HeightBtn = 180, 50 # Width and Height of a Button
ColorBtn = (200, 200, 200) # Color of each button
FontColorBtn = (0, 0, 0) # Font Color 
Font = pygame.font.Font(None, 36) # Font Size

BFSBtnPosition = pygame.Rect(650, 100, WidthBtn, HeightBtn) # Position of BFS Button
AStarBtnPosition = pygame.Rect(650, 200, WidthBtn, HeightBtn) # Position of A* Button 


def BFS(walls, node, end): # BFS Function
    visited = []  # list for the visited nodes
    queue = [node]  # queue initialized with start node
    visited.append(node) # appending the start node to the visited array

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # directions to traverse the maze

    while queue: # While loop runs until queue is empty 
        vertex = queue.pop(0) # we pop the first node out of the queue

        for d in directions: # loop to go through all possible directions 
            row, col = vertex[0] + d[0], vertex[1] + d[1] # Traverse the grid using direction like if vertex position is (2,2) and d is (0,1) then move right to (2,3)

            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and walls[row][col] == 1: # first condition ensures we dont go out of bounds and the second ensures that we didnt already visit curent node and lastly the final cond ition ensures we can walk in that direction 
                visited.append((row, col)) # We append the node to the visited array
                queue.append((row, col)) # we also append append the node the queue which will be popped once the loop runs again 

            row, col = vertex # we set the row and column to the current node coordinates
            pygame.draw.rect(screen, (255, 255, 0), (col * CellSize, row * CellSize, CellSize, CellSize)) # draw the path  
            pygame.display.flip() # update the display
            time.sleep(0.03) # Set time for the path to move 

        if vertex == end: # See if we reached the end then we return visited
            return visited

    return visited # If there is no other path then return visited

 # A* Algorithm
def Heuristic(One, Two): # Design the heuristic function to calculate the cost
    return abs(One[0] - Two[0]) + abs(One[1] - Two[1]) # gets the absolute cost of all the rows and add it to the absolute value of all columns 


def AStar(node, end): # Function for the A start algorithm
    visited = [node]  # create visit list with the start node initialized
    Priorityqueue = PriorityQueue()  # Initialize the priority queue
    Priorityqueue.put((0 + Heuristic(node, end), 0, node, [node])) # first tuple is start node with 0 cost added with the final cost which is the heuristic function then the second tuple is the actual cost and the node is the current node we are on and lastly [node] is the path so far 

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # all possible directions if availible

    while not Priorityqueue.empty():  # While there are nodes in the queue
        TotalCost, Cost, Current, Path = Priorityqueue.get()  # Get the node with the lowest cost

        # Check if the current node is the goal
        if Current == end: # if we reach the end then reconstruct the path
            for row, col in Path: # loop that colors the path
                pygame.draw.rect(screen, (0, 255, 0), (col * CellSize, row * CellSize, CellSize, CellSize))  # Draw the path
                pygame.display.flip() # update the display
                time.sleep(0.08)  # Set time for path to move
            return TotalCost, Cost, Path, visited

        # Explore neighbors
        for d in directions:
            row, col = Current[0] + d[0], Current[1] + d[1] # Traverse the grid using direction like if current position is (2,2) and d is (0,1) then move right to (2,3) if the cost is worth it 

            # Check if the neighbor is within bounds, walkable, and not visited
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and walls[row][col] == 1: # first condition ensures we dont go out of bounds and the second ensures that we didnt already visit curent node and lastly the final cond ition ensures we can walk in that direction 
                visited.append((row, col))  # append the node to visited
                Priorityqueue.put(
                    (TotalCost + 1 + Heuristic((row, col), end), Cost + 1, (row, col), Path + [(row, col)]) # Loop over the each node to add the new cost over it which will then be a deciding factor later
                )


    return TotalCost,Cost,Path,visited  # If no path is found


# Loop that keeps the game running until you close the tab.
running = True # Set running to be true 
while running: # as long as the game is running
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # exiting the game will
            running = False # make running false
        elif event.type == pygame.MOUSEBUTTONDOWN: # clicking event to be registered 
            if BFSBtnPosition.collidepoint(event.pos): # if statemenet when we click the bfs button 
                BFS(walls, start_position, end_position) # then run the BFS function
            elif AStarBtnPosition.collidepoint(event.pos): # else if clicking the A* button then
                AStar(start_position, end_position) # run the AStar function

    
    screen.fill(background) # Fill the background of the screen

    for row in range(rows): # for every row in range 10
        for col in range(cols): # for every column in range 10
            rect = pygame.Rect(col * CellSize, row * CellSize, CellSize, CellSize) # create a cell 
            if walls[row][col] == 1:  # if path is unblocked then 
                pygame.draw.rect(screen, (0, 0, 0), rect) # make it black
            else:  # else the path is blocked 
                pygame.draw.rect(screen, (255, 255, 255), rect) # color it white 
            
            if (row, col) == start_position: # if the row and column is in the first position
                text = Font.render('A', True, (0, 0, 255)) # then label it as position A
                screen.blit(text, (rect.x + (CellSize // 3), rect.y + (CellSize // 3))) # Position the text
            elif (row, col) == end_position: # and if the row and column is in the end position 
                text = Font.render('B', True, (255, 0, 0)) # then label it as B
                screen.blit(text, (rect.x + (CellSize // 3), rect.y + (CellSize // 3))) # position the text  

    pygame.draw.rect(screen, ColorBtn, BFSBtnPosition) # make the button color grey for BFS 
    pygame.draw.rect(screen, ColorBtn, AStarBtnPosition) # make the button color grey for A*

    BFSTextBtn = Font.render("BFS", True, FontColorBtn) # Create text BFS for the button
    AStarTextBtn = Font.render("A*", True, FontColorBtn) # Create text A* for the button 

    screen.blit(BFSTextBtn, (BFSBtnPosition.x + 65, BFSBtnPosition.y + 15)) # Position the text BFS in the button
    screen.blit(AStarTextBtn, (AStarBtnPosition.x + 65, AStarBtnPosition.y + 15)) # Position the text A* in the button 

    pygame.display.flip() # update the display 

pygame.quit() # Exit the game 
sys.exit() # Exit the system
