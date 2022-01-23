# python3

import sys
import threading


def node_height(index, heights):
    parent_index = parents[index]
    if parent_index in heights:
        height = heights[parent_index]
    elif parent_index == -1:
        height = 1
    else:
        height = node_height(parent_index, heights) + 1
    heights[parent_index] = height
    return height

def compute_height(n, parents):
    global heights
    heights = dict()
    height = 0
    for index in range(n):
        curr_height = node_height(index, heights)
        height = max(curr_height, height)

    return height

def main():
    global parents
    n = int('5')
    parents = list(map(int, '4 -1 4 1 1'.split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
