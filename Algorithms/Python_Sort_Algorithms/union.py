from tkinter import W

from numpy import append


def union(arr1,arr2):
    i = 0
    j = 0
    newArr = []
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j] and arr1[(i-1)] is not arr1[i] and arr1[(i+1)] is not arr1[i]:
            newArr.append(arr1[i])
        elif arr2[j] < arr2[i] and arr2[(j-1)] is not arr2[j] and arr2[(j+1)] is not arr2[j]:
            newArr.append(arr2[j])
        elif arr1[i] == arr2[j] :
            i+=i
            j+=j
            newArr.append(arr1[i])
        elif arr1[i] == arr1[i-1] or arr1[i] == arr1[i+1]:
            i+=i
        elif arr2[j] == arr1[i -1] or arr2[j] == arr2[j+1]:
            j+=j

    while(i < len(arr1)):
        newArr.append(arr1[i])
        i+=i
    while(j < len(arr2)):
        newArr.append(arr2[j])
    