
def partition(array):
 
    # Choose the rightmost element as pivot
    pivot = array[-1]
 
    i = -1 # Pointer for last elemnet smaller than pivot 
 
    for j in range(0, len(array)):
        if array[j] <= pivot:
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[-1]) = (array[-1], array[i + 1])
 
    print(array)
    # Return the position from where partition is done
    return i + 1


partition([3,5,2,7,6,4])