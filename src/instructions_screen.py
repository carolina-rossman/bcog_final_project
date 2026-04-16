import tkinter as tk
class Display(): 
    screen_size = (800, 600)
    def __init__(self):
        self.root = tk.Tk()
        self.screen_size_x = self.screen_size[0]
        self.screen_size_y = self.screen_size [1]
        self.background_image = tk.PhotoImage(file = "../stimuli/instructions_background.png")
        self.load_instructions()
        self.init_window()
        self.create_interface_buttons()
       
    def load_instructions(self): 
        with open ("../stimuli/instructions.txt", "r") as file: 
            self.instructions = file.read()
            
    def init_window(self):
       self.root.title("Instructions Screen")
       self.canvas = tk.Canvas(self.root, width = self.screen_size_x, height= self.screen_size_y)
       self.canvas.pack()
       self.canvas.create_image(
           self.screen_size_x // 2,
           self.screen_size_y //2, 
           image = self.background_image,
       )
       self.canvas.create_text (
           self.screen_size_x //2, 
            100,
            text = self.instructions,
            font = ("Arial", 20, "bold"),
            fill = "white",
            width = 600,
            anchor= "n",
            justify = "left", 
       )
  
    def create_interface_buttons(self): 
        go_button = tk.Button(
           self.root, 
           text = "Next",
           font = ("Arial", 20, "bold"),
           fg = "black",
           command = self.go, 
        )
        go_button.pack()
        self.canvas.create_window(400, 480, window= go_button)
    
    def go(self):
        frame_delay = 50
        self.canvas.destroy()
        self.action_canvas = tk.Canvas(self.root, width= self.screen_size_x, height=self.screen_size_y, bg="black" )
        self.action_canvas.pack()
        self.background = self.action_canvas.create_image(
            self.screen_size_x //2, 
            self.screen_size_y //2,
            image = self.background_image
        )
        self.root.after (frame_delay)


def main(): 
    my_display = Display()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()