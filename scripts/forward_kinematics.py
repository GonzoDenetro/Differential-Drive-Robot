import pygame
import sys
import random
from pygame.locals import * 


#Initialize Pygame
pygame.init()


#Game Setup
FPS = 60
clock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Differential Robot - Forward Kinematics')

#Main function
def main():
    #Robot Configuration
    init_pos = [10, 10]
    robot_width = 20
    robot_height = 20
    robot = pygame.Rect(init_pos[0], init_pos[1], robot_width, robot_height)
    
    running = True
    
    while running:
        #Get INputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        #Processing
        
        
        #Render Elements
        pygame.display.update()
        clock.tick(FPS)
        
        pygame.draw.rect(window, (255, 30, 70), robot)


if __name__ == '__main__':
    main()