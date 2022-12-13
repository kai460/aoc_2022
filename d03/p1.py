
def get_prior(c):
    prior = ord(c.lower()) - ord('a') + 1
    if c == c.upper():
        return prior + 26
    return prior

def get_total_prior():
    total = 0

    with open("d3/d3_input.txt") as file:
        line = file.readline()

        while len(line.split()) != 0:
            p1, p2 = line[:len(line) // 2], line[len(line) // 2:]
            inter = set(p1) & set(p2)

            if len(inter) == 0:
                continue

            total += get_prior(next(iter(inter)))

            line = file.readline()

    return total

if __name__ == "__main__":
    print(get_total_prior())
