
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if upper_bound is None:
        if left < len(arr):
            upper_bound = arr[left]
        else:
            upper_bound = None
    
    return iterations, upper_bound
