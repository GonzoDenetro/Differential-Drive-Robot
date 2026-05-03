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



def forward_kinematics(phi_l, phi_r, x, y, theta, dt):
    radius = 0.05 #meters
    L = 0.2 # Robot Length

    
    vel = ((phi_l*radius)+(phi_r*radius)) / 2 # m/s
    omega = (radius*(-phi_l + phi_r)) / L
    
    #Use the prevous theta
    theta_old = theta
      
    x_dot = vel * math.cos(theta_old)
    y_dot = vel * math.sin(theta_old)
        
    print(f'Linear Velocity: {vel}')
    print(f'Omega: {omega}')
    print(f'Theta: {theta}')
    #Integrate position 
    x += x_dot * dt
    y += y_dot * dt
    theta += omega * dt
    print(f'x: {x}, y: {y}')
    return x, y, theta
        

#Main function
def main():
    PIXELS_PER_METER = 100
    #dt = 0.01 #The simulation moves in steps of 0.01 s (100Hz) 
    
    #Robot Configuration
    robot_x = 0.1 #meters (1 meters)
    robot_y = 1 # meters
    robot_width = 20
    robot_height = 20
    robot_surface = pygame.Surface((robot_width, robot_height), pygame.SRCALPHA)
    robot_surface.fill((255, 30, 70))
    theta = 0
    
    robot_pixel_x = robot_x * PIXELS_PER_METER
    robot_pixel_y = robot_y * PIXELS_PER_METER
    robot_rect = robot_surface.get_rect(center=(robot_pixel_x, robot_pixel_y))
    
    
    running = True
    
    
    
    while running:
         # dt is obtained with clock.tick(FPS) / 1000 to otain the real time.
         # This make that the simulation don´t depend of the FPS fixed, otherwise in real time 
        dt = clock.tick(FPS) / 1000 #To have real time of simulation
        
        #Get INputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            phi_left = -31
            phi_right = 31
            print('-'*50)
        elif keys[pygame.K_UP]:
            phi_left = 31
            phi_right = 31
        else: 
            phi_left = 0
            phi_right = 0
            
            
        #Processing        
        current_x = robot_pixel_x / PIXELS_PER_METER
        current_y = robot_pixel_y / PIXELS_PER_METER
        x, y, theta = forward_kinematics(phi_left, phi_right, current_x, current_y, theta, dt)
        robot_pixel_x = x * PIXELS_PER_METER
        robot_pixel_y = y * PIXELS_PER_METER
                    
        #Rotate robot
        rotated_robot = pygame.transform.rotate(robot_surface, -math.degrees(theta))
        robot_rect = rotated_robot.get_rect(center = (robot_pixel_x, robot_pixel_y))
        
        
        #Exit
        for event in pygame.event.get():            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    
        
        
        #Render Elements
        window.fill((255, 255, 255)) #Erase window
        #pygame.draw.rect(window, (255, 30, 70), robot) #Draw robot
        window.blit(rotated_robot, robot_rect)
        pygame.draw.line(
            robot_surface,
            (0, 0, 0),
            (robot_width//2, robot_height//2),
            (robot_width, robot_height//2),
            2
        )
        
        pygame.display.update()
        #clock.tick(FPS)
        
    


if __name__ == '__main__':
    main()