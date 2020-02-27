nums = [0 for i in range(10)]
val = 9
for i in range(0, len(nums)):
    nums[i] = val
    val -= 1

def selection_sort(nums):
    size = len(nums)
    for i in range(size):
        min = i
        for j in range(min + 1, size):
            if nums[j] < nums[min]:
                min = j
        (nums[i], nums[min]) = (nums[min], nums[i])

selection_sort(nums)
print(nums)