def solution(myString, pat):
    if len(pat) > len(myString):
        return 0
    return int(pat.lower() in myString.lower())
