# -*- coding: utf-8 -*-

from tkinter import Text, Tk, Frame, Button, Label, YES, END, DISABLED, NORMAL, Menu, Image

from PIL import ImageTk
from tabulate import tabulate

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
        self.p1hasanswered = False
        self.p2hasanswered = False
        self.p3hasanswered = False
        self.p4hasanswered = False
        
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

        # Run
        self.frame.pack(expand=YES)
        self.write("Welcome to the P-Beauty Contest")
        self.window.mainloop()


    """ Begin the contest by printing some text and creating the button and textzone for the 4 players.
    """
    def contest_initialization(self):
        self.contest.current_round = 1
        self.write("Round 1 begin")
        self.write("Please, give your answer.")
        # Frame for players
        self.frame_play = Frame(self.frame)

        # Text zone for players (writing answers) and Button associated
        self.writingconsoleP1 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        # self.writingconsoleP1.pack()
        self.writingconsoleP2 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        # self.writingconsoleP2.pack()
        self.writingconsoleP3 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        # self.writingconsoleP3.pack()
        self.writingconsoleP3 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        # self.writingconsoleP3.pack()
        self.writingconsoleP4 = Text(self.frame_play,
                                     state=NORMAL,
                                     height=1,
                                     width=3)
        # self.writingconsoleP4.pack()
        # Answer button
        self.answer_buttonP1 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp1)
        # self.answer_buttonP1.pack(padx=25)
        self.answer_buttonP2 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp2)
        # self.answer_buttonP2.pack(padx=25)
        self.answer_buttonP3 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp3)
        # self.answer_buttonP3.pack(padx=25)
        self.answer_buttonP4 = Button(self.frame_play,
                                      text="Answer",
                                      font=("Helvetica", 20),
                                      command=self.answeredp4)
        # self.answer_buttonP4.pack(padx=25)
        self.writingconsoleP1.grid(column=0, row=0)
        self.answer_buttonP1.grid(column=0, row=1)
        self.writingconsoleP2.grid(column=1, row=0)
        self.answer_buttonP2.grid(column=1, row=1)
        self.writingconsoleP3.grid(column=2, row=0)
        self.answer_buttonP3.grid(column=2, row=1)
        self.writingconsoleP4.grid(column=3, row=0)
        self.answer_buttonP4.grid(column=3, row=1)
        self.frame_play.pack()

    """ Get the answer of player 1.
    """
    def answeredp1(self):
        if self.writingconsoleP1.get(1.0, "end-1c").isdigit():
            answer = int(self.writingconsoleP1.get(1.0, "end-1c"))
            if not self.p1hasanswered:
                if 0<=answer & answer<=100:
                    self.contest.players[0].selected_value = answer
                    tempstr = self.contest.players[0].name + " has answered."
                    #self.write(answer)
                    self.nb_response = self.nb_response + 1
                    self.p1hasanswered = True
                    if self.nb_response == 4:
                        self.write(tempstr)
                        tempstr = ""
                        self.nb_response = 0
                        self.mean()
                else:
                    tempstr = self.contest.players[0].name + " : Your answer is not included in [0,100]."
            else:
                tempstr = self.contest.players[0].name + " :  You have already answered."
        else:
            tempstr = self.contest.players[0].name + ": Your answer is a negative number or not a number."
        self.write(tempstr)

    """ Get the answer of player 2.
    """
    def answeredp2(self):
        if self.writingconsoleP2.get(1.0, "end-1c").isdigit():
            answer = int(self.writingconsoleP2.get(1.0, "end-1c"))
            if not self.p2hasanswered:
                if 0<=answer & answer<=100:
                    self.contest.players[1].selected_value = answer
                    tempstr = self.contest.players[1].name + " has answered."
                    #self.write(answer)
                    self.nb_response = self.nb_response + 1
                    self.p2hasanswered = True
                    if self.nb_response == 4:
                        self.write(tempstr)
                        tempstr = ""
                        self.nb_response = 0
                        self.mean()
                else:
                    tempstr = self.contest.players[1].name + " : Your answer is not included in [0,100]."
            else:
                tempstr = self.contest.players[1].name + " :  You have already answered."
        else:
            tempstr = self.contest.players[1].name + ": Your answer is a negative number or not a number."
        self.write(tempstr)

    """ Get the answer of player 3.
    """
    def answeredp3(self):
        if self.writingconsoleP3.get(1.0, "end-1c").isdigit():
            answer = int(self.writingconsoleP3.get(1.0, "end-1c"))
            if not self.p3hasanswered:
                if 0<=answer & answer<=100:
                    self.contest.players[2].selected_value = answer
                    tempstr = self.contest.players[2].name + " has answered."
                    #self.write(answer)
                    self.nb_response = self.nb_response + 1
                    self.p3hasanswered = True
                    if self.nb_response == 4:
                        self.write(tempstr)
                        tempstr = ""
                        self.nb_response = 0
                        self.mean()
                else:
                    tempstr = self.contest.players[2].name + " : Your answer is not included in [0,100]."
            else:
                tempstr = self.contest.players[2].name + " :  You have already answered."
        else:
            tempstr = self.contest.players[2].name + ": Your answer is a negative number or not a number."
        self.write(tempstr)

    """ Get the answer of player 4.
    """
    def answeredp4(self):
        if self.writingconsoleP4.get(1.0, "end-1c").isdigit():
            answer = int(self.writingconsoleP4.get(1.0, "end-1c"))
            if not self.p4hasanswered:
                if 0<=answer & answer<=100:
                    self.contest.players[3].selected_value = answer
                    tempstr = self.contest.players[3].name + " has answered."
                    #self.write(answer)
                    self.nb_response = self.nb_response + 1
                    self.p4hasanswered = True
                    if self.nb_response == 4:
                        self.write(tempstr)
                        tempstr = ""
                        self.nb_response = 0
                        self.mean()
                else:
                    tempstr = self.contest.players[3].name + " : Your answer is not included in [0,100]."
            else:
                tempstr = self.contest.players[3].name + " :  You have already answered."
        else:
            tempstr = self.contest.players[3].name + ": Your answer is a negative number or not a number."
        self.write(tempstr)


    """ Calculate the mean of players' values.
    """
    def mean(self):
        contest_mean = self.contest.mean()

        head = ["Player", "Guess"]
        table = [[self.contest.players[0].name, self.contest.players[0].selected_value],
                 [self.contest.players[1].name, self.contest.players[1].selected_value],
                 [self.contest.players[2].name, self.contest.players[2].selected_value],
                 [self.contest.players[3].name, self.contest.players[3].selected_value]]
        self.console["state"] = NORMAL
        self.console.insert(END, tabulate(table, headers=head, tablefmt="grid") + '\n')
        self.console.insert(END, "Mean : " + str(contest_mean) + '\n')
        self.console["state"] = DISABLED

        tempplayer = self.whowin(contest_mean * self.contest.p)
        self.winner(tempplayer)

    """ Find the winner of the round.
    """
    def whowin(self, valuetoguess: int):
        global closerplayer
        lastgap = 100
        for player in self.contest.players:
            gap = self.checkgap(valuetoguess, player)
            if lastgap > gap :
                lastgap = gap
                closerplayer = player
        return closerplayer

    """ Calculate the gap between the selected value and the value to guess.
    """
    def checkgap(self, v: int, p: player):
        return abs(v - p.selected_value)


    """ Write the winner of the current round, update the round and check if the game end.
    """
    def winner(self, winner: player):
        tempstr = winner.name + " win round n°" + str(self.contest.current_round)
        self.write(tempstr)
        self.contest.current_round = self.contest.current_round + 1
        winner.score = winner.score + 1
        self.checkifendgame(winner)


    """ Check if the last player to win a point has 5 points. If yes, it reinitialize the game.
    """
    def checkifendgame(self, winner: player):
        if winner.score >= 5:
            tempstr = winner.name + "win the game !"
            self.write(tempstr)
            self.contest_reinitialization()

    """ Reinitialize game parameters.
    """
    def contest_reinitialization(self):
        for player in self.contest.players:
            player.score = 0
            player.current_value = -1
        self.contest.current_round = 1
        self.write("Round 1 begin")
        self.write("Please, give your answer.")


    """ Write in the window textbox.
    """
    def write(self, message, end="\n"):
        text = str(message)
        text += end
        self.console["state"] = NORMAL
        self.console.insert(END, text)
        self.console["state"] = DISABLED
        
if __name__ == "__main__":
    w = Window()
