import pygame 
import pygame.freetype
import sys
import base_dino

class Display(): 
    screen_size = (800, 600)
    def __init__(self):
        pygame.init()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        self.canvas = pygame.display.set_mode(self.screen_size)
        self.background_image = pygame.image.load("../stimuli/instructions_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_size))
        self.start_button = pygame.Rect(300, 250, 200, 50)
        self.quit_button = pygame.Rect(300, 350, 200, 50)
        pygame.display.set_caption("Instructions Screen")
        self.load_instructions()
       
    def load_instructions(self): 
        with open ("../stimuli/instructions.txt", "r") as file: 
            self.instructions = file.read()
            
    def init_window(self):
       self.canvas.blit(self.background_image, (0,0))
       self.instructions_font = pygame.font.SysFont("Arial", 24)
       instruction = self.instructions_font.render (self.instructions, True, (255, 255, 255))
       instructions_rect = instruction.get_rect (center = (self.screen_size_x/2, 100))
       self.canvas.blit (instruction, instructions_rect)
  
    def create_interface_buttons(self): 
        pygame.draw.rect(self.canvas, (0, 200, 0), self.start_button)
        pygame.draw.rect(self.canvas,(200, 0, 0), self.quit_button)
        self.button_font = pygame.font.SysFont("Arial", 20, bold=True)
        start_text = self.button_font.render ("Next!", True, (255, 255, 255))
        quit_text = self.button_font.render ("Quit", True, (255, 255, 255))
        self.canvas.blit (start_text, (self.start_button.x, self.start_button.y))
        self.canvas.blit(quit_text, (self.quit_button.x, self.quit_button.y))
    
    def go(self):
        clock = pygame.time.Clock()
        running = True 
        while running: 
            self.init_window()
            self.create_interface_buttons()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()   
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    print("Start clicked!")
                    if self.start_button.collidepoint(event.pos):
                        base_dino.Display.go()
                    if self.quit_button.collidepoint(event.pos): 
                        pygame.quit()
                        sys.exit()
            pygame.display.update
            clock.tick(120)


def main(): 
    my_display = Display()
    my_display.go()

if __name__ == "__main__":
    main()