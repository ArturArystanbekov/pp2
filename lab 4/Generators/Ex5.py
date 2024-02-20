def reverse(n):
    for i in range(n, -1, -1):
        yield i
n=int(input())
a=reverse(n)
for x in a:
    print(x)