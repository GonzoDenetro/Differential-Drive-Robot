import pygame
import sys
import random
from pygame.locals import * 
import math

#Initialize Pygame
pygame.init()


#Game Setup
FPS = 60
clock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Differential Robot - Forward Kinematics')



def forward_kinematics(angular_vel_left, angular_vel_right):
    radius = 0.05 #meters
    L = 0.2
    dt = 0.01
    theta = 0
    x = 0
    y = 0
    
    for phi_l, phi_r in zip(angular_vel_left, angular_vel_right):
        vel = ((phi_l*radius)+(phi_r*radius)) / 2
        omega = (radius*(-phi_l + phi_r)) / L
        theta += omega * dt  
        x_dot = vel * math.cos(theta)
        y_dot = vel * math.sin(theta)
        
        print(f'Linear Velocity: {vel}')
        print(f'Omega: {omega}')
        #Integrate position 
        x += x_dot * dt
        y += y_dot * dt
        


#Main function
def main():
    PIXELS_PER_METER = 100
    dt = 0.01 #The simulation moves in steps of 0.01 s (100Hz) 
    
    #Robot Configuration
    robot_x = 1 #meters (1 meters)
    robot_y = 1 # meters
    robot_width = 20
    robot_height = 20
    robot = pygame.Rect(robot_x*PIXELS_PER_METER, robot_y*PIXELS_PER_METER, robot_width, robot_height)
    
    #Robot Wheel Velocities
    v_left = []
    v_right = []
    
    running = False
    
    
    angular_vel_left = [31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4]
    angular_vel_right = [31.4, 31.4, 31.4, 31.4, -31.4, 31.4, 31.4, 31.4, 31.4]
    forward_kinematics(angular_vel_left, angular_vel_right)
    
    while running:
        #Get INputs
        
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                pass
            
            
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