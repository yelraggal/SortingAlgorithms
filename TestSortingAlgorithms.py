import time
import numpy as np
import sys
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import time
sys.setrecursionlimit(6000)


def bubble(A):
    n = len(A)
    counter = 0
    for l in range(0, n - 1):
        flag = 0
        for y in range(0, n - 1 - l):
            if A[y] > A[y + 1]:
                A[y], A[y + 1] = A[y + 1], A[y]
                flag = 1
            counter = counter + 1
        if flag == 0:
            break
    return


def InsertionSorter(A):
    for i in range(1, len(A)):
        j = i
        key = A[i]
        while j > 0 and key < A[j - 1]:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = key

    return


def SelectionSorter(A):
    counter = 0
    l = 0
    minimum = A[0]
    for y in range(0, len(A) - 1):
        for m in range(y + 1, len(A)):
            if A[m] <= minimum:
                minimum = A[m]
                l = m
        if A[l] <= A[counter]:
            A[l] = A[counter]
            A[counter] = minimum
            counter = counter + 1
            minimum = A[counter]
    return


def quickSort(start, end, A, pivType):
    if pivType == 1:
        pivot = start
    elif pivType == 2:
        A[start], A[end] = A[end], A[start]
    elif pivType == 3:
        x= (end+start)//2
        A[start], A[x] = A[x], A[start]
    elif pivType == 4:
        x = random.randint(start, end)
        A[start], A[x] = A[x], A[start]
    else:
        print("wronge input")
        return
    pivot = start
    while (start < end):
        if A[pivot] > A[end]:
            A[pivot], A[end] = A[end], A[pivot]
            pivot = end
            start = start + 1
        elif A[pivot] < A[start]:
            A[pivot], A[start] = A[start], A[pivot]
            pivot = start
            end = end - 1
        elif pivot == start:
            end = end - 1
        elif pivot == end:
            start = start + 1
    return pivot


def random_quick(start, end, A, pivType):
    if end <= start:
        return
    else:
        pivot = quickSort(start, end, A, pivType)
        random_quick(start, pivot - 1, A, pivType)
        random_quick(pivot + 1, end, A, pivType)
    return

def random_quick_moduled(start, end, A, K):
    pivot = quickSort(start, end, A,1)
    if K > len(A):
        return
    else:
        if pivot + 1 == K:
            return A[pivot]
        elif pivot + 1 > K:
            return random_quick_moduled(start, pivot - 1, A, K)
        else:
            return random_quick_moduled(pivot + 1, end, A, K)


def call_merge(A):
    mid = len(A) // 2
    if len(A) > 1:
        firstArray = A[:mid]
        secondArray = A[mid:]
        call_merge(firstArray)
        call_merge(secondArray)
        index1 = 0
        index2 = 0
        mainInd = 0
        while index1 < len(firstArray) and index2 < len(secondArray):
            if firstArray[index1] <= secondArray[index2]:
                A[mainInd] = firstArray[index1]
                mainInd += 1
                index1 += 1
            else:
                A[mainInd] = secondArray[index2]
                mainInd += 1
                index2 += 1
        while index1 < len(firstArray):
            A[mainInd] = firstArray[index1]
            mainInd += 1
            index1 += 1
        while index2 < len(secondArray):
            A[mainInd] = secondArray[index2]
            mainInd += 1
            index2 += 1


def hybrid_merge_selection(A, threshould):
    if len(A) <= threshould:
        SelectionSorter(A)
    elif len(A) > 1:
        mid = len(A) // 2
        firstArray = A[:mid]
        secondArray = A[mid:]
        hybrid_merge_selection(firstArray, threshould)
        hybrid_merge_selection(secondArray, threshould)
        index1 = 0
        index2 = 0
        mainInd = 0
        while index1 < len(firstArray) and index2 < len(secondArray):
            if firstArray[index1] <= secondArray[index2]:
                A[mainInd] = firstArray[index1]
                mainInd += 1
                index1 += 1
            else:
                A[mainInd] = secondArray[index2]
                mainInd += 1
                index2 += 1
        while index1 < len(firstArray):
            A[mainInd] = firstArray[index1]
            mainInd += 1
            index1 += 1
        while index2 < len(secondArray):
            A[mainInd] = secondArray[index2]
            mainInd += 1
            index2 += 1


def tester(sizes):
    b = len(sizes)
    graphlist = list([])
    first = list()
    second = list()
    third = list()
    fourth = list()
    fifth = list()
    for i in range(0, b, 1):
        unsorted = np.random.choice(1000000, sizes[i], replace=True)
        res = unsorted.tolist()
        res1 = unsorted.tolist()
        res2 = unsorted.tolist()
        res3 = unsorted.tolist()
        res4 = unsorted.tolist()

        start = time.time()
        bubble(res)
        end = time.time()
        first.append(end - start)
        print("Running time for bubble Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        InsertionSorter(res1)
        end = time.time()
        second.append(end - start)
        print("Running time for insertion Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        SelectionSorter(res2)
        end = time.time()
        third.append(end - start)
        print("Running time for Selection Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        random_quick(0, len(res3) - 1, res3,1)
        end = time.time()
        fourth.append(end - start)
        print("Running time for quick Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        start = time.time()
        call_merge(res4)
        end = time.time()
        fifth.append(end - start)
        print("Running time for merge Sort of " + str(sizes[i]) + " elements is " + str((end - start)*1000) + " msec")

        print("\n")

    graphlist.append(first)
    graphlist.append(second)
    graphlist.append(third)
    graphlist.append(fourth)
    graphlist.append(fifth)

    return graphlist


def plotter(sizes, graphlist):

    sorts = ["Buble sort", "Insertion sort", "Selection sort", "Quick sort", "Merge sort"]
    plt.xlabel("Size of Array")
    plt.ylabel("Time for Execution (msec)")
    plt.yticks([0, 10000, 35000, 70000, 100000])
    plt.xticks([10, 1000, 5000, 15000, 30000])
    plt.title("Execution Graph")
    for i in range(0, len(graphlist[0])):
        plt.plot(sizes, graphlist[i], label=sorts[i])
        for j in range(0, len(graphlist[0])):
            plt.scatter(sizes[j], graphlist[i][j], c="black")
    plt.legend()
    plt.show()




sorting = Tk()
sorting.title("Asrotly")
sorting.minsize(100,300)
input1 = Label(text="Enter number of elements for a random array:", height=1, font=("Arial", 12))
input1.grid(row= 0)

arraysize = StringVar()
arraysize.set("0")
threshould = StringVar()
threshould.set("0")
sortingtype = StringVar()
sortingtype.set("0")
kEle = StringVar()
kEle.set("0")
choice = StringVar()
choice.set("0")

arrSize1 = Entry(sorting, width=40, textvariable=arraysize)
arrSize1.grid(row=1)
input2 = Label(text="Choose sorting type: 1)bubble 2)Insertion 3)Selection 4)Merge 5)Quick ", height=1, font=("Arial",12))
input2.grid(row=2)
sortingType = Entry(sorting, width=20, textvariable=sortingtype)
sortingType.grid(row=3)
input3 = Label(text="Hybrid merge & select sorter:", height=1, font=("Arial", 12))
input3.grid(row=5)
input4 = Label(text="Enter THRESHOULD: ", height=1, font=("Arial", 8))
input4.grid(row=6, column=0)

threshould = Entry(sorting, width=20, textvariable=threshould)
threshould.grid(row=6,column=1)

def quicksorting1():
    PIVOT = int(choice.get())
    start = time.time()
    random_quick(0, len(res) - 1, res, PIVOT)
    end = time.time()
    messagebox.showinfo("Quick sort", "Running time for array of " + str(size) + " elements is " + str(
        (end - start) * 1000) + " msec")
def choosepivote(res , size):
    pivot = Toplevel(sorting)
    pivot.title("Choose pivot location")
    pivot.minsize(100,100)


    input = Label(pivot,text="1)first element 2)last element 3)median element 4)Random element" , height=1 , font=("Arial",12))
    input.grid()
    piv = Entry(pivot, width=40, textvariable=choice)
    piv.grid()

    def quicksorting1():
        PIVOT = int(choice.get())
        start = time.time()
        random_quick(0, len(res) - 1, res, PIVOT)
        end = time.time()
        messagebox.showinfo("Quick sort", "Running time for array of " + str(size) + " elements is " + str(
            (end - start) * 1000) + " msec")
    pivotBtn = Button(pivot, width=20, height=1, bg="#e91e63", fg="black", borderwidth=0, text="find", command=quicksorting1)
    pivotBtn.grid()




def asrot():
    size = int(arraysize.get())
    unsorted = np.random.choice(1000000, size, replace=True)
    res = unsorted.tolist()
    check = int(sortingtype.get())
    thr = int(threshould.get())
    PIVOT = int(choice.get())
    if thr > 0:

        unsorted = np.random.choice(50000, 10000, replace=True)
        res1 = unsorted.tolist()
        res2 = unsorted.tolist()
        start = time.time()
        call_merge(res1)
        end = time.time()
        merge=(end-start)*1000
        messagebox.showinfo("Merge sort only", "Time for merge sorting only is " + str(merge) + " msec")
        time.sleep(2)
        start = time.time()
        hybrid_merge_selection(res2,thr)
        end = time.time()
        hybrid=(end-start)*1000
        messagebox.showinfo("hybrid sort", "Time taken for the same array for hybrid is " + str(hybrid)+" msec")

        messagebox.showinfo("hybrid and merge", "Time taken by merge only is " + str(merge) + "\nTime taken by hybrid is " + str(hybrid))



    else:
        if check == 1:
            start = time.time()
            bubble(res)
            end = time.time()
            messagebox.showinfo("Bubble sort","Running time for array of " + str(size) + " elements is " + str((end - start) * 1000) + " msec")
        elif check == 2:
            start = time.time()
            InsertionSorter(res)
            end = time.time()
            messagebox.showinfo("Insertion sort", "Running time for array of " + str(size) + " elements is " + str((end - start) * 1000) + " msec")
        elif check == 3:
            start = time.time()
            SelectionSorter(res)
            end = time.time()
            messagebox.showinfo("Selection sort", "Running time for array of " + str(size) + " elements is " + str((end - start) * 1000) + " msec")
        elif check == 4:
            start = time.time()
            call_merge(res)
            end = time.time()
            messagebox.showinfo("Merge sort", "Running time for array of " + str(size) + " elements is " + str((end - start) * 1000) + " msec")
        elif check == 5:
            choosepivote(res, size)
        else:
            messagebox.showinfo("Wrong input")

doneBtn =  Button(sorting, width=20, height=1, bg="#e91e63", fg="black", borderwidth=0, text="done", command=asrot)
doneBtn.grid(row=4)
hybridBtn = Button(sorting, width=20, height=1, bg="#e91e63", fg="black", borderwidth=0, text="hit", command=asrot)
hybridBtn.grid(row=6,column=2)

input5 = Label(text="Finding Kth element:", height=1, font=("Arial", 12))
input5.grid(row=7)
input6 = Label(text="Enter Kth element:", height=1, font=("Arial", 8))
input6.grid(row=8)
kElement = Entry(sorting, width=20, textvariable=kEle)
kElement.grid(row=8,column=1)
def kelem():
    size = int(arraysize.get())
    k = int(kEle.get())
    unsorted = np.random.choice(100, size, replace=True)
    res = unsorted.tolist()
    array1 = str(res)
    start = time.time()
    x = random_quick_moduled(0, len(res)-1, res, k)
    end = time.time()
    print(array1)
    messagebox.showinfo("Kth element","Kth Element: "+ str(x) + "\nRunning time: " + str(
        (end - start) * 1000) + "msec \n Array:"+"".join(array1))
kBtn = Button(sorting, width=20, height=1, bg="#e91e63", fg="black", borderwidth=0, text="find", command=kelem)
kBtn.grid(row=8,column=2)

input7 = Label(text="Lab 1:", height=1, font=("Arial", 20))
input7.grid(row=9)


def StartBtnAction():
    sizes = [10, 1000, 5000, 15000, 30000]
    Graph = tester(sizes)
    print(Graph)
    messagebox.showinfo("Graph",Graph)
    plotter(sizes, Graph)

startBtn = Button(sorting, width=12, height=1, bg="#e91e63", fg="white", borderwidth=0, text="Start", command=StartBtnAction)
startBtn.grid(row=10)

sorting.mainloop()






'''unsorted = np.random.choice(50, 20, replace=True)
res = unsorted.tolist()
threshould=2
hybrid_merge_selection(res, threshould)'''




'''unsorted = np.random.choice(50, 20, replace=True)
res = unsorted.tolist()
print(res)
k=4
kth = random_quick_moduled(0, len(res)-1, res, k)
print(kth'''


