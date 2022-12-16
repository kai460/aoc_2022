
def parse_ls(file, dir : dict[object]) -> str:

    line = file.readline().strip('\n')

    while len(line.split()) != 0 and line[0] != '$':
        type, name = line.split(' ', 2)

        if type != "dir":
            dir[name] = int(type)
        else:
            dir[name] = {".." : dir}

        line = file.readline().strip('\n')

    return line


# what the actual ???
def parse_disk():

    f = {}
    f[".."] = f     # the .. of / is still /
    cur = f

    with open("d07/d7_input.txt") as file:

        _ = file.readline() # ignore first line

        line = file.readline().strip('\n')

        while len(line.split()) != 0:

            # I kinda hate python tbh
            if line[:4] == "$ cd":
                dst = line[5:]

                if dst not in cur:
                    cur[dst] = {".." : cur}

                cur = cur[dst]
                line = file.readline().strip('\n')
            elif line[:4] == "$ ls":
                line = parse_ls(file, cur)

    return f

_total = {}
_hm = 0
_hmmmm = 41735494

def calculate_size(dir : dict[object], name : str, thres=100000, thres2=30000000-28264506):
    global _total, _hm, _hmmmm

    total = 0

    for k, v in dir.items():
        if k == "..":
            continue

        if isinstance(v, dict):
            if "total" not in v:
                calculate_size(v, k)
            total += v["total"]
        else:
            total += v

    dir["total"] = total

    if total <= thres:
        _total[name] = total
        _hm += total

    # honestly dumping everything into a list is probably easier
    if total >= thres2:
        print(total)
        _hmmmm = min(_hmmmm, total)

if __name__ == "__main__":

    dir = parse_disk()
    print(dir)

    calculate_size(dir, '\\')

    print(_total)
    print(_hm)
    print(_hmmmm)
    print(dir["total"])