

def selection_sort(arr):

    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j

        arr[min_index],arr[i]=arr[i],arr[min_index]

    return arr

print(selection_sort([23,12,1,2,1,312,3,123,1]))