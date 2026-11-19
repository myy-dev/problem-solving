def solution(code):
    ret = ""
    mode = 0
    for i, v in enumerate(code):
        if mode:
            if v == "1":
                mode = 0
            elif i % 2:
                ret += v
        else:
            if v == "1":
                mode = 1
            elif not i % 2:
                ret += v
    return ret or "EMPTY"