def move_negative(nums):
    new_nums = []

    for i in nums:
        if i < 0:
            new_nums.append(i)
    
    for i in nums:
        if i >= 0:
            new_nums.append(i)
    
    return new_nums



print(move_negative([-12, 11, -13, -5, 6, -7, 5, -3, -6]))

