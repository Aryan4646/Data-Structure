# Bubble Sort

def bubble_Sort(a):
    n = len(a)-1
    for i in range(n):
        for j in range(n-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
    return a

arr = [64, 34, 25, 12, 22, 11, 90]

print(f"Original array is: {arr}")
print(f"Sorted array: {bubble_Sort(arr)}")