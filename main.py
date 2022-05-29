from tkinter import *
from tkinter import ttk
import random


class Game:

    def __init__(self):
        self.window = Tk()
        self.window.title("Rock Paper Scissors")
        self.icon = PhotoImage(file="logo.png")
        self.window.iconphoto(True, self.icon)
        self.window.resizable(False, False)
        frame = ttk.Frame(self.window, padding=(5, 5, 5, 5))
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.win_count = 0
        self.lose_count = 0
        self.scoreboard = StringVar()
        self.win_condition = StringVar()
        self.ai_display = StringVar()
        ttk.Label(frame, text=f"Win: {self.win_count}  Lose: {self.lose_count}").grid(column=2, row=0)
        ttk.Label(frame, textvariable=self.scoreboard).grid(column=2, row=0)
        ttk.Label(frame, textvariable=self.win_condition).grid(column=2, row=2)
        ttk.Label(frame, textvariable=self.ai_display).grid(column=2, row=1)
        ttk.Button(frame, text="Rock", command=self._rock, width=15).grid(column=1, row=3, sticky=SW)
        ttk.Button(frame, text="Paper", command=self._paper, width=15).grid(column=2, row=3, sticky=S)
        ttk.Button(frame, text="Scissors", command=self._scissors, width=15).grid(column=3, row=3, sticky=SE)
        self.window.eval('tk::PlaceWindow . center')

    def _ai_choice(self):
        """Ai randomly select."""
        options = ["rock", "paper", "scissors"]
        return random.choice(options)

    def _ai_display_choice(self, ai):
        self.ai_display.set(f"Ai picked {ai}!")

    def _update_win_count(self):
        self.win_count += 1

    def _update_lose_count(self):
        self.lose_count += 1

    def _update_scoreboard(self):
        self.scoreboard.set(f"Win: {self.win_count}  Lose: {self.lose_count}")

    def _logic(self, user):
        """Compare user input to Ai input."""
        ai = self._ai_choice()

        if user == ai:
            self.win_condition.set("Tie!")
        elif (user == 'rock' and ai == 'scissors') or \
                (user == 'scissors' and ai == 'paper') or \
                (user == 'paper' and ai == 'rock'):
            self.win_condition.set("You win!")
            self._update_win_count()
        else:
            self.win_condition.set("You lose!")
            self._update_lose_count()
        self._ai_display_choice(ai)
        self._update_scoreboard()

    def _rock(self):
        user_input = 'rock'
        self._logic(user_input)

    def _paper(self):
        user_input = 'paper'
        self._logic(user_input)

    def _scissors(self):
        user_input = 'scissors'
        self._logic(user_input)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    Game().run()
