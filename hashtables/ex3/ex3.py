def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    storage = {}
    for idx in arrays:
        for i in idx:
            if i not in storage:
                storage[i] = 0
            else:
                storage[i] += 1
    result = []
    for key in storage:
        if storage[key] == len(arrays) - 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
