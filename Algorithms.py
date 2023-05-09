import State as St
from queue import PriorityQueue
import time


# def DFS(st, visited, calculated):
#     visited += 1
#     if St.checkState(st.state):
#         print("ŁOT")
#         return st, visited, calculated
#     if st.deep > 19:
#         return None, visited, calculated
#     st.createChildren()
#     calculated += len(st.children)
#     for i in st.children:
#         helps, visited, calculated = DFS(i, visited, calculated)
#         if helps is not None:
#             return helps, visited, calculated
#     return None, visited, calculated


def BFS(st):
    calculatedStates = 0
    visitedStates = 0
    queue = [st]
    maxDeep = 0
    start = time.time()
    end = time.time()
    while True:
        node = queue.pop(0)
        if node.deep > maxDeep:
            maxDeep = node.deep
        visitedStates += 1
        if St.checkState(node.state):
            return node, visitedStates, calculatedStates, maxDeep, end - start
        if end - start > 20:
            return None, visitedStates, calculatedStates, maxDeep, end - start
        node.createChildren()
        calculatedStates += len(node.children)
        for i in node.children:
            queue.append(i)
        end = time.time()


def DFS(st):
    calculatedStates = 0
    visitedStates = 0
    queue = [st]
    maxDeep = 0
    start = time.time()
    end = time.time()
    while len(queue) > 0:
        node = queue.pop(-1)
        if node.deep > maxDeep:
            maxDeep = node.deep
        visitedStates += 1
        if St.checkState(node.state):
            return node, visitedStates, calculatedStates, maxDeep, end - start
        if end - start > 20:
            return None, visitedStates, calculatedStates, maxDeep, end - start
        if node.deep == 20:
            continue
        node.createChildren()
        calculatedStates += len(node.children)
        for i in reversed(node.children):
            queue.append(i)
        end = time.time()
    return None, visitedStates, calculatedStates, maxDeep


# def Hamm(st):
#     calculatedStates = 0
#     visitedStates = 0
#     node = st
#     start = time.time()
#     while True:
#         visitedStates += 1
#         if St.checkState(node.state):
#             return node, visitedStates, calculatedStates
#         end = time.time()
#         if end - start > 20:
#             return None, visitedStates, calculatedStates
#         node.createChildren()
#         calculatedStates += len(node.children)
#         index = 0
#         minimum = 0
#         iteration = 0
#         for i in node.children:
#             i.calculateHamm()
#             if iteration == 0:
#                 minimum = i.hamm
#                 index = iteration
#             else:
#                 if i.hamm < minimum:
#                     minimum = i.hamm
#                     index = iteration
#             iteration += 1
#         node = node.children[index]
#
#
# def Manh(st):
#     calculatedStates = 0
#     visitedStates = 0
#     node = st
#     start = time.time()
#     while True:
#         visitedStates += 1
#         if St.checkState(node.state):
#             return node, visitedStates, calculatedStates
#         end = time.time()
#         if end - start > 20:
#             return None, visitedStates, calculatedStates
#         node.createChildren()
#         calculatedStates += len(node.children)
#         index = 0
#         minimum = 0
#         iteration = 0
#         for i in node.children:
#             i.calculateManh()
#             if iteration == 0:
#                 minimum = i.manh
#                 index = iteration
#             else:
#                 if i.manh < minimum:
#                     minimum = i.manh
#                     index = iteration
#             iteration += 1
#         node = node.children[index]


def Hamm(st):
    calculatedStates = 0
    visitedStates = 0
    node = st
    q = PriorityQueue()
    maxDeep = 0
    start = time.time()
    end = time.time()
    while True:
        visitedStates += 1
        if node.deep > maxDeep:
            maxDeep = node.deep
        if St.checkState(node.state):
            return node, visitedStates, calculatedStates, maxDeep, end - start
        if end - start > 20:
            return None, visitedStates, calculatedStates, maxDeep, end - start
        node.createChildren()
        node.calculateHamm()
        calculatedStates += len(node.children)
        for i in node.children:
            i.calculateHamm()
            q.put(St.PrioritizedItem(i.compare, i))
        node = q.get().item
        end = time.time()


def Manh(st):
    calculatedStates = 0
    visitedStates = 0
    node = st
    q = PriorityQueue()
    maxDeep = 0
    start = time.time()
    end = time.time()
    while True:
        visitedStates += 1
        if node.deep > maxDeep:
            maxDeep = node.deep
        if St.checkState(node.state):
            return node, visitedStates, calculatedStates, maxDeep, end - start
        if end - start > 20:
            return None, visitedStates, calculatedStates, maxDeep, end - start
        node.createChildren()
        node.calculateManh()
        calculatedStates += len(node.children)
        for i in node.children:
            i.calculateManh()
            q.put(St.PrioritizedItem(i.compare, i))
        node = q.get().item
        end = time.time()
