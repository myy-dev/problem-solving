def solution(myStr):
    split_arr = [
        e
        for e in myStr.translate(str.maketrans({"a": "X", "b": "X", "c": "X"})).split(
            "X"
        )
        if e
    ]
    return split_arr if split_arr else ["EMPTY"]
