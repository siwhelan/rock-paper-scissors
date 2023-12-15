from lib.game import *


def test_play_takes_user_input():
    play = Play("rock")
    assert play.user_input == "rock"


# test an error is raised if the user input is not valid
def test_is_valid():
    play = Play("rock")
    assert play.is_valid() is True
    play = Play("banana")
    assert play.is_valid() is False


# test generate_move generates a random move for the computer
def test_generate_move():
    play = Play("rock")
    computer_move = play.generate_move()
    assert computer_move in ["rock", "paper", "scissors"]


# test determine_winner returns the correct winner
def test_determine_winner():
    play = Play("rock")
    play.generate_move = lambda: "scissors"
    assert play.determine_winner() == "user"
    play.generate_move = lambda: "paper"
    assert play.determine_winner() == "computer"
    play.generate_move = lambda: "rock"
    assert play.determine_winner() == "tie"
