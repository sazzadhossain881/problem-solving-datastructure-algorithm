def isMonotonic(nums):
    isNonDecreasig = True
    isNonIncreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            isNonDecreasig = False
        
        if nums[i] > nums[i-1]:
            isNonIncreasing = False
    
    return isNonDecreasig or isNonIncreasing

print(isMonotonic([1,1,1,2,3,4,3,4,5]))
