
def get_most_calories():

    max_calories = (0, 0)

    with open("d01/d1_input.txt") as file:

        elf, calories = 1, 0
        line = file.readline()

        # runs at O(n) time due to no sorting
        while True:

            while len(line.strip()) != 0:
                calories += int(line)
                line = file.readline()

            max_calories = max(max_calories, (calories, elf))

            elf, calories = elf + 1, 0

            line = file.readline()

            if len(line.strip()) == 0:
                break

    return max_calories

if __name__ == "__main__":
    print(get_most_calories())