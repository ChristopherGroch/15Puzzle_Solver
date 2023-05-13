import os
import glob
import pandas as pd
import csv

files = glob.glob('[0-9]x[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]*.txt')
statFiles = []
for f in files:
    if len(f.split("")) == 6:
        if f.split("")[5] == 'stats.txt':
            statFiles.append(f)

with open("stat.csv", mode="w") as csvfile:
    features = ['Method', 'Order', 'Puzzle_length', 'Solution_length', 'Visited_states', 'Calculated_states',
                'Max_deep', 'Calculatingtime']
    writer = csv.DictWriter(csvfile, fieldnames=features)
    writer.writeheader()
    for f in statFiles:
        with open(f, mode='r') as currfile:
            method = f.split("")[3]
            order = f.split("")[4]
            puzzleLength = int(f.split("")[1][1])
            solutionLength = int(currfile.readline())
            visitedStates = int(currfile.readline())
            calculatedStates = int(currfile.readline())
            maxDeep = int(currfile.readline())
            calculatingTime = float(currfile.readline())
            writer.writerow({'Method': method, 'Order': order, 'Puzzle_length': puzzleLength, 'Solution_length':solutionLength, 'Visited_states': visitedStates, 'Calculated_states': calculatedStates,
                'Max_deep': maxDeep, 'Calculating_time': calculatingTime})