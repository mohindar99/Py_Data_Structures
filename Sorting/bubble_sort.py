def bubble_sort(cust_list):
    for i in range(len(cust_list)):
        for j in range(len(cust_list)-1-i):
            if cust_list[i]>cust_list[i+1]:
                cust_list[i],cust_list[i+1]=cust_list[i+1],cust_list[i]

    return cust_list

print(bubble_sort([3,2,78,12,15,67,99]))