import State as St
from queue import PriorityQueue
import time

MAX_depht = 20
MAX_calculating_time = 20


def bfs(st):
    calculated_states = 0
    visited_states = 0
    queue = [st]
    max_depth = 0
    start = time.time()
    end = time.time()
    while True:
        node = queue.pop(0)
        if node.deep > max_depth:
            max_depth = node.deep
        visited_states += 1
        if St.check_state(node.state):
            return node, visited_states, calculated_states, max_depth, end - start
        if end - start > MAX_calculating_time:
            return None, visited_states, calculated_states, max_depth, end - start
        node.create_children()
        calculated_states += len(node.children)
        for i in node.children:
            queue.append(i)
        end = time.time()


def dfs(st):
    calculated_states = 0
    visited_states = 0
    queue = [st]
    max_depth = 0
    start = time.time()
    end = time.time()
    while len(queue) > 0:
        node = queue.pop(-1)
        if node.deep > max_depth:
            max_depth = node.deep
        visited_states += 1
        if St.check_state(node.state):
            return node, visited_states, calculated_states, max_depth, end - start
        if end - start > MAX_calculating_time:
            return None, visited_states, calculated_states, max_depth, end - start
        if node.deep == MAX_depht:
            continue
        node.create_children()
        calculated_states += len(node.children)
        for i in reversed(node.children):
            queue.append(i)
        end = time.time()
    return None, visited_states, calculated_states, max_depth


def hamm(st):
    calculated_states = 0
    visited_states = 0
    node = st
    q = PriorityQueue()
    max_depth = 0
    start = time.time()
    end = time.time()
    while True:
        visited_states += 1
        if node.deep > max_depth:
            max_depth = node.deep
        if St.check_state(node.state):
            return node, visited_states, calculated_states, max_depth, end - start
        if end - start > MAX_calculating_time:
            return None, visited_states, calculated_states, max_depth, end - start
        node.create_children()
        node.calculate_hamm()
        calculated_states += len(node.children)
        for i in node.children:
            i.calculate_hamm()
            q.put(St.PrioritizedItem(i.compare, i))
        node = q.get().item
        end = time.time()


def manh(st):
    calculated_states = 0
    visited_states = 0
    node = st
    q = PriorityQueue()
    max_depth = 0
    start = time.time()
    end = time.time()
    while True:
        visited_states += 1
        if node.deep > max_depth:
            max_depth = node.deep
        if St.check_state(node.state):
            return node, visited_states, calculated_states, max_depth, end - start
        if end - start > MAX_calculating_time:
            return None, visited_states, calculated_states, max_depth, end - start
        node.create_children()
        node.calculate_manh()
        calculated_states += len(node.children)
        for i in node.children:
            i.calculate_manh()
            q.put(St.PrioritizedItem(i.compare, i))
        node = q.get().item
        end = time.time()
