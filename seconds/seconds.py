def seconds(list_1):
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]
    result = []
    for i in range(len(list_1)):
        if (i+1) % 2 == 0:
            result.append(list_1[i])
    return result

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
