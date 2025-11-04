# num 2164.py
def remove_odd_index(arr):
    j = 0
    for i in range(0, len(arr), 2):
        arr[j] = arr[i]
        j += 1
    del arr[j:]
    return arr

def remove_even_index(arr):
    j = 0
    for i in range(1, len(arr), 2):
        arr[j] = arr[i]
        j += 1
    del arr[j:]
    return arr

n = int(input())
arr = list(range(1, n + 1))

while len(arr) > 1:
    if len(arr) % 2 == 0:
        arr = remove_even_index(arr)
    else:
        keep = arr[1]
        tail = arr[2:]
        arr = remove_even_index(tail)
        arr.append(keep)

print(arr[0])