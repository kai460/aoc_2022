
def get_prior(c):
    prior = ord(c.lower()) - ord('a') + 1
    if c == c.upper():
        return prior + 26
    return prior

def get_total_prior():
    total = 0

    with open("d3/d3_input.txt") as file:
        input = file.read()
        lines = input.split('\n')
        idx = 0

        while len(lines) - idx >= 3:
            l1, l2, l3 = lines[idx:idx + 3]
            idx += 3
            inter = set(l1) & set(l2) & set(l3)

            if len(inter) == 0:
                continue
            total += get_prior(next(iter(inter)))

    return total

if __name__ == "__main__":
    print(get_total_prior())
