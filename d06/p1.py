
# Kinda of a bad way of doing this
def find_marker_position():
    with open("d06/d6_input.txt") as file:
        line = file.readline()

        for i in range(4, len(line)):
            if len(line[i - 4 : i]) == len(set(line[i - 4 : i])):
                return i

    return -1

def find_start_of_msg():
    with open("d06/d6_input.txt") as file:
        line = file.readline()

        for i in range(14, len(line)):
            if len(line[i - 14 : i]) == len(set(line[i - 14 : i])):
                return i

    return -1

if __name__ == "__main__":
    print(find_start_of_msg())