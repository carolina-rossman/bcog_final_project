import tkinter as tk 
import random
import pygame
import base_dino

class Display(): 
    def __init__(self, root):  
        self.init_window()
        self.load_dino
        self.create_obstacles()
        self.create_powerups()
        self.create_powerdowns()

        # load scrolling background from other .py
    def init_window(self): 
        base_dino()

    def create_powerups(self): 
        self.jetpack = tk.PhotoImage(file = "../stimuli/jetpack_token.png")
        self.immunity = tk.PhotoImage(file = "../stimuli/shield_token.png")
        self.revival = tk.PhotoImage(file = "../stimuli/life_token.png")
        selected_powerup = random.choice(self.jetpack, self.immunity, self.revival)

    def create_powerdowns(self):
        self.speed_up = tk.PhotoImage(file = "../stimuli/double_time_token.png")
        self.tiny_dino = tk.PhotoImage(file = "../stimuli/tiny_dino_token.png")
        selected_powerdown = random.choice(self.speed_up, self.tiny_dino)
        
    def create_obstacles(self): 
        self.fence = tk.PhotoImage(file= "../stimuli/fence.png")
        self.bush = tk.PhotoImage(file = "../stimuli/bush.png")
        selected_obstacles = random.choice (self.bush, self.fence)
        # generate those images as background scrolls 
        # use pygame
    def user_jumps(self): 
        pass


        
 




def main(): 
     my_display = Display()
     my_display.root.mainloop() 

if __name__ == "__main__":
    main()