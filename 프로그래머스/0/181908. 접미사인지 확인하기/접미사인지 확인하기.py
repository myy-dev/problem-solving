def solution(my_string, is_suffix):
    suffixs = {}
    for i in range(len(my_string)):
        suffixs[my_string[i:]] = 1
    return suffixs.get(is_suffix, 0)
