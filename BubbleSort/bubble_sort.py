#Create a list and populate a list
nums = [0 for i in range(0, 10)]
j = 9
for i in range(0, len(nums) - 1):
    nums[i] = j
    j -= 1


def optimized_bubble_sort(nums):
    length = len(nums)    
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                (nums[j], nums[j + 1]) = (nums[j + 1], nums[j])
                swapped = True
        if swapped == False:
            break

optimized_bubble_sort(nums)
print(nums)
            
