def bubblesort(input_array):
    array = input_array[:]
    if len(array) <= 1:
        return array
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1 ):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


## Example [3,2,4,1]
# i=0, j=0: [2,3,4,1] switch
# i=0, j=1: [2,3,4,1] pass
# i=0, j=2: [2,3,1,4] switch
# i=1, j=0: [2,3,1,4] pass
# i=1, j=1: [2,1,3,4] switch
# i=2, j=0: [1,2,3,4] switch
## return: [1,2,3,4]
