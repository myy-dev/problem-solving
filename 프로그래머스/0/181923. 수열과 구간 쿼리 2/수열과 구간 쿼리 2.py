def solution(arr, queries):
    ans = []
    for s, e, k in queries:
        ans.append(min([i for i in arr[s : e + 1] if i > k], default=-1))
    return ans