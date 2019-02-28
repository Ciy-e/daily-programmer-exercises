# adds all the elements in an array to except for the index passed through
def sumExcept(arr, i):
    sum = 0
    for n in range(len(arr)):
        if n == i:
            pass
        else:
            sum += arr[n]
    return sum
            
#minimax implementation for an array of ints
def miniMaxSum(arr):
    lowest = sumExcept(arr, 0)
    highest = sumExcept(arr, 0)

    for i in range(1, len(arr)):
        currentSum = sumExcept(arr, i)
        if currentSum > highest:
            highest = currentSum
        if currentSum < lowest:
            lowest = currentSum
    
    print(str(lowest) + " " + str(highest))