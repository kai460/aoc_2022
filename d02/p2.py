WIN = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

SHAPE = {
    "rock" : 1,
    "paper" : 2,
    "scissor" : 3
}

OUTCOME = {
    "A X" : WIN["X"] + SHAPE["scissor"],
    "A Y" : WIN["Y"] + SHAPE["rock"],
    "A Z" : WIN["Z"] + SHAPE["paper"],
    "B X" : WIN["X"] + SHAPE["rock"],
    "B Y" : WIN["Y"] + SHAPE["paper"],
    "B Z" : WIN["Z"] + SHAPE["scissor"],
    "C X" : WIN["X"] + SHAPE["paper"],
    "C Y" : WIN["Y"] + SHAPE["scissor"],
    "C Z" : WIN["Z"] + SHAPE["rock"],
}

def calculate_score():
    score = 0
    with open("d2/d2_input.txt") as file:
        input = file.read()
        strategy = input.split('\n')

        score = sum(OUTCOME[s] for s in strategy if s in OUTCOME)

    return score

if __name__ == "__main__":
    print(calculate_score())