import time

max_time = 0.250
swapCount = 0

##---to reset swap count
def mergeSort(arr,displayArray,speedInput,pauseBool,start,end):
    global swapCount
    swapCount = 0
    merge_sort(arr,displayArray,speedInput,pauseBool,start,end)


# divides the array recursively into two parts then sorts
def merge_sort(arr,displayArray,speedInput,pauseBool,start,end):
    if start<end:
        mid = (start+end) // 2
        merge_sort(arr,displayArray,speedInput,pauseBool,start,mid)
        merge_sort(arr,displayArray,speedInput,pauseBool,mid+1,end)
        merge(arr,displayArray,speedInput,pauseBool,start,mid,end)


def merge(arr,displayArray,speedInput,pauseBool,start,mid,end):
    global swapCount

    #--highlight the left and the right parts of the array
    colorArray = []
    for i in range(len(arr)):
        if i>=start and i<=mid:
            colorArray.append('#ffff00')
        elif i>=mid+1 and i<=end:
            colorArray.append('#5200cc')
        else:
            colorArray.append('red')

    displayArray(arr,colorArray,swapCount)
    time.sleep(max_time - (speedInput * max_time / 100))

    arrL = arr[start:mid+1]
    arrR = arr[mid+1:end+1]

    i, j, k = 0, 0,start # i->arrL;   j->arrR;   k->arr

    while (i < len(arrL) and j < len(arrR)):
        if arrL[i] < arrR[j]:
            arr[k] = arrL[i]
            swapCount+=1
            i+=1
            for x in range(start,k):
                colorArray[x] = 'green'
            displayArray(arr, colorArray, swapCount)
            time.sleep(max_time - (speedInput * max_time / 100))
        else:
            arr[k] = arrR[j]
            swapCount+=1
            j+=1
            for x in range(start,k):
                colorArray[x] = 'green'
            displayArray(arr, colorArray, swapCount)
            time.sleep(max_time - (speedInput * max_time / 100))

        k+=1

    #check if anything left
    while i<len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        swapCount+=1
        for x in range(start, k ):
            colorArray[x] = 'green'
        displayArray(arr, colorArray, swapCount)
        time.sleep(max_time - (speedInput * max_time / 100))

    while j<len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1
        swapCount+=1
        for x in range(start, k ):
            colorArray[x] = 'green'
        displayArray(arr, colorArray, swapCount)
        time.sleep(max_time - (speedInput * max_time / 100))

    print("Sorted arr : ",arr)
