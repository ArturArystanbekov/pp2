#Ex6.
def reverse(x):
    words=x.split()
    y=' '.join(reversed(words))
    return y
n=reverse(input())
print(n)