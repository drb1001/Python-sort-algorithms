def mergesort(input_array):
    array = input_array[:]
    if len(array) <= 1:
        return array
    subarray1 = mergesort( array[:len(array)/2] )
    subarray2 = mergesort( array[len(array)/2:] )
    return merge(subarray1, subarray2)

def merge(array1, array2):
    output = []
    while ( len(array1) > 0 and len(array2) > 0 ):
        if array1[0] > array2[0] :
            output.append( array2[0] )
            array2 = array2[1:]
        else:
            output.append( array1[0] )
            array1 = array1[1:]
    if len(array1) > 0 :
        output.extend( array1 )
    if len(array2) > 0 :
        output.extend( array2 )
    return output


## Example: [3,4,2,1]
# [3,4] ; [2,1]
# [3][4] ; [2][1]
# [3][4] ; [2][1]
# [][4] -> [3] ; [2][] -> [1]
# [][] -> [3,4] ; [][] -> [1,2]
# [3,4] ; [1,2]
# [3,4] [2] -> [1]
# [3,4] [] -> [1,2]
# [] [] -> [1,2,3,4]
## return: [1,2,3,4]
