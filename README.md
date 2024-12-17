# Tuple Out Dice Game

## Rules

### Objective
- Players aim to score the most points or reach the target score (default is 50).

### Gameplay
1. Players take turns rolling three dice.
2. Special rules for dice rolls:
   - **Tuple Out**: If all three dice show the same value, the player "tuples out" and ends their turn with 0 points.
   - **Fixed Dice**: If two dice show the same value, they are "fixed" and cannot be rerolled.
3. Players can reroll unfixed dice as many times as they like or stop to lock in their score.

### Turn End
- If a player stops voluntarily, their score for the turn is the sum of all three dice.
- If a player "tuples out," their score for the turn is 0.

---

## Game Instructions

### Running the Game
1. Save the Python script to a file (e.g., `ConsolidationProject.py`).
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python dice_game.py
### Example Gameplay
1. Player 1 rolls: `(3, 3, 5)`
- Two dice are the same, so the player can reroll the unfixed dice.
- Player 1 chooses to reroll the 5.
2. Player 1 rerolls: `(3, 3, 4)`
- Player 1 decides to stop and locks in the score for the turn: `3 + 3 + 4 = 10`.

Repeat for the next players until someone reaches the target score!