def solution(num_list):
    res = 0
    for n in num_list:
        cnt = 0
        while n > 1:
            if n % 2:
                n = (n - 1) / 2
            else:
                n /= 2
            cnt += 1
        res += cnt
    return res

