import time

max_time = 0.250

#finds the minimum value of the remaining array everytime
def selectionSort(arr,displayArray,speedInput,pauseBool):
    swapCount = 0

    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

                colorArray = []
                for x in range(len(arr)):
                    if x<i:
                        colorArray.append('green')
                    elif x==j or x==min_ind:
                        colorArray.append('blue')
                    else:
                        colorArray.append('red')

                displayArray(arr,colorArray,swapCount)
                time.sleep(max_time - (speedInput * max_time / 100))

        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        swapCount+=1
        colorArray = ['green' if x<=i else 'red' for x in range(len(arr))]
        displayArray(arr,colorArray,swapCount)
        time.sleep(max_time - (speedInput * max_time / 100))

    colorArray = ['green' for i in range(len(arr))]
    displayArray(arr, colorArray, swapCount)
    print("Sorted arr : ", arr)

