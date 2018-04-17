'''
Given an array, return the length of the longest increasing contiguous subarray.
E.g., [1, 3, 2, 3, 4, 8, 7, 9], should return 4 because the longest increasing array is [2, 3, 4, 8].
'''


# aproch lenth using 2 variable
def getLong(arr):
    
    sum = 1
    max = 0
    for i in range(0, len(arr)):
        
        if i+1 < len(arr) and arr[i] < arr[i+1]:
            sum = sum+1
        elif sum > max:
            max = sum
            sum = 1
        else:
            sum = 1
    
    return max


arr = [1, 3, 2, 3, 4, 8, 9, 10]
print("the length of the longest increasing contiguous subarray is "
      ,getLong(arr))