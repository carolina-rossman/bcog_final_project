import sys #From Me!
import pygame #From Me!



# pygame.init() #From Me!

# # setting up score display

# font = pygame.font.Font (None,14) #From Me!
def draw_score_counter(meters, screen, font): #creating the scoreboard and it will count the distances traveled in meters. From Me!
    
    score_text = font.render(f"Distance: {int(meters)}", True, 'black') #From Me! learned how to code font rendering from (https://youtu.be/tK-r89FYF-M?si=wS5nElx8qoJ49Ype)
    screen.blit(score_text,(548,6)) #From Me!
