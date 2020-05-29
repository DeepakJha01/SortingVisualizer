import time

max_time = 0.250
# compares neighbouring elements in the array
def bubbleSort(arr, displayArray, speedInput, pauseBool):

    swapCount = 0
    N = len(arr)
    for i in range(N):
        swapped = False

        for j in range(N - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapCount += 1
                colorArray = ['red'] * N
                colorArray[j] = 'blue'
                colorArray[j + 1] = 'blue'
                if i:
                    colorArray[-i:] = ['green'] * i

                displayArray(arr, colorArray, swapCount)
                time.sleep(max_time - (speedInput*max_time/100))
                swapped = True

        if not swapped:
            break

    colorArray = ['green'] * N
    displayArray(arr, colorArray, swapCount)
    print("Sorted arr : ",arr)



# arr = [2, 10,11,25,13,78,1,7,80]
#
# print(bubbleSort(arr))
