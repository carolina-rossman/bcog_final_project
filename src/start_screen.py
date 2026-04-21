import pygame 
import pygame.freetype
from pygame.sprite import Sprite 
from pygame.rect import Rect 
import instructions_screen
import sys

class Display(): 
    screen_size = pygame.Surface((800, 600))
    def __init__(self):
        pygame.init()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        self.canvas = pygame.display.set_mode(width = self.screen_size_x, height= self.screen_size_y)
        self.background_image = pygame.image.load(file = "../stimuli/start_screen_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_size_x, self.screen_size_y))
        pygame.display.set_caption("Start Screen")
        self.init_window()
        self.create_interface_buttons()

    def init_window(self):
       self.canvas.blit(self.background_image)
       pygame.draw.rect(self.canvas)
       self.title_font = pygame.font.SysFont("Arial", 60, bold = True)
       title = self.title.render ("Dino Dash")
       self.canvas.blit (title)
       pygame.display.update()

    def create_interface_buttons(self):
        # quit button 
        pygame.draw.rect(self.canvas, self.start_button)
        pygame.draw.rect(self.canvas, self.quit_button)
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        start_text = self.button_font.render ("Start!", True)
        quit_text = self.button_font.render ("Quit", True)
        self.canvas.blit (start_text, (self.start_button.x, self.start_button.y))
        self.canvas.blit(quit_text, (self.quit_button.x, self.quit_button.y))
        pygame.display.update()
    def go(self):
        running = True 
        while running: 
            self.init_window()
            self.create_interface_buttons()
            pygame.display.update()
            for response in pygame.event.get(): 
                if response.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
            
                if response.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = response.pos
                    if self.start_button.collidepoint(mouse_pos):
                        instructions_screen.Display.go()
                    if self.quit_button.collidepoint(mouse_pos): 
                        pygame.quit()
                        sys.exit()
        instructions_screen.Display().run()
        


def main(): 
    my_display = Display()
    my_display.go()

if __name__ == "__main__":
    main()