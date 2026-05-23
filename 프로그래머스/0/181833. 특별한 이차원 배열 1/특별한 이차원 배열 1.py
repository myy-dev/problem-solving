def solution(n):
    return [[0 if r != c else 1 for c in range(n)] for r in range(n)]
