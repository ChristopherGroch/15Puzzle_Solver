import copy
from dataclasses import dataclass, field
from typing import Any

ideal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

order = "RLDU"


class State:

    def __init__(self, state, last_move, zero_loc, deep, move_sequence):
        self.deep = deep
        self.state = copy.deepcopy(state)
        self.move_sequence = copy.deepcopy(move_sequence)
        self.moves = good_moves(zero_loc, last_move)
        self.zero_loc = copy.deepcopy(zero_loc)
        self.children = None
        self.hamm = 0
        self.manh = 0
        self.compare = 0

    def create_children(self):
        self.children = []

        for i in self.moves:
            newZeroLoc = copy.deepcopy(self.zero_loc)
            newState = copy.deepcopy(self.state)
            move(newState, i, newZeroLoc)
            s = State(newState, i, newZeroLoc, self.deep + 1, self.move_sequence + i)
            self.children.append(s)

    def calculate_manh(self):
        manh = 0
        for i in range(len(ideal_state)):
            for j in range(len(ideal_state[i])):
                num = ideal_state[i][j]
                if num != 0:
                    for x in range(len(self.state)):
                        for y in range(len(self.state[x])):
                            if self.state[x][y] == num:
                                manh += abs(x - i) + abs(y - j)
        self.manh = manh
        self.compare = manh + self.deep

    def calculate_hamm(self):
        hamm = 0
        for i in range(len(ideal_state)):
            for j in range(len(ideal_state[i])):
                if self.state[i][j] != 0:
                    if ideal_state[i][j] != self.state[i][j]:
                        hamm += 1
        self.hamm = hamm
        self.compare = hamm + self.deep

    def __lt__(self, other):
        if self.compare < other.compare:
            return -1
        elif self.compare > other.compare:
            return 1
        else:
            return 0


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


def create_ideal_state(r, c):
    idealstate = []
    val = 1
    for i in range(r):
        subList = []
        for j in range(c):
            subList.append(val)
            val += 1
        idealstate.append(subList)
    idealstate[r - 1][c - 1] = 0

    return idealstate


def print_state(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            print(tab[i][j], end='       ')
        print()


def move(tab, way, zero_loc):
    x = zero_loc['r']
    y = zero_loc['c']

    if way == 'L':
        v = tab[x][y - 1]
        tab[x][y - 1] = 0
        tab[x][y] = v
        zero_loc['c'] -= 1
    elif way == 'R':
        v = tab[x][y + 1]
        tab[x][y + 1] = 0
        tab[x][y] = v
        zero_loc['c'] += 1
    elif way == 'U':
        v = tab[x - 1][y]
        tab[x - 1][y] = 0
        tab[x][y] = v
        zero_loc['r'] -= 1
    elif way == 'D':
        v = tab[x + 1][y]
        tab[x + 1][y] = 0
        tab[x][y] = v
        zero_loc['r'] += 1


def check_state(tab):
    return tab == ideal_state


def good_moves(cord, last_move):
    badMoves = ""
    if cord['r'] == 0:
        badMoves += 'U'
    if cord['r'] == 3:
        badMoves += 'D'
    if cord['c'] == 0:
        badMoves += "L"
    if cord['c'] == 3:
        badMoves += 'R'
    if last_move != "":
        if last_move == 'R':
            badMoves += 'L'
        elif last_move == "L":
            badMoves += 'R'
        elif last_move == 'U':
            badMoves += 'D'
        elif last_move == 'D':
            badMoves += 'U'

    properMoves = ""

    for i in order:
        if i in badMoves:
            continue
        properMoves += i

    return properMoves
