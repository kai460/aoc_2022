# mis-interpreted the question so...

def convert_to_int(f : list[str]) -> list[int]:
    return [int(e) for e in f]

def get_contain():

    overlaps = 0

    with open("d4/d4_input.txt") as file:
        line = file.readline()

        while len(line.split()) != 0:
            p1, p2 = line.split(',', 2)
            d11, d12 = convert_to_int(p1.split('-', 2))
            d21, d22 = convert_to_int(p2.split('-', 2))

            overlaps += max(0, min(1, min(d12, d22) - max(d11, d21) + 1))
            line = file.readline()

    return overlaps

if __name__ == "__main__":
    print(get_contain())