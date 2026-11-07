# Letter by Letter

A word guessing game for the terminal, written in Python.

The game picks a random word. You guess one letter at a time. Correct
letters appear on the board, and every wrong guess costs one attempt.
Guess the whole word before you run out of attempts to win.

## Features

- Three difficulty levels (easy, medium, hard), each with its own
  word list and number of attempts
- One hint per game: type `?` to reveal a letter on the board
- Input checks: only single letters are accepted, and repeated
  guesses don't cost an attempt
- Win and loss messages that show the word
- Play again option after every game

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. In the project folder, run:

   python word_guess.py

## How to play

1. Choose a difficulty: easy, medium or hard.
2. Type one letter at a time and press Enter.
3. Type `?` once per game to reveal a letter.
4. After the game, type `y` to play again or `n` to quit.

| Difficulty | Word length   | Attempts |
|------------|---------------|----------|
| Easy       | 5-6 letters   | 3        |
| Medium     | 7-9 letters   | 7        |
| Hard       | 10-14 letters | 10       |

## What I practiced

- Loops, conditionals, lists and strings
- Functions
- The `random` module
- Exception handling with `try` / `except`
- Git and GitHub

## To do

- Web version with Streamlit (`app.py`, in progress)
- Write pytest tests
