def add(bit1, bit2):
    carry = 0
    result = []
    i = len(bit1) - 1
    j = len(bit2) - 1
    while i >= 0 or j >= 0:
        # Move from back to front
        if i < 0:
            num1 = 0
            num2 = bit2[j]
        elif j < 0:
            num1 = bit1[i]
            num2 = 0
        else:
            num1 = bit1[i]
            num2 = bit2[j]
        # Get value at this position
        # value = num1 + num2 + carry
        value = num1 ^ num2
        value = value ^ carry
        result.append(value)
        # Get carry at this position
        if carry == 0:
            carry = num1 & num2
        else:
            carry = num1 | num2
        i -= 1
        j -= 1
        print(carry)
    if carry == 1:
        result.append(carry)
    return result[::-1]


a = [1, 1, 1]
b = [1, 0]
print(add(a, b))
