import State as St


def readFile(path):
    with open(path, 'r') as f:
        line = f.readline()
        r = int(line.split()[0])
        c = int(line.split()[1])
        idealstate = St.createIdealState(r, c)

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
        return idealstate, currentState, zeroLoc


def saveFirstFile(moves, path):
    with open(path, 'w') as f:
        if moves is not None:
            if len(moves) != 0:
                f.write(f"{len(moves)}")
                f.write('\n')
                f.write(moves)
                return

        f.write('-1')


def saveSecondFile(movesCount, visited, calculated, depth, time, path):
    with open(path, 'w') as f:
        if movesCount is not None:
            if movesCount != 0:
                f.write(f"{movesCount}\n")
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
