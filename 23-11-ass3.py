n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
bs=l[0:s]
afs=l[e+1:n]
s=l[s:e+1]
s.sort()
res=bs+s+afs
for i in res:
    print(i,end=' ')
