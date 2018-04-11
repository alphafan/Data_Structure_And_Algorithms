""" Hamming Distance """


def hammingDistance(num1, num2):
    num1, num2 = abs(num1), abs(num2)
    print('{}: {:b}'.format(num1, num1))
    print('{}: {:b}'.format(num2, num2))
    distance = 0
    while num1 or num2:
        if num1 ^ 1 != num2 ^ 1:
            distance += 1
        num1 = num1 >> 1
        num2 = num2 >> 1
    print(distance)
    return distance


hammingDistance(123, -4)

