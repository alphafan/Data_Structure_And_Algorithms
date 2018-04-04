""" Knapsack Problem """


# Weights : [5, 1, 4, 7, 3]
# Values  : [1, 5, 9, 2, 7]
# maxWeight = 12
# maxValue ?


# Recursive Method

def knapsack(weights, values, capacity):
    maxValue = knapsackHelper(weights, values, capacity, 0)
    return maxValue


def knapsackHelper(weights, values, capacity, currentValue):
    if capacity <= 0:
        return 0
    if len(weights) == 0 or len(values) == 0:
        return currentValue
    # choose to take the last item
    res1 = knapsackHelper(weights[:-1], values[:-1],
                          capacity - weights[-1],
                          currentValue + values[-1])
    # not choose last item
    res2 = knapsackHelper(weights[:-1], values[:-1],
                          capacity,
                          currentValue)
    return max(res1, res2)

# Dynamic Programming


# Weights : [5, 1, 4, 7, 3]
# Values  : [1, 5, 9, 2, 7]
# maxWeight = 12
# maxValue ?


def knapsackDp(weights, values, capacity):
    numItems = len(weights)
    cache = [[0 for _ in range(capacity + 1)] for _ in range(numItems + 1)]
    for i in range(1, numItems + 1):
        for j in range(1, capacity + 1):
            if j >= weights[i - 1]:
                # Take this item
                value1 = values[i - 1] + cache[i - 1][j - weights[i - 1]]
                value2 = cache[i - 1][j]
                cache[i][j] = max(value1, value2)
            else:
                cache[i][j] = cache[i - 1][j]
    for row in cache:
        print(row)
    return cache[-1][-1]


weights = [5, 1, 4, 7, 3]
values = [1, 5, 9, 2, 7]
maxWeight = 12
print(knapsack(weights, values, maxWeight))

weights = [5, 1, 4, 7, 3]
values = [1, 5, 9, 2, 7]
maxWeight = 12
print(knapsackDp(weights, values, maxWeight))
