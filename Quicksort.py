def quicksort(input_array):
    array = input_array[:]
    if len(array) <= 1:
        return array
    array, pivot_location = partition(array)
    subarray1 = quicksort( array[:pivot_location] )
    subarray2 = quicksort( array[pivot_location+1:] )
    outputarray = subarray1[:]
    outputarray.append( array[pivot_location] )
    outputarray.extend(subarray2)
    return outputarray

def partition(input_array):
    array = input_array[:]
    pivot_value = array[0]
    leftwall = 1
    for i in range(1, len(array)):
        if array[i] < pivot_value :
            temp = array[i]
            array[i] = array[leftwall]
            array[leftwall] = temp
            leftwall = leftwall + 1
    array[0] = array[leftwall-1]
    array[leftwall-1] = pivot_value
    return array, leftwall-1


## Example: [3,5,2,1,4]
# [3,5,2,1,4]. pivot = 3. leftwall = 1
#   i=1: [3,5,2,1,4]. pass. leftwall = 1
#   i=2: [3,2,5,1,4]. switch. leftwall = 2
#   i=3: [3,2,1,5,4]. switch. leftwall = 3
#   i=4: [3,2,1,5,4]. pass. leftwall = 3
#   switch pivot with leftwall-1
# [1,2,3,5,4] -> [1,2][3][5,4]
#    [1,2]. pivot = 1. leftwall = 1.
#      i=1: [1,2]. pass. leftwall = 1.
#      switch pivot and leftwall-1
#    [1,2] -> [1][2]
#    [5,4]. pivot = 5. leftwall = 1.
#      i=1: [5,4]. switch. leftwall = 2.
#      switch pivot and leftwall-1
#    [4,5] -> [4][5]
# [1][2][3][4][5]
## return: [1,2,3,4,5]
