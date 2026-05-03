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
    print(f'Theta: {-math.degrees(theta)}')
    #Integrate position 
    x += x_dot * dt
    y += y_dot * dt
    theta += omega * dt
    print(f'x: {x}, y: {y}')
    return x, y, theta


def angle_diff(a, b):
    # Computes the smallest angular difference between two angles (a and b)
    # taking into account the circular nature of angles (wrap-around at 2π).
    # So this expression normalizes the difference to the range [-π, π],
    # ensuring we always get the shortest distance between the two angles.
    difference = a - b + math.pi 
    wrap_norm = difference % (2 * math.pi) - math.pi 
    return abs(wrap_norm)      

#Main function
def main():
    PIXELS_PER_METER = 100
    #dt = 0.01 #The simulation moves in steps of 0.01 s (100Hz) 
    
    #Robot Inital State
    robot_x = 0.1 #meters (10 cm)
    robot_y = 1 # meters
    theta = 0
    
    #Robot Geometry
    robot_width = 20
    robot_height = 20
    robot_surface = pygame.Surface((robot_width, robot_height), pygame.SRCALPHA)
    robot_surface.fill((255, 30, 70))
    pygame.draw.line( #Line to show robot front
            robot_surface,
            (0, 0, 0),
            (robot_width//2, robot_height//2),
            (robot_width, robot_height//2),
            2
        )
    
    #Scale to pixels
    robot_pixel_x = robot_x * PIXELS_PER_METER
    robot_pixel_y = robot_y * PIXELS_PER_METER
    robot_rect = robot_surface.get_rect(center=(robot_pixel_x, robot_pixel_y))
    
    points = [(robot_pixel_x, robot_pixel_y)]
    
    #Time for square simulation
    time_elapsed = 0
    #time_goal = 2 # 2 seconds
    
    
    #Square trajectory
    omega = (0.05*(-23.5 + 23.5)) / 0.2
    forward_time = 2.0
    turn_time = 0.1213#(math.pi/2) / 15.5
    index = 0
    trajectory_vals = [
        ('forward', forward_time),
        ('turn',  turn_time),
        ('forward', forward_time),
        ('turn',  turn_time),
        ('forward', forward_time),
        ('turn',  turn_time),
        ('forward', forward_time),
        ('turn',  turn_time),
        
    ]
    
    running = True    
    
    while running:
         # dt is obtained with clock.tick(FPS) / 1000 to otain the real time.
         # This makes the simulation independent of frame rate and ensures consistent physics 
        dt = clock.tick(FPS) / 1000 #To have real time of simulation
        
        #Time
        time_elapsed += dt 
        
        
        mode, time_goal = trajectory_vals[index]
        
        #Get INputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: #Rotate in place
            phi_left = -23.5
            phi_right = 23.5
            print('-'*50)
        elif keys[pygame.K_UP]: #Mover forward
            phi_left = 23.5
            phi_right = 23.5
        elif keys[pygame.K_DOWN]: #Mover backward
            phi_left = -23.5
            phi_right = -23.5
        else: 
            phi_left = 0
            phi_right = 0
            
        
        #Square trajectory
        if mode == 'forward':
            phi_left = 23.5
            phi_right = 23.5
        elif mode == 'turn':
            phi_left = -23.5
            phi_right = 23.5
        print(index)    
        
        if time_elapsed >= time_goal:
            print('SIUUUUUUUUUUUUUUUUUU')
            index += 1
            time_elapsed = 0
            
            if index >= len(trajectory_vals):
                continue    
        print(f'Time elapsed: {time_elapsed}')
        """
        if time_elapsed <= time_goal:
            phi_left = 23.5
            phi_right = 23.5
         """   
       
        
                
        #PROCCESING
        #points.append((robot_pixel_x, robot_pixel_y)) #Past points        
        
        #Convert pixel to meters
        current_x = robot_pixel_x / PIXELS_PER_METER
        current_y = robot_pixel_y / PIXELS_PER_METER
        
        #Update kinematics
        x, y, theta = forward_kinematics(phi_left, phi_right, current_x, current_y, theta, dt)
        
        #Convert meters to pixels
        robot_pixel_x = x * PIXELS_PER_METER
        robot_pixel_y = y * PIXELS_PER_METER
                    
        # Store trajectory (only if moved enough)
        points.append((robot_pixel_x, robot_pixel_y)) #new points
        if len(points) > 1000:
            points.pop(0)           
        
        #Fixed Angle
        theta = theta % (2 * math.pi) # Mantain the angle in the range of 0 an 2pi
        snap_angles = [0, math.pi/2, math.pi, 3*math.pi/2]
        tolerance = 0.0872 #radianes
        
        for angle in snap_angles:
            if angle_diff(theta, angle) < tolerance:
                theta = angle
                break
        
        #Rotate robot
        rotated_robot = pygame.transform.rotate(robot_surface, -math.degrees(theta))
        
        #Give position to robot with center
        robot_rect = rotated_robot.get_rect(center = (robot_pixel_x, robot_pixel_y))
        
        
        #Exit
        for event in pygame.event.get():            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    
        
        
        #RENDER ELEMENTS
        window.fill((255, 255, 255)) #Erase window
        #pygame.draw.rect(window, (255, 30, 70), robot) #Draw robot
        window.blit(rotated_robot, robot_rect)
        
        #Draw Path line
        pygame.draw.lines(window, color=(159,156,155), 
                         closed=False,
                         points=points, width=1)
        
        pygame.display.update()
        #clock.tick(FPS)
        
    


if __name__ == '__main__':
    main()