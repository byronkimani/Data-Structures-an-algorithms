#Functioin to merge that takes the left list, right list and the array to merge into as arguments

def merge(left, right, A):
    #Variables to keep track of the smallest value in the lists
    #i is for L
    #j is for R
    #k is for the main array to be joined into

    i = j = k = 0
    l_size = len(left)
    r_size = len(right)

    #Comparing the values of the lowest indices in both left and right and putting it into main

    while i < l_size and j < r_size:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1

        else:
            A[k] = right[j]
            j += 1

        k += 1

    #if you finish iterating through either one of the 2 list L and R one of the following will execute

    while i < l_size:
        A[k] = left[i]
        i += 1
        k += 1
    
    while j < r_size:
        A[k] = right[j]
        j += 1
        k += 1
    

def merge_sort(nums):
    size = len(nums)
    if size < 2:
        return

    mid = size // 2
    left = [0 for i in range(mid)]

    for i in range(0, len(left)):
        left[i] = nums[i]   

    right = [0 for i in range(0, len(nums) - mid)]
    for i in range(0, len(right)):
        right[i] = nums[i + mid]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, nums)

#Create a list and populate a list
nums = [0 for i in range(0, 10)]
j = 9
for i in range(0, len(nums) - 1):
    nums[i] = j
    j -= 1

print(nums)
merge_sort(nums)
print(nums)
