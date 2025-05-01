def palindrom(n):
    answer=''
    for i in n:
        answer=i+answer
    if answer==n:
        return True
    else:
        return False
n=input()
print(palindrom(n))