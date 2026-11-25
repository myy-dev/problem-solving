def solution(arr):
    ans = 0
    flag = False
    while True:
        for i, v in enumerate(arr):
            if v >= 50 and not v % 2:
                arr[i] /= 2
                flag = True
            elif v < 50 and v % 2:
                arr[i] = arr[i] * 2 + 1
                flag = True
        if not flag:
            return ans
        ans += 1
        flag = False

