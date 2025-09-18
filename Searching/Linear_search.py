# Linear Search

def linear_search(a,target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

Arr = [4, 7, 1, 9, 3]
Target = 9

print(f"Original_Array: {Arr}")

is_present = linear_search(Arr,Target)

if is_present == -1:
    print("Target element is not present")
else:
    print(f"Target element is at index {is_present}")
