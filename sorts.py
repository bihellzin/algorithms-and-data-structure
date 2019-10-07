# Selection sort

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Bubble sort

def bubble(arr):
    for i in range(len(arr)):

        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr

# Insertion sort

def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

# Merge sort

def merge(arr, l, r):
    i = j = k = 0

    nL = len(l)
    nR = len(r)

    while i < nL and j < nR:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1

        else:
            arr[k] = r[j]
            j += 1

        k += 1

    while i < nL:
        arr[k] = l[i]
        k += 1
        i += 1

    while j < nR:
        arr[k] = r[j]
        k += 1
        j += 1


    return arr

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    meio = n//2
    esquerda = arr[0:meio]
    direita = arr[meio:]

    mergeSort(esquerda)
    mergeSort(direita)

    merge(arr, esquerda, direita)

    return arr

# Quick Sort

def quicksort(arr):
    if arr == []:
        return []
    else:
        pivo = arr.pop(0)
        return quicksort([x for x in arr if x <= pivo]) + [pivo] + quicksort([x for x in arr if x > pivo])
    



                   


    
