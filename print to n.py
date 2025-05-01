def print_to_n(n):
    s=1
    list=[]
    while s<=n:
        list.append(s)
        s=s+1   
    return list
n=int(input()) 
print(print_to_n(n))
       