import random

def insertion_sort(arr):
    for i in range (1, len(arr)):
        value = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > value):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = value

arr = []
for i in range(100):
    arr.append(random.randint(0,1000))
insertion_sort(arr)
print arr
