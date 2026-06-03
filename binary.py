def binary_search(listi, item):
    low = 0
    high = len(listi) - 1
    while low <= high:
        middle = int((low + high) / 2)
        attempt = listi[middle]
        if attempt == item:
            return middle
        if attempt > item:
            high = middle - 1
        else:
            low = middle + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 5))

# item == 5
# listi = [1, 3, 5, 7, 9]
# low == 0
# high == 4
# while first loop:
# middle = int((0+4)/2)
#