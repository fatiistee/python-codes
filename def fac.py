def factorial(n):
    s=1
    h=1
    while h<=n:
        s=s*h
        h=h+1
    return s
n=int(input())
print(factorial(n))