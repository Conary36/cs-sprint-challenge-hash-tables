def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    set_neg = set()
    for i in a:
        set_neg.add(i)
    for i in a:
        if(i > 0 and -1*i in set_neg):
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
