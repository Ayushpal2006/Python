def binary_search(arr, target):
    
    start = 0 
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2 

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1

# Example usage:
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7
    
    result = binary_search(sorted_array, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")