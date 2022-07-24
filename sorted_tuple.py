n=int(input())
lst=[]
for i in range(n):
    a= tuple(int(a) for a in input().split())
    lst.append(a)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i][1]>lst[j][1]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)
