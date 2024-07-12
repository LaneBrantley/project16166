#INSERTIONSORT
def insertionSort(myArr):
    length = len(myArr)
    if length <= 1: #case if array is only one or less element, meaning it is already "sorted"
        return myArr

    for index in range(1, length): #for each element
        currElement = myArr[index] #get current element
        j = index - 1 # index before current index
        while j >= 0 and currElement < myArr[j]: #while j is 0 or higher to avoid out of bounds, and if current element greater than
                                                 #the element comparing to
            myArr[j + 1] = myArr[j] #swaps two elements if current element is less than
            j -= 1 #decrement j
        myArr[j + 1] = currElement #once j = -1 or current element is not less than j, fill missing element with j + 1

#MERGESORT
def merge(leftHalf, rightHalf):
    newArr = []

    while len(leftHalf) > 0 and len(rightHalf) > 0:

        if leftHalf[0] > rightHalf[0]: #since arrays are all single elements, only need to compare index 0
            newArr.append(rightHalf[0]) #add least element and pop
            rightHalf.pop(0)
        else:
            newArr.append(leftHalf[0])
            leftHalf.pop(0)

    while len(leftHalf) > 0: #one of them will still have an element, so add to newArr and pop
        newArr.append(leftHalf[0])
        leftHalf.pop(0)

    while len(rightHalf) > 0:
        newArr.append(rightHalf[0])
        rightHalf.pop(0)

    return newArr #return sorted arr

def mergeSort(myArr): #due to nature of merge sorting, recursion makes it a lot more readable, so this will use recursion
    if len(myArr) == 1:
        return myArr

    leftHalf = myArr[0: int(len(myArr) / 2)] #split in two halfs
    rightHalf = myArr[int(len(myArr) / 2):]

    leftHalf = mergeSort(leftHalf) #recursively call to split them into individual elements
    rightHalf = mergeSort(rightHalf)

    return merge(leftHalf, rightHalf) #merge once down to singular elements back into sorted array

#HEAPSORT
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2 #find left and right nodes using ranks

    if left < n and arr[i] < arr[left]: #check if either node is greater than root, swap if they are
        largest = left

    if right < n and arr[i] < arr[right]: #
        largest = right

    if largest != i: #swap root if necessary
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        heapify(arr, n, largest) #recursively call until heap is re-heapified

def insertHeap(heap, num):
    heap.append(num) #adds num to heap
    index = len(heap) - 1 #goes to last index in heap

    while index > 0:
        parent = (index - 1) // 2 #finds parent of node
        if heap[index] > heap[parent]: #if node greater than parent, swap
            temp = heap[index]
            heap[index] = heap[parent]
            heap[parent] = temp
            index = parent

        else: #if not break
            break


def heapsort(arr):
    length = len(arr)

    # Build a maxheap
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)

    # One by one extract elements
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

#INPLACEQUICKSORT
def inPlacePartition(arr, low, high):
    pivot = arr[high]
    ptr = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            ptr += 1

            temp = arr[ptr]
            arr[ptr] = arr[j]
            arr[j] = temp

    temp = arr[ptr + 1]
    arr[ptr + 1] = arr[high]
    arr[high] = temp

    return ptr + 1


def inPlaceQuicksort(arr, low, high):
    if low < high:

        pi = inPlacePartition(arr, low, high)

        inPlaceQuicksort(arr, low, pi - 1)

        inPlaceQuicksort(arr, pi + 1, high)

#MODIFIED QUICKSORT
def medianOfThree(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if a < c:
            return low
        elif b > c:
            return mid
        else:
            return high
    else:
        if a > c:
            return low
        elif b < c:
            return mid
        else:
            return high

def modifiedPartition(arr, low, high):
    pivotIndex = medianOfThree(arr, low, high)
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex] #move pivot to end of array
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def modifiedQuicksort(arr, low, high):
    if low < high:
        if high - low + 1 <= 10: # if less than 10, use insertion sort
            insertionSort(arr[low:high + 1])

        else:
            pi = modifiedPartition(arr, low, high)
            modifiedQuicksort(arr, low, pi - 1)
            modifiedQuicksort(arr, pi + 1, high)

# #HEAPSORT TEST
# arr = []
# nums_to_insert = [12, 11, 13, 5, 6]
# for num in nums_to_insert:
#     insertHeap(arr, num)
# print("Heap before sorting:", arr)
# heapsort(arr)
# print("Sorted array is:", arr)

# #INPLACE QUICKSORT TEST
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
# size = len(data)
# inPlaceQuicksort(data, 0, size - 1)
# print('Sorted Array in Ascending Order:')
# print(data)

#MODIFIED QUICKSORT TEST
arr = [1, 7, 4, 1, 10, 9, -2, 3, 5, 8, 6, 11, 15, 13]
print("Unsorted Array")
print(arr)
modifiedQuicksort(arr, 0, len(arr) - 1)
print('Sorted Array in Ascending Order:')
print(arr)