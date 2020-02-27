def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = key

#Create list and populate it with elements in decreasing order
nums = [0 for i in range(10)]
val = 9
for i in range(len(nums)):
    nums[i] = val
    val -= 1  

insertion_sort(nums)
print(nums)
      
