import tkinter as tk
import instructions_screen
class Display(): 
    screen_size = (800, 600)
    def __init__(self, root):
        self.root = root
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        self.background_image = tk.PhotoImage(file = "../stimuli/start_screen_background.png")
        self.init_window()
        self.create_interface_buttons()

    def init_window(self):
       self.root.title("Start Screen")
       self.canvas = tk.Canvas(self.root, width = self.screen_size_x, height= self.screen_size_y)
       self.canvas.pack()
       self.canvas.create_image(
           self.screen_size_x // 2,
           self.screen_size_y //2, 
           image = self.background_image,
       )
       self.canvas.create_rectangle(
           250, 
           70, 
           550, 
           130, 
           fill = "white",
       )
       self.canvas.create_text (
           self.screen_size_x //2, 
           100,
           text = "Dino Dash",
           font = ("Arial", 60, "bold"),
           fill = "black",
       )
    def create_interface_buttons(self):
        # quit button 
        quit_button = tk.Button(
           self.root, 
           text = "Quit",
           font = ("Arial", 20),
           fg = "black",
           command = self.root.destroy,  
           bd = 0,
           highlightthickness=0,
           relief= tk.SUNKEN,
      )
        quit_button.pack()
        # go button
        go_button = tk.Button(
           self.root, 
           text = "Start!",
           font = ("Arial", 40, "bold"),
           fg = "black",
           command = self.go, 
        )
        go_button.pack()

        self.canvas.create_window(400, 440, window= go_button)
        self.canvas.create_window(400, 500, window=quit_button)
    def go(self):
        self.root.destroy()
        new_root = tk.Tk()
        instructions_screen.Display(new_root)
        new_root.mainloop()

def main(): 
    my_display = Display()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()