import random

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        if (min != i):
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

arr = []
for i in range(100):
    arr.append(random.randint(0,1000))
    
selection_sort(arr)
print arr
