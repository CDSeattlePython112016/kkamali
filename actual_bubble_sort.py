import random
import time

start_time = time.time()
def bubble_sort(arr):
    swapped = True
    while (swapped):
        swapped = False;
        for i in range (len(arr) - 1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr

arr = []
for i in range(100):
    arr.append(random.randint(0,1000))

sorted_arr = bubble_sort(arr)
print("%s seconds" % (time.time() - start_time))
print sorted_arr
