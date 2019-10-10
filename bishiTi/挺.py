import sys

[t, k] = list(map(int, sys.stdin.readline().strip().split()))
value = []
for _ in range(t):
    value.append(list(map(int, sys.stdin.readline().strip().split())))


def solution(a, b):
    res = 0
    for length in range(a, b + 1):
        res += fun(length)

    return res


def fun(length):
    res = 1
    pn = length // k
    for i in range(1, pn + 1):
        res += length - i * k + 1

    return res


if __name__ == "__main__":
    for i in range(t):
        print(solution(value[i][0], value[i][1]))