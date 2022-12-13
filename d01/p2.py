def get_3_most_calories():

    total = 0
    top = [0, 0, 0]
    min_idx = 0

    with open("d01/d1_input.txt") as file:

        calories = 0
        line = file.readline()

        # runs at O(n) time due to no sorting
        while True:

            while len(line.strip()) != 0:
                calories += int(line)
                line = file.readline()

            if top[min_idx] < calories:
                total += (calories - top[min_idx])
                top[min_idx] = calories
                min_idx = top.index(min(top)) # not happy with this line but whatever -- O(3)

            calories = 0
            line = file.readline()

            if len(line.strip()) == 0:
                break

    return total

if __name__ == "__main__":
    print(get_3_most_calories())