

def Fib(n,memo):
    if n==1:
        return 0
    if n==2:
        return 1
    if not n in memo:
        memo[n]=Fib(n-1,memo) + Fib(n-2,memo)
    return memo[n]

myDict={}
print(Fib(6,myDict))
