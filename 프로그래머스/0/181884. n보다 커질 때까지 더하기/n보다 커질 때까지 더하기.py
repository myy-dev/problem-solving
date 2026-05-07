def solution(numbers, n):
    res = 0
    for e in numbers:
        res += e
        if res > n:
            return res
    return res
