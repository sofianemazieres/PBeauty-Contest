# -*- coding: utf-8 -*-

from tkinter import Text, Tk, Frame, Button, Label, YES, END, DISABLED, NORMAL
from beautycontest import beautycontest as bc


class Window():
    #Constructor
    def __init__(self):
        # Create a window
        self.window = Tk()
        
        # Set the parameters of the window
        self.window.title("P-beauty contest")
        self.window.geometry("1080x720")
        self.window.minsize(480, 720)
        self.window.iconbitmap("icons/keynes.ico")
        
        # Create the game
        self.contest = bc()
        
        # Text zone for printing
        self.console = Text(self.window,
                            state = DISABLED)
        self.console.pack()
        
        # Create a frame
        self.frame = Frame(self.window)
        
        # Create the title
        self.label_title = Label(self.frame,
                            text = "Welcome to the P-Beauty Contest",
                            font = ("Helvetica", 30))
        self.label_title.pack()
        
        # Create the PLay button
        self.play_button = Button(self.frame, 
                             text = "Play", 
                             font = ("Helvetica", 20),
                             command = self.write)#contest.init_contest())
        self.play_button.pack(pady = 25)
        
        # Run
        self.frame.pack(expand = YES)
        self.window.mainloop()
        

    def write(self):#, message, end = "\n", sep = " "):
        text = "Welcome to the P-Beauty Contest"
        #text += message
        #text += end
        self.console["state"] = NORMAL
        self.console.insert(END, text)
        self.console["state"] = DISABLED
        
if __name__ == "__main__":
    w = Window()
    #w.write()
