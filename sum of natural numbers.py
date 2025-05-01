def sum(n):
    h=1
    s=0
    while h<=n:
        s=s+h
        h=h+1
    return s
n=int(input())
print(sum(n))
