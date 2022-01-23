# python3


def sift_down(i, n, data, swaps):
    smallest = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n and data[l] < data[smallest]:
        smallest = l
    if r < n and data[r] < data[smallest]:
        smallest = r
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        sift_down(smallest, n, data, swaps)

    return swaps


def sift_up(i, data, swaps):
    parent = int((i+1) / 2) - 1
    if i > 0 and data[parent] > data[i]:
        swaps.append((parent, i))
        data[i], data[parent] = data[parent], data[i]
        sift_up(parent, data, swaps)
    return swaps


def get_height(i):
    found_height = False
    if i == 1:
        found_height = 0
        return found_height
    else:
        lower_bound = 2
        upper_bound = 3
        current_height = 1
        while found_height is False:
            if lower_bound <= i <= upper_bound:
                found_height = current_height
                return found_height
            else:
                current_height += 1
                lower_bound = upper_bound + 1
                upper_bound += (2 ** current_height) - 1


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)
    for i in range(int(n/2), -1, -1):
        swaps = sift_down(i, n, data, swaps)
    return swaps


def main():
    file = open("test2.txt", "r")
    n = int(file.readline())
    data = list(map(int, file.readline().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
