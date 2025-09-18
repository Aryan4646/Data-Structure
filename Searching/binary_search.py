# BINARY SEARCH

def binary_search(a,target):
    low = 0
    high = len(a)-1

    while low <= high:
        mid = (low+high)//2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid+1
        elif a[mid] > target:
            high = mid-1

    return -1

Arr = [1, 3, 5, 7, 9, 11, 13]
Target = 9

print(f"Original_Array: {Arr}")

is_present = binary_search(Arr,Target)

if is_present == -1:
    print("Target element is not present")
else:
    print(f"Target element is at index {is_present}")