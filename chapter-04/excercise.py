def sum(arr:list):
    length = len(arr)
    acum = 0
    if length == 0:
        return 0
    else:
        f = first(arr)
        s = first(arr)
        addition = f + s
        ("That's addition: {addition}")
        acum = acum + addition
        sum(arr)
        return acum
def first(arr):
    if not arr:
        return 0
    else:
        first = arr.pop(0)
        return first

array = [2, 4, 6]

print(sum(array))