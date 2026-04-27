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
    robot_x = 10
    robot_y = 10
    robot_width = 20
    robot_height = 20
    robot = pygame.Rect(robot_x, robot_y, robot_width, robot_height)
    
    #Robot Wheel Velocities
    
    running = True
    
    while running:
        #Get INputs
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                robot.x += 3
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        #Processing
        
        
        #Render Elements
        window.fill((255, 255, 255)) #Erase window
        pygame.draw.rect(window, (255, 30, 70), robot) #Draw robot
        
        pygame.display.update()
        clock.tick(FPS)
        
    


if __name__ == '__main__':
    main()