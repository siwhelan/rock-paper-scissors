from lib.game import *


def test_play_takes_user_input():
    play = Play("rock")
    assert play.user_input == "rock"


# test generate_move generates a random move for the computer
def test_generate_move():
    play = Play("rock")
    computer_move = play.generate_move()
    assert computer_move in ["rock", "paper", "scissors"]


# test determine_winner returns the correct winner
def test_determine_winner():
    play = Play("rock")
    # Mock generate_move to set computer_move to "scissors"
    play.generate_move = (
        lambda: setattr(play, "computer_move", "scissors") or "scissors"
    )
    assert play.determine_winner() == "user"
