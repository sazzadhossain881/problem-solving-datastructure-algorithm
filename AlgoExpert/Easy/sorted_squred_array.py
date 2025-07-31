def sorted_squred(nums):
   sorted_squred = [0 for _ in nums]
   print(sorted_squred)

   smaller_index = 0
   larger_index = len(nums)-1

   for index in reversed(range(len(nums))):
        samller_value = nums[smaller_index]
        larger_value = nums[larger_index]

        if abs(samller_value) > abs(larger_value):
            sorted_squred[index] = samller_value * samller_value
            smaller_index += 1
        else:
            sorted_squred[index] = larger_value * larger_value
            larger_index -= 1
    
   return sorted_squred

result = sorted_squred([1,2,3, 5,6,8, 9])
print("result", result)
