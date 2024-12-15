# Determines if the rolls are considered tupled out by seeing if each if the values rolled are all equal to eachother

def tuple_out(roll):
    return roll[0] == roll[1] == roll[2]