d = {}

def has_negatives(a):
    """
    YOUR CODE HERE
    """

    result = []
    #get all positive int added to a dict
    for i in a:
        if i >= 0:
            d[i] = i
    #compare negative values in a to keys in dict
    for i in a:
        if i < 0:
            if abs(i) in d:
                result.append(abs(i))

    return result


# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


print(has_negatives([-1,-2,1,2,3,4,-4]))
