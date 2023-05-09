import sys
import fileFunctions as Ff
import State as St
import Algorithms as Al



algorithms = {"dfs": Al.DFS, "bfs": Al.BFS, "astr": {"manh": Al.Manh, "hamm": Al.Hamm}}

if __name__ == '__main__':

    try:
        algorithm = algorithms[sys.argv[1]]

        St.order = sys.argv[2]

        filename1 = sys.argv[3]

        filename2 = sys.argv[4]

        filename3 = sys.argv[5]
    except:
        print("ERROR")

    if type(algorithm) == dict:
        algorithm = algorithm[St.order]
        St.order = "RLDU"

    St.ideal_State, currentState, zeroLoc = Ff.readFile(f"{filename1}")

    s1 = St.State(currentState, "", zeroLoc, 0, "")

    final, vis, cal, depth, time = algorithm(s1)

    moves = None
    size = 0
    if final is not None:
        moves = final.movearr
        size = len(moves)
    Ff.saveFirstFile(moves, filename2)
    Ff.saveSecondFile(size, vis, cal, depth, time, filename3)
