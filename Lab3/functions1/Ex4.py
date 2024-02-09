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