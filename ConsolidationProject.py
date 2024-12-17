import random
import diceRoll
import tupleOut
import fixedDice
    
# This programs the process of whether or not the player should be allowed to reroll their turn depending on if they
# tupled out or rolled a fixed dice
def player_turn(player, scores):
    print(f"\nPlayer {player + 1}'s turn ==============================================================================================")
    roll = diceRoll.dice_roll()
    if_fixed = fixedDice.fixed_dice(roll)

    while True:
        print(f"Dice rolled: {roll}")

        if tupleOut.tuple_out(roll):
            print("You tupled out! Your score for this round is 0 :(")
            return 0
        
        if if_fixed:
            print(f"Fixed dice: {', '.join(str(roll[i]) for i in if_fixed)}")
        reroll_chance = input("\nDo you want to reroll? (yes/no): ").strip().lower()
        
        if reroll_chance == 'no':
            total_score = sum(roll)
            print(f"Scored {total_score} points")
            return total_score
        
        elif reroll_chance != 'yes':
            print("Invalid input, please enter 'yes' or 'no'.")
            continue
        
        for i in range(3):
            if i not in if_fixed: # reroll the unfixed dice
                roll[i] = random.randint(1, 6)
        if_fixed = fixedDice.fixed_dice(roll)

# This function keeps track of the players scores while saving past scores and updating them with each roll
def game(target_score):
    scores = [0, 0] # initialize score for two players
    current_player = 0

    while all(score < target_score for score in scores):
        print(f"\nScores: \nPlayer 1 = {scores[0]}, Player 2 = {scores[1]}")
        turn_score = player_turn(current_player, scores) # play turn
        scores[current_player] += turn_score # update score for the current player
        current_player = 1 - current_player # switch player

    winner = 1 if scores[0] >= target_score else 2
    print(f"\nFinal Scores: Player 1 = {scores[0]}, Player 2 = {scores[1]}")
    print(f"Player {winner} wins!")

# Initializing game. First to reach a specific goal (in this case 50) wins the game
game(target_score = 50)