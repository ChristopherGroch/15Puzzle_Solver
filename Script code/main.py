import sys
import fileFunctions as Ff
import State as St
import Algorithms as Al

algorithms = {"dfs": Al.dfs, "bfs": Al.bfs, "astr": {"manh": Al.manh, "hamm": Al.hamm}}

if __name__ == '__main__':

    algorithm = None
    state_file = None
    solution_file = None
    info_file = None

    try:
        algorithm = algorithms[sys.argv[1]]

        St.order = sys.argv[2]

        state_file = sys.argv[3]

        solution_file = sys.argv[4]

        info_file = sys.argv[5]
    except:
        print("ERROR")

    if type(algorithm) == dict:
        algorithm = algorithm[St.order]
        St.order = "RLDU"

    St.ideal_state, currentState, zeroLoc = Ff.read_file(f"{state_file}")

    s1 = St.State(currentState, "", zeroLoc, 0, "")

    final, vis, cal, depth, time = algorithm(s1)

    moves = None
    size = 0
    if final is not None:
        moves = final.move_sequence
        size = len(moves)
    Ff.save_solution_file(moves, solution_file)
    Ff.save_info_file(size, vis, cal, depth, time, info_file)
