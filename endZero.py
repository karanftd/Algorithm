'''
Given an array of integers, modify the array by moving all the zeros to the end (right side). 
The order of other elements doesn't matter.
E.g. [1, 2, 0, 3, 0, 1, 2], the program can output [1, 2, 3, 1, 2, 0, 0].
'''



def moveZero(arr):
    
    count = 0
    for i in range (0, len(arr)):

        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    
    while count < len(arr):
        
        arr[count] = 0 
        count = count + 1

    return arr     

arr = [1, 2, 0, 3, 0, 1, 2] 

print moveZero(arr)