import sys 
import pygame



pygame.init()

# setting up score display

font = pygame.font.Font (None,14)
def draw_score_counter(meters,screen): #creating the scoreboard and it will count the distances traveled in meters.
    
    score_text = font.render (f"Distance: {int(meters)}", True, 'black') #learned how to code font rendering from (https://youtu.be/tK-r89FYF-M?si=wS5nElx8qoJ49Ype)
    screen.blit(score_text,(548,6))
