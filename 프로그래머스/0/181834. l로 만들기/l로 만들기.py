def solution(myString):
    myString = list(myString)
    for i, v in enumerate(myString):
        if v < "l":
            myString[i] = "l"
    return "".join(myString)