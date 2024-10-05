def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def first(x):
    list=[]
    for j in range(1,x):
        if prime(j):
            list.append(j)
    return list   
print(len(first(525))) 
print(sum(first(525)))           



