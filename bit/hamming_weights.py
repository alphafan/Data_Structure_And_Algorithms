""" Number of 1 Bits """

def hammingWeights(number):
    print('{}: {:b}'.format(number, number))
    count = 0
    while number:
        count += number & 1
        number = number >> 1
    print(count)
    return count


hammingWeights(123)

