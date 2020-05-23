
#---start import section-------------------
import time
import math
import random
from tkinter import *
from tkinter import ttk
from mergesort import mergeSort
from quicksort import quickSort
from bubblesort import bubbleSort
from selectionsort import selectionSort
# from tkinter.scrolledtext import ScrolledText
#---end import section---------------------


root = Tk()
root.title('Sorting Algorithms Visualizer')
root_width = 1000
root_height = 650
root.maxsize(root_width,root_height)   #(width,height)
root.config(bg='black')

#----GLOBAL VARIABLES---------
allAlgos = ('Bubble Sort','Merge Sort','Quick Sort','Selection Sort')
selectedAlgo = StringVar()
pauseBool = False
arr = []
#-----------------------------

def generateRandomArray():
    #random array of non-repeating n elements
    global arr
    arr = []
    n = int(dataSize.get())
    for i in range(1,n+1):
        arr.append(i)

    #random shuffle
    for i in range(n-1,0,-1):
        ind = math.floor(random.random()*(i+1))
        arr[i],arr[ind] = arr[ind],arr[i]

    arrayColor = ['red' for i in range(n)]

    swapCount = 0
    displayArray(arr,arrayColor,swapCount)
    # return arr

def normalizeArray(arr):
    return [i/max(arr) for i in arr]

def displayArray(arr,arrayColor,opCount):

    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasHeight = 400 - 10
    outputCanvasWidth = 950 - 20

    barWidth = outputCanvasWidth/(n+1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i,h in enumerate(normalizedArr):
        #top - left                                           #|(x0,y0)-------------|
        x0 = i*barWidth+initialspace+barspace                 #|                    |
        y0 = outputCanvasHeight - h*350                       #|                    |
                                                              #|                    |
        #bottom-left                                          #|                    |
        x1 = (i+1)*barWidth+initialspace                      #|                    |
        y1 = outputCanvasHeight                               #|-------------(x1,y1)|

        outputCanvas.create_rectangle(x0,y0,x1,y1, fill = arrayColor[i])

    ##display swapCount
    swapCountLabel = Label(outputCanvas,text = '#Swap Count : '+str(opCount),fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,20,window = swapCountLabel)

    root.update_idletasks()

def startSort():
    global arr

    if algoCombo.get() == 'Bubble Sort':
        bubbleSort(arr,displayArray,sortSpeed.get(),pauseBool)

    elif algoCombo.get() == 'Selection Sort':
        selectionSort(arr,displayArray,sortSpeed.get(),pauseBool)

    elif algoCombo.get() == 'Merge Sort':
        mergeSort(arr,displayArray,sortSpeed.get(),pauseBool,0,len(arr)-1)

    elif algoCombo.get() == 'Quick Sort':
        quickSort(arr,displayArray,sortSpeed.get(),pauseBool,0,len(arr)-1)

# def pauseSort():
#     global pauseBool
#     pauseBool = True
    # return bubbleSort


# arr = generateRandomArray(5)
# displayArray(arr)

#----User Interface Section---------------------------------------------------------------------------------------------
inputFrame = Frame(root,height = 200,width = 950,bg = 'black')
inputFrame.grid(row = 0,column = 0,padx = 10,pady = 10)

outputCanvas = Canvas(root,height = 400,width = 950,bg = '#99ffff')
outputCanvas.grid(row = 1,column = 0,padx = 10,pady = 10)

#--input frame-------------------------------------------------------
head = Label(inputFrame,text = 'Select Algorithm -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head.grid(row = 0,column = 0,padx = 5,pady = 5)

algoCombo = ttk.Combobox(inputFrame,values = allAlgos,width = 15,font = ('Comic Sans MS',14))
algoCombo.grid(row = 0,column = 1,padx = 5,pady = 5)
algoCombo.current()

generate = Button(inputFrame,text = 'Generate',fg = 'black',bg = '#ff0000',height = 1,width = 10,font = ('Comic Sans MS',14),command = generateRandomArray )
generate.grid(row = 0,column = 2,padx = 5,pady = 5)

dataSize = Scale(inputFrame,from_ = 3,to = 100,resolution = 1,length = 400,width = 15,orient = HORIZONTAL,label = 'Data Size [n]',font = ('Comic Sans MS',10))
dataSize.grid(row = 1,column = 0,padx = 5,pady = 5,columnspan = 2)

# enter = Button(inputFrame,text = 'Enter->',fg = 'black',bg = '#99ffff',height = 1,width = 10,font = ('Comic Sans MS',14),command = '' )
# enter.grid(row = 1,column = 2,padx = 5,pady = 5)

sortSpeed = Scale(inputFrame,from_ = 1,to = 100,resolution = 0.1,length = 400,width = 15,orient = HORIZONTAL,label = 'Sorting Speed [s]',font = ('Comic Sans MS',10))
sortSpeed.grid(row = 2,column = 0,padx = 5,pady = 5,columnspan = 2)

play = Button(inputFrame,text = 'Play',fg = 'black',bg = '#00ff00',height = 5,width = 10,font = ('Comic Sans MS',14),command = startSort )
play.grid(row = 1,column = 2,padx = 5,pady = 5,rowspan = 2)

# xxx = ScrolledText(inputFrame,width = 20,height = 12)
# xxx.grid(row = 0,column = 3,padx = 5,pady = 5,rowspan = 3)

#--output frame------------------------------------------------------
    #---displayArray---

root.mainloop()
