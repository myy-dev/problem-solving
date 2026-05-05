def solution(strArr):
    return [v.lower() if not (i % 2) else v.upper() for i, v in enumerate(strArr)]
