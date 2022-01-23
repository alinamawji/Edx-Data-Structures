# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_index_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            opening_index_stack.append(i+1)
        elif next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            else:
                top = opening_brackets_stack.pop(len(opening_brackets_stack)-1)
                index = opening_index_stack.pop(len(opening_index_stack)-1)
                if not are_matching(top, next):
                    return i+1
        else:
            pass
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_index_stack.pop(len(opening_index_stack)-1)

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
