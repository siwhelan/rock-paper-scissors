from flask import Flask, render_template, request
import os
from lib.game import Play

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    user_input = request.form["weapon"]
    game = Play(user_input)
    winner = game.determine_winner()
    return render_template(
        "play.html",
        winner=winner,
        user_move=user_input,
        computer_move=game.computer_move,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
