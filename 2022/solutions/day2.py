# Rock = 1 point
# Paper = 2 points
# Scissors = 3 points

# A = Rock
# B = Paper
# C = Scissors

# loss = 0
# draw = 3
# win = 6

# Must follow strategy guide

def strategy_1(p1, p2):
    points = 0
    if p2 == 'X': # Rock
        points += 1
        if p1 == 'A': # Rock
            points += 3 
        elif p1 == 'B': # Paper
            points += 0 
        elif p1 == 'C': # Scissors
            points += 6 
    elif p2 == 'Y': # Paper
        points += 2
        if p1 == 'A': # Rock
            points += 6
        elif p1 == 'B': # Paper
            points += 3
        elif p1 == 'C': # Scissors
            points += 0
    elif p2 == 'Z': # Scissors
        points += 3
        if p1 == 'A': # Rock
            points += 0
        elif p1 == 'B': # Paper
            points += 6
        elif p1 == 'C': # Scissors
            points += 3

    return points

def strategy_2(p1, p2): 
    # X = you need to lose
    # Y = you need to draw
    # Z = you need to win
    points = 0
    if p1 == 'A': # rock
        if p2 == 'X': # lose w/ scissors
            points += 3 + 0
        elif p2 == 'Y': # draw w/ rock
            points += 1 + 3
        elif p2 == 'Z': # win w/ paper
            points += 2 + 6
    elif p1 == 'B': # paper
        if p2 == 'X': # lose with rock
            points += 1 + 0
        elif p2 == 'Y': # draw with paper
            points += 2 + 3
        elif p2 == 'Z': # win with scissors
            points += 3 + 6
    elif p1 == 'C': # scissors
        if p2 == 'X': # lose w/ paper
            points += 2 + 0
        elif p2 == 'Y': # draw with scissors
            points += 3 + 3
        elif p2 == 'Z': # win with rock
            points += 1 + 6
    return points

with open("../inputs/day2.txt") as f:
    total_points = 0
    for line in f:
        chars = [x for x in line]
        opp_play = chars[0]
        my_play = chars[2]
        print(f"opp_play: {opp_play}")
        print(f"my_play: {my_play}")
        pts = strategy_2(opp_play, my_play)
        print(f"Points for round: {pts}")
        total_points += pts
    print(total_points)




