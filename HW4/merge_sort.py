def mergeSort(array):
    if len(array) > 1:

        midPoint = len(array)//2
        leftArray = array[:midPoint]
        rightArray = array[midPoint:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        x = 0
        y = 0
        z = 0

        while x < len(leftArray) and y < len(rightArray):
            if leftArray[x] < rightArray[y]:
                array[z] = leftArray[x]
                x += 1
            else:
                array[z] = rightArray[y]
                y += 1
            z += 1

        
        while x < len(leftArray):
            array[z] = leftArray[x]
            x += 1
            z += 1

        while y < len(rightArray):
            array[z] = rightArray[y]
            y += 1
            z += 1


def printSortedArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()