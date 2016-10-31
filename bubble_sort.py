import random

def bubble_sort(arr):
    for i in range (len(arr)):
        for j in range (len(arr) - 1):
            if (arr[j] > arr[i]):
                arr[i], arr[j] = arr[j], arr[i]


arr = []
for i in range(100):
    arr.append(random.randint(0,100))

bubble_sort(arr)
print arr
