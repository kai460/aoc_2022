
# A bit cheesy
SHAPE = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

OUTCOME = {
    "A X" : SHAPE["X"] + 3,
    "A Y" : SHAPE["Y"] + 6,
    "A Z" : SHAPE["Z"],
    "B X" : SHAPE["X"],
    "B Y" : SHAPE["Y"] + 3,
    "B Z" : SHAPE["Z"] + 6,
    "C X" : SHAPE["X"] + 6,
    "C Y" : SHAPE["Y"],
    "C Z" : SHAPE["Z"] + 3
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