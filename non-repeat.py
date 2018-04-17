'''
Given an array of integers where every value appears twice except one, find the single, non-repeating value. 

Follow up: do so with O(1) space.
E.g., [2, 5, 3, 2, 1, 3, 4, 5, 1] returns 4, because it is the only value that appears in the array only once.
'''

def getSingle(arr):
    
    if len(arr) == 0:
        return

    xor = 0

    for ele in arr:
        xor = xor ^ ele

    return xor    

arr = [2, 5, 3, 2, 1, 3, 4, 5, 1]
print("The element with single occurrence is "
      ,getSingle(arr))