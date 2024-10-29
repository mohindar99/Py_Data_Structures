from math import *

# insertion sort algo

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
    return arr


def bucket_sort(cust_list):

    # we are finding the no.of.buckets and max value to send the values of an array

    numofbuckets= round(sqrt(len(cust_list)))
    maxvalue= max(cust_list)
    arr=[]

    # creating the buckets

    for i in range(numofbuckets):
        arr.append([])

    #sending each value to the specific bucket based on the formula

    for j in cust_list:
        index_b=ceil(j*numofbuckets/maxvalue)
        arr[index_b-1].append(j)

    #sorting each bucket of the array using insertion sort

    for i in range(numofbuckets):
        arr[i]=insertion_sort(arr[i])

    # combining all the buckets back to the single array

    k=0
    for i in range(numofbuckets):
        for j in range(len(arr[i])):
            cust_list[k]=arr[i][j]
            k+=1
    return cust_list


print(bucket_sort([23,1,12,3,12,31,23,345,3,45,5,67,6,78,5]))
