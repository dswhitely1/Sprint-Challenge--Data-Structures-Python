import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
def merge(a, b):
    x = y = 0
    result = []

    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            result.append(a[x])
            x += 1
        else:
            result.append(b[y])
            y += 1

    result.extend(a[x:])
    result.extend(b[y:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    lhs = merge_sort(arr[midpoint:])
    rhs = merge_sort(arr[:midpoint])

    return merge(lhs, rhs)


print('Starting Sort of Names_2')
sort_start = time.time()
sorted_names = merge_sort(names_2)
sort_end = time.time()
print(f'Sorting finished in {sort_end - sort_start}')


def binary_search(target, arr=sorted_names):
    if len(arr) == 0:
        return False

    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        middle = (low + high) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return False


for name in names_1:
    if binary_search(name):
        duplicates.append(name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
