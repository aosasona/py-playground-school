def split_nums(raw_num: str) -> list[int]:
    result = []
    if "," in raw_num:
        res = raw_num.split(",")
    elif " " in raw_num:
        res = raw_num.split(" ")
    else:
        raise Exception("Invalid characters")
    for val in res:
        sanitized = int(val.strip())
        if sanitized is None or sanitized == 0:
            continue
        result.append(sanitized)
    return result