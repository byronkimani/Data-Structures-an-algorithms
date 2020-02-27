numbers = [5,3,6,7,70,8,9,2,]

def linear_search(numbers, key):
    if key not in numbers:
        return -1
    else:
        for i in range(len(numbers)):
            if numbers[i] == key:
                return i

print(int(linear_search(numbers, 7)))
