def square_numbers(n):
    for x in range(n+1):
        if x%2==1:
            yield x
n=int(input())    
a=square_numbers(n)
for i in a:
    print(i)