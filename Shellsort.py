def shellsort(input_array):
    array = input_array[:]
    if len(array) <= 1:
        return array

    gaps = [ len(array) / 2]
    while gaps[-1] > 1 :
        gaps.append( gaps[-1]/2 )

    for gap in gaps:
        for start in range(gap, len(array)):
            restart = start
            while restart > 0 and array[restart] < array[restart - gap]:
                temp = array[restart]
                array[restart] = array[restart - gap]
                array[restart - gap] = temp
                restart = restart - gap
    return array

## Example [3,5,2,4,1]
# gaps = [2,1]
# gap = 2
#   [3,2,1]
#   i=1: [2,3,1]
#   i=2: [2,1,3]
#        [1,2,3]
#   [5,4]
#   i=1: [4,5]
# [1,4,2,5,3]
# gap = 1
#   [1,4,2,5,3]
#   i=1: [1,4,2,5,3]
#   i=2: [1,2,4,5,3]
#   i=3: [1,2,4,5,3]
#   i=4: [1,2,4,3,5]
#        [1,2,3,4,5]
## return: [1,2,3,4,5]
