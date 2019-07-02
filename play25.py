n1=int(input())
l1=list(map(str,input().split()))
l1.sort(key=len)
for i1 in range(len(l1)-1):
    if len(l1[i1])==len(l1[i1+1]) and l1[i1]>l1[i1+1]:
        l1[i1],l1[i1+1]=l1[i1+1],l1[i1]
print(*l1)
