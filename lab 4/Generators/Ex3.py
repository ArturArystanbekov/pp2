def numbers(n):
    for x in range(n+1):
        if x%3==0 and x%4==0:
            yield x
n=int(input())    
a=numbers(n)
for i in a:
    print(i)