# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

file = open('1.txt', 'r')


def post_order(node):
    if node == -1:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.key, end=' ')


def pre_order(node):
    if node == -1:
        return
    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node == -1:
        return
    in_order(node.left)
    print(node.key, end=' ')
    in_order(node.right)


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
        root = self.nodes[0]
        in_order(root)
        print()

    def preOrder(self):
        root = self.nodes[0]
        pre_order(root)
        print()

    def postOrder(self):
        root = self.nodes[0]
        post_order(root)
        print()


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder()
    tree.preOrder()
    tree.postOrder()


threading.Thread(target=main).start()
