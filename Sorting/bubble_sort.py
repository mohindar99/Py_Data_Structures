def bubble_sort(cust_list):
    for i in range(len(cust_list)):
        for j in range(len(cust_list)-1-i):
            if cust_list[j]>cust_list[j+1]:
                cust_list[j],cust_list[j+1]=cust_list[j+1],cust_list[j]

    return cust_list

print(bubble_sort([98,3,2,78,12,19,15,67,99,6]))