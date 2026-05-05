def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    res = 1
    for e in num_list:
        res *= e
    return res