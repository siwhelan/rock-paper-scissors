import random


class Play:
    def __init__(self, user_input):
        self.user_input = user_input
        self.computer_move = None

    def is_valid(self):
        return self.user_input in ["rock", "paper", "scissors"]

    def generate_move(self):
        self.computer_move = random.choice(["rock", "paper", "scissors"])
        return self.computer_move

    def determine_winner(self):
        if self.computer_move is None:
            self.generate_move()

        winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        if self.user_input == self.computer_move:
            return "tie"
        elif winning_moves[self.user_input] == self.computer_move:
            return "user"
        else:
            return "computer"
