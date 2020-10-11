d = {}

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    #iterate through each arr of matrix
    for i in range(len(arrays)-1):
        for j in arrays[i]:


    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
