def sort_nums(nums):
    left, mid, right = 0, 0, len(nums)-1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        
        elif nums[mid] == 1:
            mid += 1
        
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
    
    return nums

print(sort_nums([0, 1, 2, 0, 1, 2]))
