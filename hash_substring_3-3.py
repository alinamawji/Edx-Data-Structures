# python3

file = open('4.txt', 'r')


# p = subtext
# s = substrings of t
# t = original text
# p = 1000000007
# x = 263


def hash_text(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans


def pre_compute_hashes(text, subtext_len, p, x):
    text_len = len(text)
    arr_len = text_len - subtext_len + 1
    h = [None] * arr_len                                # length t - p + 1
    pos1 = text_len - subtext_len
    pos2 = text_len
    s = text[pos1:pos2]
    h[pos1] = hash_text(s, p, x)
    y = 1
    for j in range(1, subtext_len+1):
        y = (y * x) % p
    iter_range = text_len - subtext_len - 1
    for k in range(iter_range, -1, -1):
        h[k] = ( (x * h[k+1]) + (ord(text[k]) - (y * ord(text[k + subtext_len]))) ) % p
    return h


def rabin_karp(subtext, text):
    p = 1000000007
    x = 263
    text_len = len(text)
    subtext_len = len(subtext)
    arr_len = text_len - subtext_len - 1
    positions = list()
    pHash = hash_text(subtext, p, x)
    h = pre_compute_hashes(text, len(subtext), p, x)
    for i in range(text_len - subtext_len + 1):
        if pHash != h[i]:
            continue
        if text[i:(i + subtext_len)] == subtext:
            positions.append(i)
    return positions


def read_input():
    return (file.readline().rstrip(), file.readline().rstrip())


if __name__ == '__main__':
    res = ''
    for i in rabin_karp(*read_input()):
        res += str(i)
        res += ' '
    print(res)
