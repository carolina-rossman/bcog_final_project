import sys 
import pygame
import os

# creating scrolling background
WIDTH = 623
HEIGHT = 150


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Dash")

class BG:

    def __init__(self, x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()

    def update(self, dx):
        self.x += dx
        if self.x <= -WIDTH:
            self.x = WIDTH

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path  =  os.path.join("assets", "images", "bg.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

# class Score:

#     def __init__(self, hs):
#         self.hs = hs
#         self.act = 0
#         self.font = pygame.font.SysFont('monospace', 18)
#         self.color = (0, 0, 0)
#         self.show()

#     def update(self, loops):
#         self.act = loops // 10
#         self.check_hs()

#     def show(self):
#         self.lbl = self.font.render(f'HI {self.hs} {self.act}', 1, self.color)
#         lbl_width = self.lbl.get_rect{}.width
#         screen.blit(self.lbl, (WIDTH - lbl_width - 10, 10))

#     def check_hs(self):
#         if self.act >= self.hs:
#             self.hs = self.act

#     def reset(self):
#         self.act =0

class Game:

    def __init__(self):
        self.bg = [BG(x=0), BG(x=WIDTH) ]
        self.speed = 3
        # self.score = Score(hs=0)

def main():

    game = Game()

    clock = pygame.time.Clock()

    while True:

        for bg in game.bg:
            bg.update(-game.speed)
            bg.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # clock.tick(80)
        # pygame.display.update()

        # game.score.update(loops)
        # game.score.show()


    
main()