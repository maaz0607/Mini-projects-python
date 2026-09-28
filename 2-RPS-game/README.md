# Rock Paper Scissors Lizard Spock

A command-line Rock Paper Scissors game in Python, extended with Lizard and Spock and a "first to N wins" match mode. This was my second Python project, built to practice dictionaries, loop control, and clean decision logic.

## How to Play

1. Run the script:
   ```
   python rock_paper_scissors.py
   ```
2. Enter how many wins are needed to take the match (e.g. `3` for first to 3).
3. Each round, type `rock`, `paper`, `scissors`, `lizard`, or `spock`. Type `quit` to leave at any time.
4. The computer picks a move at random, and the round result and running score are shown.
5. The first player to reach the target number of wins takes the match. The final score is shown when the game ends, whether by a match win or by quitting.

## Rules

- Scissors cuts paper and decapitates lizard
- Paper covers rock and disproves Spock
- Rock crushes scissors and crushes lizard
- Lizard poisons Spock and eats paper
- Spock smashes scissors and vaporizes rock
- Same move from both sides is a tie: no points, and the round doesn't count toward either score

## Features

- **First-to-N match mode**: the winning target is chosen at the start of each game
- **Five moves, one lookup table**: a dictionary maps each move to the moves it beats, so all the win rules live in one place
- **Explicit tie handling**: ties are checked first and never counted as a loss
- **Input validation**: invalid moves and invalid match targets show a message and ask again, without crashing or costing a round

## What I Learned Building This

- Using a dictionary with lists as values to replace a long chain of `and`/`or` win conditions
- Keeping one source of truth: the dictionary's keys double as the list of valid moves, so adding a move means editing one place
- `continue` to skip the rest of a loop pass on invalid input, versus `break` to leave the loop entirely
- Ordering `if/elif` checks deliberately: tie first, then win, then loss
- Debugging syntax errors from a broken `if/elif` chain (a normal statement in the middle of the chain ends it)
- Renaming variables for readability (`u_wins` to `user_wins`) so the code reads without decoding

## Possible Future Improvements

- Play multiple matches in a row with a replay option
- Track win streaks across rounds
- Build the input prompt from the dictionary so it updates automatically when moves are added
- Wrap the game in a `main()` function
