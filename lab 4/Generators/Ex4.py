def square_numbers(a, b):
    for x in range(a, b+1):
        yield x*x
a=int(input())
b=int(input())    
a=square_numbers(a, b)
for i in a:
    print(i)