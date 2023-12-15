import random


class Play:
    def __init__(self, user_input):
        self.user_input = user_input

    def is_valid(self):
        return self.user_input in ["rock", "paper", "scissors"]

    def generate_move(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self):
        winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        computer_input = self.generate_move()

        if self.user_input == computer_input:
            return "tie"

        if winning_moves[self.user_input] == computer_input:
            return "user"
        else:
            return "computer"
