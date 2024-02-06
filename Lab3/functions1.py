#Ex1.
def ounces(k):
    print(k*28.3495231)
k=float(input())
ounces(k)

#Ex2.
def function(f):
    s=(5/9)*(f-32)
    print(s)
f=float(input())
function(f)

#Ex3.
def farm(heads, legs):
    r=(legs-(heads*2))/2
    ch=heads-r
    print("rabbits =",r, "chikens =",ch)
heads=int(input("How many heads?"))
legs=int(input("How many legs?"))
farm(heads, legs)
#Ex4.
def prime():
    lst=[]
    list=[]
    x=int(input())
    for i in range(x):
        num=int(input())
        lst.append(num)
        k=2
        for j in range(0, len(lst)):
            while k<lst[j]:
                if lst[j]%k!=0:
                    k+=1
        list.append(lst[j])            
    print(list)
prime()
#Ex6.
def reverse(x):
    words=x.split()
    y=' '.join(reversed(words))
    return y
n=reverse(input())
print(n)