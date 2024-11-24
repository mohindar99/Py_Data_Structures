# creation of generators in the python

def count_values(n):
    count=1
    while count<=n:
        yield count
        count+=1

counter=count_values(5)
for n in counter:
    print(n)



