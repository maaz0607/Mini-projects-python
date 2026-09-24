# Number Guessing Game

A command-line number guessing game built in Python, with difficulty levels, a guess limit, and a replay system. This was my first Python project, built to learn core language fundamentals hands-on rather than through tutorials.

## How to Play

1. Run the script:
   ```
   python guessing_game.py
   ```
2. Choose whether to play (`Y`/`N`).
3. Pick a difficulty:
   - **1 — Easy**: guess a number between 0–2, 3 tries
   - **2 — Medium**: guess a number between 0–5, 6 tries
   - **3 — Hard**: guess a number between 0–10, 11 tries
4. Keep guessing — you'll be told if your guess is too high or too low.
5. Guess correctly before you run out of tries to win.
6. After the round ends, choose to play again or exit.

## Features

- **Input validation** — rejects non-numeric and invalid input without crashing, and re-prompts instead
- **Difficulty levels** — sets the guessing range and guess limit automatically based on your choice
- **Guess cap** — the game ends in a loss if you run out of tries before guessing correctly
- **Replay loop** — play as many rounds as you want without restarting the script
- **Clean exit handling** — using `sys.exit()` to end the program properly from anywhere in the game

## What I Learned Building This

- Structuring logic with functions (`def`) and understanding why functions must be defined before they're called
- `while True` loops combined with `break`/`continue` for repeatable, validated input
- The difference between `.isdigit()` and other validation approaches, and its limitations with negative numbers
- String slicing (`[0]`, `[1:]`) vs indexing, and how to combine conditions with `and`/`or`
- Variable scope — when a value needs `return` vs when it can stay local to a function
- Debugging by tracing code line-by-line against specific test inputs, rather than guessing at fixes
- The difference between `quit()`/`exit()` (interactive-shell-only) and `sys.exit()` (the correct way to end a script from code)

## Possible Future Improvements

- Refactor difficulty settings into a dictionary instead of if/elif branches
- Add a "hint" system based on how close recent guesses are
- Track and display best scores across rounds
