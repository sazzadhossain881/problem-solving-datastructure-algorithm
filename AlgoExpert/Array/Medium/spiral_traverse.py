def spiral_traverse(array):
    result = []
    start_row, end_row = 0, len(array)-1
    start_col, end_col = 0, len(array[0])-1

    while start_row <= end_row and start_col <= end_col:

        for col in range(start_col, end_col):
            result.append(array[start_row][col])
        
        for row in range(start_row+1, end_col+1):
            result.append(array[row][end_col])
        
        for col in reversed(range(start_col, end_col)):
            result.append(array[end_row][col])
        
        for row in reversed(range(start_row+1, end_row+1)):
            result.append(array[row][start_col])

        start_row += 1
        end_row += 1
        start_col += 1
        end_col += 1
    
    return result

