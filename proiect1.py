def insertion_sort(v):  #O(n**2)
    for i in range(1, len(v)):
        key = v[i]
        j = i-1
        while j >= 0 and key < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key

def radix_sort(v):  #O(d*(n+b)) d-nr of digits b-bucket size
    maxi = max(v)
    p = 1
    while maxi:
        b = [[] for x in range(10)]
        for i in v:
            b[i//p % 10].append(i)
        k = 0
        for i in b:
            for j in i:
                v[k] = j
                k = k+1
        maxi = maxi//10
        p = p*10


def merge_sort(v):    #O(nlogn)
    if len(v) > 1:
        mid = len(v) // 2
        st = v[:mid]
        dr = v[mid:]
        merge_sort(st)
        merge_sort(dr)
        i = j = k = 0
        while i < len(st) and j < len(dr):
            if st[i] <= dr[j]:
                v[k] = st[i]
                i += 1
            else:
                v[k] = dr[j]
                j += 1
            k += 1
        while i < len(st):
            v[k] = st[i]
            i += 1
            k += 1

        while j < len(dr):
            v[k] = dr[j]
            j += 1
            k += 1


def printList(v):
    for i in range(len(v)):
        print(v[i], end=" ")
    print()


def shell_sort(v):
    m = len(v) // 2
    while m > 0:
        j = m
        while j < len(v):
            i = j - m
            while i >= 0:
                if v[i+m] > v[i]:

                    break
                else:
                    v[i+m], v[i] = v[i], v[i+m]

                i = i - m
            j += 1
        m = m // 2


def heapify(v, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and v[largest] < v[l]:
        largest = l
    if r < n and v[largest] < v[r]:
        largest = r
    if largest != i:
        v[i], v[largest] = v[largest], v[i]
        heapify(v, n, largest)


def heap_sort(v):
    n = len(v)
    for i in range(n // 2 - 1, -1, -1):
        heapify(v, n, i)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)

def test_sort(v):
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return 0
    return 1

import random
import time
n = 0
t = 1
with open('date.in', 'r') as f:
    for linie in f:
        if n == 0:
            n = int(linie)
        else:
            L = linie.strip().split()
            a = int(L[0])
            b = int(L[1])
            v = [0]
            print("TESTUL", t)
            print("N =",a,"max =",b)
            for x in range(a):
                v.append(random.randint(0,b))
            start = time.time()
            insertion_sort(v)
            stop = time.time()
            if test_sort(v) == 1:
                print("Insertion Sort ",stop-start)
            start = time.time()
            radix_sort(v)
            stop = time.time()
            if test_sort(v) == 1:
                print("Radix Sort ",stop-start)
            start = time.time()
            shell_sort(v)
            stop = time.time()
            if test_sort(v) == 1:
                print("Shell Sort ",stop-start)
            start = time.time()
            merge_sort(v)
            stop = time.time()
            if test_sort(v) == 1:
                print("Merge Sort ",stop-start)
            start = time.time()
            heap_sort(v)
            stop = time.time()
            if test_sort(v) == 1:
                print("Heap Sort ",stop-start)
            t += 1

