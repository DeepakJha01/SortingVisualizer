import time

max_time = 0.250
swapCount = 0

##---to reset swap count
def mergeSort(arr, displayArray, speedInput, pauseBool):
    global swapCount
    swapCount = 0
    start, end = 0, len(arr) - 1
    _merge_sort(arr, displayArray, speedInput, pauseBool, start, end)


# divides the array recursively into two parts then sorts
def _merge_sort(arr, displayArray, speedInput, pauseBool, start, end):
    if start < end:
        mid = (start + end) // 2
        _merge_sort(arr, displayArray, speedInput, pauseBool, start, mid)
        _merge_sort(arr, displayArray, speedInput, pauseBool, mid + 1, end)
        _merge(arr, displayArray, speedInput, pauseBool, start, mid, end)


def _merge(arr, displayArray, speedInput, pauseBool, start, mid, end):
    global swapCount

    N = len(arr)
    #--highlight the left and the right parts of the array
    colorArray = ['red'] * N
    colorCoords = ((start, mid + 1, '#ffff00'), (mid + 1, end + 1, '#5200cc'))
    for lower, upper, color in colorCoords:
        colorArray[lower:upper] = [color] * (upper - lower)

    displayArray(arr, colorArray, swapCount)
    time.sleep(max_time - (speedInput() * max_time / 100))

    arrL = arr[start:mid+1]
    arrR = arr[mid + 1:end + 1]

    i, j, k = 0, 0, start # i->arrL;   j->arrR;   k->arr

    while (i < len(arrL) and j < len(arrR)):
        if arrL[i] < arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1

        swapCount += 1
        colorArray[start:k] = ['green'] * (k - start)
        displayArray(arr, colorArray, swapCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

        k += 1

    #check if anything left
    while i < len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['green'] * (k - start)
        displayArray(arr, colorArray, swapCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    while j < len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['green'] * (k - start)
        displayArray(arr, colorArray, swapCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    print("Sorted arr : ", arr)
