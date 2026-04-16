import tkinter as tk 
import random


class Display(): 
    def __init__(self, root): 
        pass 
        self.init_window()
        self.load_dino
        self.create_obstacles()
        self.create_powerups()
        self.create_powerdowns()

        # load scrolling background from other .py
    def init_window(self): 
        pass
    
    def load_dino(self): 
        self.dino = tk.PhotoImage(file = "../stimuli/dino.png")

    def create_powerups(self): 
        self.jetpack = tk.PhotoImage(file = "../stimuli/_______")
        self.immunity = tk.PhotoImage(file = "../stimuli/_____")
        self.revival = tk.PhotoImage(file = "../stimuli/_____")

    def create_powerdowns(self):
        self.speed_up = tk.PhotoImage(file = "../stimuli/_____")
        
    def create_obstacles(self): 
        self.fence = tk.PhotoImage(file= "../stimuli/fence.png")
        self.bush = tk.PhotoImage(file = "../stimuli/bush.png")
        selected_obstacles = random.choice ([self.bush, self.fence])
        # generate those images as background scrolls 
        # use pygame


        
 




def main(): 
     my_display = Display()
     my_display.root.mainloop() 

if __name__ == "__main__":
    main()