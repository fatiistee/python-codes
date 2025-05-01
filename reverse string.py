def reverse_string(n):
    answer=''
    for i in n:
        answer=i+answer
    return answer
n=input()
print(reverse_string(n))