  def rotLeft(a, d):
    n=int(input())
    l=list(map(int,input().split()))
    r=int(input())
    res=l[r:n]+l[0:r]
for i in res:
    print(i,end=' ')
