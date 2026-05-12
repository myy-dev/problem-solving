def solution(arr, intervals):
    res = []
    for ai, bi in intervals:
        res.extend(arr[ai : bi + 1])
    return res

