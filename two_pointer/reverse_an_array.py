def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()




def reverseArray(arr, n):
    start = 0
    end = n - 1
    while start < end:
        arr[start] = arr[end]
        arr[end] =arr[start]
        start += 1
        end -= 1
    printArray(arr, n)

# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)