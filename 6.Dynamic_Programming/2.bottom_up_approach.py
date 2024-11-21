def fib(n):
    tb=[0,1]
    for i in range(2,n):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]


print(fib(4))