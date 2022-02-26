# -*- coding: utf-8 -*-

from tkinter import Text, Tk, Frame, Button, Label, YES, END, DISABLED, NORMAL, Menu, Image

from PIL import ImageTk

from beautycontest import beautycontest as bc
from beautycontest import player
import time
import numpy as np

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

        # Create a menubar
        self.menubar = Menu(self.window)
        self.gamecascade = Menu(self.menubar, tearoff=0)
        self.gamecascade.add_command(label="Exit",
                                     #image=ImageTk.PhotoImage(file="icons/exit.png"),
                                     command=self.window.destroy)
        self.menubar.add_cascade(label="Game", menu=self.gamecascade)
        self.window.config(menu=self.menubar)
        
        # Create the game
        self.contest = bc()
        self.nb_response = 0
        
        # Create a frame
        self.frame = Frame(self.window)

        # Text zone for printing
        self.console = Text(self.frame,
                            state=DISABLED,
                            height=15,
                            width=80)
        self.console.pack()
        
        # Create the title
        self.label_title = Label(self.frame,
                            text="Welcome to the P-Beauty Contest",
                            font=("Helvetica", 30))
        self.label_title.pack()
        
        # Create the Play button
        self.play_button = Button(self.frame, 
                             text="Play",
                             font=("Helvetica", 20),
                             command=self.contest_initialization)
        self.play_button.pack(pady=25)

        # Frame for players
        self.frame_play = Frame(self.frame)


        # Text zone for players (writing answers) and Button associated
        self.writingconsoleP1 = Text(self.frame_play,
                                    state=NORMAL,
                                    height=1,
                                    width=3)
        #self.writingconsoleP1.pack()
        self.writingconsoleP2 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        #self.writingconsoleP2.pack()
        self.writingconsoleP3 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        #self.writingconsoleP3.pack()
        self.writingconsoleP3 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        #self.writingconsoleP3.pack()
        self.writingconsoleP4 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        #self.writingconsoleP4.pack()
        # Answer button
        self.answer_buttonP1 = Button(self.frame_play,
                                    text="Answer",
                                    font=("Helvetica", 20),
                                    command=self.answeredp1)
        #self.answer_buttonP1.pack(padx=25)
        self.answer_buttonP2 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp2)
        #self.answer_buttonP2.pack(padx=25)
        self.answer_buttonP3 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp3)
        #self.answer_buttonP3.pack(padx=25)
        self.answer_buttonP4 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp4)
        #self.answer_buttonP4.pack(padx=25)
        self.writingconsoleP1.grid(column=0, row=0)
        self.answer_buttonP1.grid(column=0, row=1)
        self.writingconsoleP2.grid(column=1, row=0)
        self.answer_buttonP2.grid(column=1, row=1)
        self.writingconsoleP3.grid(column=2, row=0)
        self.answer_buttonP3.grid(column=2, row=1)
        self.writingconsoleP4.grid(column=3, row=0)
        self.answer_buttonP4.grid(column=3, row=1)
        self.frame_play.pack()
        
        # Run
        self.frame.pack(expand=YES)
        self.write("Welcome to the P-Beauty Contest")
        self.window.mainloop()
        
    def contest_initialization(self):
        self.contest.current_round = 1
        self.write("Round 1 begin")
        self.write("Please, give your answer.")
        self.contest.players[1].selected_value = 10
        self.contest.players[1].selected_value = 30
        self.contest.players[1].selected_value = 30

    def answeredp1(self):
        # TODO check the int condition separatly for no error
        answer = int(self.writingconsoleP1.get(1.0, "end-1c"))
        if type(answer) is int:
            if 0<=answer & answer<=100:
                self.contest.players[0].selected_value = answer
                self.write(answer)
                self.nb_response = self.nb_response + 1
                if self.nb_response == 4:
                    self.nb_response = 0
                    self.mean()
            else:
                self.write("Your answer is not included in [0,100].")
        else:
            self.write("Your answer is not a number.")

    def answeredp2(self):
        # TODO check the int condition separatly for no error
        answer = int(self.writingconsoleP2.get(1.0, "end-1c"))
        if type(answer) is int:
            if 0<=answer & answer<=100:
                self.contest.players[1].selected_value = answer
                self.write(answer)
                self.nb_response = self.nb_response + 1
                if self.nb_response == 4:
                    self.nb_response = 0
                    self.mean()
            else:
                self.write("Your answer is not included in [0,100].")
        else:
            self.write("Your answer is not a number.")

    def answeredp3(self):
        # TODO check the int condition separatly for no error
        answer = int(self.writingconsoleP3.get(1.0, "end-1c"))
        if type(answer) is int:
            if 0<=answer & answer<=100:
                self.contest.players[2].selected_value = answer
                self.write(answer)
                self.nb_response = self.nb_response + 1
                if self.nb_response == 4:
                    self.nb_response = 0
                    self.mean()
            else:
                self.write("Your answer is not included in [0,100].")
        else:
            self.write("Your answer is not a number.")

    def answeredp4(self):
        # TODO check the int condition separatly for no error
        answer = int(self.writingconsoleP4.get(1.0, "end-1c"))
        if type(answer) is int:
            if 0<=answer & answer<=100:
                self.contest.players[3].selected_value = answer
                self.write(answer)
                self.nb_response = self.nb_response + 1
                if self.nb_response == 4:
                    self.nb_response = 0
                    self.mean()
            else:
                self.write("Your answer is not included in [0,100].")
        else:
            self.write("Your answer is not a number.")

    def mean(self):
        contest_mean = self.contest.mean()
        tempplayer = self.whowin(contest_mean * self.contest.p)
        self.winner(tempplayer)

    def whowin(self, valuetoguess: int):
        global closerplayer
        lastgap = 100
        for player in self.contest.players:
            gap = self.checkgap(valuetoguess, player)
            if lastgap > gap :
                lastgap = gap
                closerplayer = player
        return closerplayer

    def checkgap(self, v: int, p: player):
        return abs(v - p.selected_value)

    def winner(self, winner: player):
        tempstr = winner.name + "round n°" + str(self.contest.current_round)
        self.write(tempstr)
        self.contest.current_round = self.contest.current_round + 1
        winner.score = winner.score + 1
        self.checkifendgame(winner)

    def checkifendgame(self, winner: player):
        if winner.score >= 5:
            tempstr = winner.name + "win the game !"
            self.write(tempstr)
            self.contest_reinitialization()

    def contest_reinitialization(self):
        for player in self.contest.players:
            player.score = 0
            player.current_value = -1
        self.contest.current_round = 1
        self.write("Round 1 begin")
        self.write("Please, give your answer.")

    def write(self, message, end="\n"):
        text = str(message)
        text += end
        self.console["state"] = NORMAL
        self.console.insert(END, text)
        self.console["state"] = DISABLED
        
if __name__ == "__main__":
    w = Window()
