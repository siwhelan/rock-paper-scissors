# Rock, Paper, Scissors

## User Stories

    As a Maker
    So I can play Rock Paper Scissors
    I would like to enter my move on the home page
    And click to confirm my move (rock, paper or scissors)

    As a Maker
    So I can play Rock Paper Scissors
    I would like the opponent's move to be decided randomly by the program

    As a Maker
    So I can play Rock Paper Scissors
    I would like to see the result of the game on the next page

    As a Maker
    So I can play Rock Paper Scissors again
    I would like to click on a link on the result page
    So it takes me back to the home page



## Page: Home / Entry Form

### Request:
- GET /
- No parameters

### Response (200 OK):
- HTML view with form to enter move (rock, paper, or scissors) and a submit button.

---

## Page: Process Move

### Request:
- POST /play
- With parameters:
  - move="rock" (or "paper" or "scissors")

### Response (200 OK):
- HTML view with the user's move, the opponent's randomly decided move, and the result of the game.

---

## Page: Play Again

### Request:
- GET /play-again
- No parameters

### Response (200 OK):
- Redirect to the home page (GET /) to play another game.