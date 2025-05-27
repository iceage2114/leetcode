def addBinary(a, b):

    lena = len(a) - 1
    lenb = len(b) - 1
    carry = 0
    result = []

    while lena >= 0 or lenb >= 0 or carry:
        sum_val = carry

        if lena >= 0:
            sum_val += int(a[lena])
            lena -= 1
        if lenb >= 0:
            sum_val += int(b[lenb])
            lenb -= 1

        result.append(str(sum_val % 2))
        carry = sum_val // 2

    return ''.join(reversed(result))


a = "1010"
b = "1011"

print(addBinary(a,b))
