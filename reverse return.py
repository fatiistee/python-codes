def print_to_n(n):
    list=[]
    while n>0:
        list.append(n)
        n=n-1   
    return list
n=int(input()) 
print(print_to_n(n))