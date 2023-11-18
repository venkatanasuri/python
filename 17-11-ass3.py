n=int(input())
l=list(map(int,input().split()))
k=int(input())
l=list(set(l))
for i in range(1,k):
    m=max(l)
    l.remove(m)
print(max(l))
