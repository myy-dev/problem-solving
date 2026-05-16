def solution(num_list):
    return int("".join([str(e) for e in num_list if e % 2])) + int(
        "".join([str(e) for e in num_list if not e % 2])
    )