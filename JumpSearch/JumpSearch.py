import math

# creating a sorted array and populate the array
numbers = [0 for i in range(18)]
for i in range(len(numbers)):
    numbers[i] = i + 10


def jump_search(numbers, target):
    length = len(numbers)
    interval = int(math.sqrt(length))
    for i in range(0, length, interval):
        if target == numbers[i]:
            return i
        elif target > numbers[i]:
            if (i + 4) < (length):
                continue 
            else:
                for k in range(i, length):
                    if numbers[k]  == target:
                        return k
                return -1      
        else:
            i -= interval
            for j in range(i, i + interval, 1):
                if numbers[j] == target:
                    return j
            return -1


print(jump_search(numbers, 20))