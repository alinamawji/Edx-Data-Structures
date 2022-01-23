# python3

import sys


file = open('2.txt', 'r')


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        substring = self.s[i:j + 1]
        self.s = self.s[:i] + self.s[j + 1:]
        if k == 0:
            self.s = substring + self.s
        else:
            self.s = self.s[:k] + substring + self.s[k:]


rope = Rope(file.readline().strip())
q = int(file.readline())
for _ in range(q):
    i, j, k = map(int, file.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
