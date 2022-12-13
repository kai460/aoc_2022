import re

def convert_to_int(f : list[str]) -> list[int]:
    return [int(e) for e in f]

# This question is awful
def rearrange_crates():

    with open("d5/d5_input.txt") as file:
        line = file.readline()
        crates = [[] for _ in range(9)]
        unparsed = []

        while line != " 1   2   3   4   5   6   7   8   9\n":
            unparsed.append(line)
            line = file.readline()

        for line in reversed(unparsed):
            for i in range(9):
                idx = 1 + i * 4
                if idx >= len(line):
                    continue
                if line[idx] != ' ':
                    crates[i].append(line[idx])

        file.readline()

        line = file.readline()

        while len(line.split()) != 0:

            # I should really learn regex
            no, src, dst = convert_to_int(re.findall("move (\d+) from (\d+) to (\d+)", line)[0])
            src, dst = src - 1, dst - 1

            crates[dst].extend(reversed(crates[src][-no:]))
            crates[src] = crates[src][:-no]

            line = file.readline()

        return ''.join(c[-1] for c in crates)

if __name__ == "__main__":
    print(rearrange_crates())