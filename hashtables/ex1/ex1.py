def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    w_s = {}
    for i in range(length):
        w2 = limit - weights[i]
        if w2 in w_s.keys():
            return (i,w_s[w2])
        w_s[weights[i]] = i

    return None
