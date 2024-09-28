
from typing import List

def removeDuplicates(arr: List[int]) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
        
    k = len(st)
    return k,list(st)


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    # for i in range(k):
    #     print(arr[i], end=" ")
    print(k)

