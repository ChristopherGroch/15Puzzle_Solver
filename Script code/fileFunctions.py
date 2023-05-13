import State as St


def read_file(path):
    with open(path, 'r') as f:
        line = f.readline()
        r = int(line.split()[0])
        c = int(line.split()[1])
        ideal_state = St.create_ideal_state(r, c)

        currentState = []
        for i in range(r):
            sublist = []
            line = f.readline()
            for j in range(c):
                sublist.append(int(line.split()[j]))
            currentState.append(sublist)

        zeroLoc = {'r': 0, 'c': 0}
        for i in range(len(currentState)):
            for j in range(len(currentState[i])):
                if currentState[i][j] == 0:
                    zeroLoc['r'] = i
                    zeroLoc['c'] = j
        return ideal_state, currentState, zeroLoc


def save_solution_file(moves, path):
    with open(path, 'w') as f:
        if moves is not None:
            if len(moves) != 0:
                f.write(f"{len(moves)}")
                f.write('\n')
                f.write(moves)
                return

        f.write('-1')


def save_info_file(moves_count, visited, calculated, depth, time, path):
    with open(path, 'w') as f:
        if moves_count is not None:
            if moves_count != 0:
                f.write(f"{moves_count}\n")
                f.write(f"{visited}\n")
                f.write(f"{calculated}\n")
                f.write(f"{depth}\n")
                f.write(f"{round(time * 1000, 3)}")
                return

        f.write('-1\n')
        f.write(f"{visited}\n")
        f.write(f"{calculated}\n")
        f.write(f"{depth}\n")
        f.write(f"{round(time * 1000, 3)}")
