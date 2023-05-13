# 15Puzzle_Solver


## Table of contents
* [General info](#general-info)
* [main.py](#main)
* [statCombiner.py](#statsCombiner)
* [Stats.ipynb](#stats)

<a name="general-info"/>

### General info
Project was written as a school project. The goals of it were to create script which finds 15-Puzzle's solutions using three different state space search algorithms and then to explore how these algorithms behave. Projects contains three core files (two of them are .py scripts and the third one is a jupyter notebook file, more details below) and other files which contain needed functions and class with its methods.

<a name="main"/>

### main.py
Main.py is the most important script. It starts solution finder. This program takes five positional arguments:
* algorithm - there are three implemented algorithms: Breadth-first search ('bfs'), Depth-first search ('dfs') and A star ('astr')
* search order/heuristic function - it says which move will be checked first. If chosen algorithm is dfs or bfs, this argument takes permutation of 'RLDU' letters (which stands for R-right, L-left, D-down, U-up). If chosen algorithms is astr, this argument takes 'hamm' (Hamming metric) or 'manh' (Manhattan metric)
* name of file containing starting state - starting_state.txt file shows how that file should look like
* name of file where solution will be saved - solution.txt file shows what that file will contain
* name of file where stats will be saved - stats.txt file shows what that file will contain


Example of how to run this script:
<img width="724" alt="Zrzut ekranu 2023-05-9 o 18 01 12" src="https://github.com/ChristopherGroch/15Puzzle_Solver/assets/93371629/c203cbd3-2c31-4af8-abf5-63ec1ca24fc1">

<a name="statsCombiner"/>

### statsCombiner.py
StatsCombiner.py script looks for every text file located in current folder containing solution statistics. It saves all matching files' content in .csv file. 

<a name="stats"/>

### Stats.ipynb
This file uses .csv file prepared by statsCombiner.py to prepare useful graphs and tables.
