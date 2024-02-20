def square_numbers(n):
    for x in range(n+1):
        yield x*x
        
n=int(input())    
a=square_numbers(n)
for x in a:
    print(x)