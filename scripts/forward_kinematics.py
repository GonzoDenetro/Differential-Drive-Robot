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


if __name__ == '__main__':
    main()