def peak_element(array):
    longestpeakelement = 0
    i = 1

    while i < len(array)-1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue

        leftIndex = i-2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1
        
        rightIndex = i+2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex-1]:
            rightIndex += 1
        
        currentpeakelement = rightIndex - leftIndex - 1
        longestpeakelement = max(longestpeakelement, currentpeakelement)
        i = rightIndex
    
    return longestpeakelement

print(peak_element([2,1,4,7,3,2,5]))

