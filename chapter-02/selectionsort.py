# smallest = 5
# small_index = 0

# First iteration:
# 3 < 5 -> True
# Therefore, smallest = 3 and small_index = 1

# Second iteration:
# 6 < 3 -> False

# Third iteration:
# 2 < 3 -> True
# Therefore, smallest = 2 and small_index = 3

# Fourth iteration:
# 10 < 2 -> False

# searchSmallest returns index 3.
# Then, arr.pop(3) removes the value 2,
# leaving the list as [5, 3, 6, 10].

# The process repeats until the original list is empty.
# Each iteration removes the smallest remaining element and appends it to newArr.