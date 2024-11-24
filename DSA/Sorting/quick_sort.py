
# Just to swap the values which are passed to the function

def swap(my_list,ind1,ind2):
    my_list[ind1],my_list[ind2]=my_list[ind2],my_list[ind1]


# This will calculate the pivot value by keeping all the smaller elements to left and larger to right

def pivot(my_list,pivot_index,end_index):
    swap_index=pivot_index
    for i in range(pivot_index+1,end_index+1):
        if my_list[i]<my_list[pivot_index]:
            swap_index+=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index

# we define the quick sort by recursively calling the same function by pivot

def quicksort(my_list,left,right):
    if left<right:
        pivot_index=pivot(my_list,left,right)
        quicksort(my_list,left,pivot_index-1)
        quicksort(my_list,pivot_index + 1,right)

    return my_list


list1=[2,3,342,35,23,5,2,23,51,23]

print(quicksort(list1,0,len(list1)-1))