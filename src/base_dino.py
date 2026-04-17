# from YouTube Video https://www.youtube.com/watch?v=ST-Qq3WBZBE
import scrolling_background

import pygame
import sys 

pygame.init()

clock = pygame.time.Clock()
screen = scrolling_background()
pygame.display.set_caption("Jumping in PyGame")

x_position, y_position = 400, 600 
jumping = False 

y_gravity = 1
jump_height = 20 
y_velocity = jump_height

standing_surface = pygame.transform.scale(pygame.image.load("../stimuli/dino.png"), (48, 64))
jumping_surface = pygame.transform.scale(pygame.image.load("../stimuli/dino.png")(48, 64))
background = scrolling_background()

mario_rect = standing_surface.get_rect(center =(x_position, y_position))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]: 
        jumping = True
    
    if jumping: 
        y_position -= y_velocity
        y_velocity -= y_gravity
        if y_velocity <- jump_height:
             jumping = False
             y_velocity = jump_height
        mario_rect = standing_surface.get_rect(center =(x_position, y_position))
        screen.blit(jumping_surface, mario_rect)
    else: 
        mario_rect = standing_surface.get_rect(center = (x_position, y_position))
        screen.blit(standing_surface, mario_rect)


    screen.blit(background, (0,0))
    screen.blit(standing_surface, mario_rect)

    pygame.display.update()
    clock.tick(60)