def valid_subsequence(arr, sequence):
    sequence_index = 0

    for value in arr:
        if sequence_index == len(sequence):
            break
        
        if sequence[sequence_index] == value:
            sequence_index += 1
    
    return sequence_index == len(sequence)


result = valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, -1, 10])
print(result)
