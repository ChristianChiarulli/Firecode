def duplicate_items(list_numbers):
    seen = []
    ret = []
    for num in list_numbers:
        if num in seen:
            ret.append(num)
        seen.append(num)
    return ret
