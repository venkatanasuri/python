  def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[i for i in range(1,n+1) if prime(i)]
for i in l:
    print(i,end=' ')
