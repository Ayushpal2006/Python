def bubble(nums):
    l = len(nums)
    for i in range(l):
        for j in range(1, l - i):
            if nums[j - 1] > nums[j]:
                # swap(nums, j - 1, j)
                nums[j - 1] ,nums[j] = nums[j],nums[j - 1]
    return nums

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == "__main__":
    nums = [1,5,7,4,2,8]
    ans = bubble(nums)
    print(ans)