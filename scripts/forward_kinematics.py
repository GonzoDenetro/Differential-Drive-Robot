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
    theta += omega * dt  
    x_dot = vel * math.cos(theta)
    y_dot = vel * math.sin(theta)
        
    print(f'Linear Velocity: {vel}')
    print(f'Omega: {omega}')
    #Integrate position 
    x += x_dot * dt
    y += y_dot * dt
    print(f'x: {x}, y: {y}')
    return x, y
        

def udpdate(robot):
    window.fill((255, 255, 255)) #Erase window
    pygame.draw.rect(window, (255, 30, 70), robot) #Draw robot
        
    pygame.display.update()
    clock.tick(FPS)


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
    theta = 0
    
    #Robot Wheel Velocities
    v_left = []
    v_right = []
    
    running = True
    
    
    
    while running:
        #Get INputs
        
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                print('Cuadrado')
                #angular_vel_left = [31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4]
                #angular_vel_right = [31.4, 31.4, 31.4, 31.4, -31.4, 31.4, 31.4, 31.4, 31.4]
                angular_vel_left = [20]
                angular_vel_right = [31]
                for phi_left, phi_right in zip(angular_vel_left, angular_vel_right):
                    current_x = robot.x / PIXELS_PER_METER
                    current_y = robot.y / PIXELS_PER_METER
                    x, y = forward_kinematics(phi_left, phi_right, current_x, current_y, theta, dt)
                    robot.x = x * PIXELS_PER_METER
                    robot.y = y * PIXELS_PER_METER
                    udpdate(robot)
                    print('-'*50)
            
            
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