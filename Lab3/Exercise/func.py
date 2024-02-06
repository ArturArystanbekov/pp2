"""
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
"""
#Ex4.
list=[]
lst=[]
num=int(input("Enter the number you wanna insert:"))
for i in range(num):
    x=int(input("Enter Number:"))
    list.append(x)
    k=2  
for j in list:
    while k<list[j]:
        if list[j]%k!=0:
            lst.append(list[j])
    k=+1
    print(lst)
        