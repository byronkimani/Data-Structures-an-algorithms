#Creating and populating the sorted list
numbers = [0 for i in range(10)]
for i in range(len(numbers)):
    numbers[i] = i + 10

#defining the function for binary search
def bin_search(numbers, target):
    length = int(len(numbers))
    min = 0
    max = length - 1
       
    while(max >= min):
        mid = int((max + min)/2)
        if target < numbers[mid]:
            max = mid -1
        elif target > numbers[mid]:
            min = mid + 1
        else:
            return mid

    return -1

print(bin_search(numbers, 13))