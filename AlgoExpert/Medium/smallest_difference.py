def smallest_differences(array1, array2):
    array1.sort()
    array2.sort()

    index_1 = 0
    index_2 = 0

    smallest = float("inf")
    current = float("inf")
    smallest_pair = []

    while index_1 < len(array1) and index_2 < len(array2):

        first_number = array1[index_1]
        second_number = array2[index_2]

        if first_number < second_number:
            current = second_number - first_number
            index_1 += 1
        
        elif second_number < first_number:
            current = first_number - second_number
            index_2 += 1
        
        else:
            return [first_number, second_number]
    
        if smallest > current:
            smallest = current
            smallest_pair = [first_number, second_number]
    
    return smallest_pair

print(smallest_differences([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

