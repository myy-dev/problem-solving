def solution(a, b, c, d):
    dices = sorted([a, b, c, d])
    if dices[0] == dices[3]:
        ans = 1111 * dices[0]
    elif dices[0] == dices[1] == dices[2]:
        ans = (10 * dices[0] + dices[3]) ** 2
    elif dices[1] == dices[2] == dices[3]:
        ans = (10 * dices[1] + dices[0]) ** 2
    elif dices[0] == dices[1] and dices[2] == dices[3]:
        ans = (dices[1] + dices[2]) * abs(dices[1] - dices[2])
    elif dices[0] == dices[1]:
        ans = dices[2] * dices[3]
    elif dices[1] == dices[2]:
        ans = dices[0] * dices[3]
    elif dices[2] == dices[3]:
        ans = dices[0] * dices[1]
    else:
        ans = dices[0]
    return ans
