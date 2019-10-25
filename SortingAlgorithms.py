#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:19:31 2019

@author: brett
"""

# bubblesort
#preconditon: lst = []

def bubbleSort(lst):
    count = len(lst)-1
    for j in range(0, count):
        done_swap = True
        for i in range(0, count-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done_swap = False
        if done_swap:
            break



lst = [5,65,3,5,6,3,45,34,32,333]   
bubbleSort(lst)         
print(lst)

# selectionsort

def selectionSort(lst):
    count = len(lst)
    
    for i in range(count-1):
        min_pos = i
        for j in range(i+1,count):
            if lst[j] < lst[min_pos]:
                min_pos = j
        temp = lst[i] 
        lst[i] = lst[min_pos]
        lst[min_pos] = temp
        
            
            
lst = [5,65,3,5,6,3,45,34,32,333]              
selectionSort(lst)
print(lst)

# insertionsort

def insertionSort(lst):
    for i in range(1, len(lst)):
        for j in range(i-1,0,-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                break

lst = [5,65,3,5,6,3,45,34,32,333]              
selectionSort(lst)
print(lst)


def merge(lst,front,middle, back):
    l = lst[front:middle]
    r = lst[middle+1:back]
    i=j=0
    for k in range(front, back+1):
        if l[i] <= r[j]:
            lst[k] = l[i]
            i+=1
        else:
            lst[k] = r[j]
            j+=1

def mergeR(lst,front,back):
    if front < back:
        middle = (back + front)/2
        mergeR(lst, front, middle)
        mergeR(lst, middle+1, back)
        merge(lst,front, middle, last)
        
        
        
def mergeSort(lst):
    mergeR(lst, 0, len(lst)-1)
    
    
    
    
    
    
    
    
    
    
lst = [5,65,3,5,6,3,45,34,32,333]              
mergeSort(lst)
print(lst)

