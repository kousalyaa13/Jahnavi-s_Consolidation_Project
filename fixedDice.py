# Determines if any two values rolled are equal to eachother or else it will just return the set if its not a fixed roll

def fixed_dice(roll):
    if roll[0] == roll[1]:
        return {0, 1}
    elif roll[1] == roll[2]:
        return {1, 2}
    elif roll[0] == roll[2]:
        return{0, 2}
    else:
        return set()