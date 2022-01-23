#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size


file = open('1.txt', 'r')
return_list = list()


class Node:
    def __init__(self, key):
        self.key = key
        self.left = -1
        self.right = -1

    def update_left_node(self, left_node):
        self.left = left_node

    def update_right_node(self, right_node):
        self.right = right_node


class TreeOrders:
    def read(self):
        self.n = int(file.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, file.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

        self.nodes = list()
        for i in range(self.n):
            node = Node(self.key[i])
            self.nodes.append(node)

        key = 0
        for node in self.nodes:
            if self.left[key] != -1:
                node.update_left_node(self.nodes[self.left[key]])
            if self.right[key] != -1:
                node.update_right_node(self.nodes[self.right[key]])
            key += 1

    def inOrder(self):
        if len(self.nodes) == 0:
            return
        root = self.nodes[0]
        in_order(root)


def in_order(node):
    if node == -1:
        return
    in_order(node.left)
    return_list.append(node.key)
    in_order(node.right)


def is_binary_search_tree():
    if len(return_list) == 0:
        return True
    for i in range(len(return_list)-1):
        if return_list[i] > return_list[i+1]:
            return False
    return True


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder()
    if is_binary_search_tree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
