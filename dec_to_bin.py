def dec_to_bin(number):
    bin = ''
    binArr = []
    while number > 0:
        remainder = number % 2
        number = number // 2
        binArr.append(str(remainder))
    return bin.join(binArr[::-1])
