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


arr = [12, 11, 13, 5, 6]
arr = mergeSort(arr)
print(arr)