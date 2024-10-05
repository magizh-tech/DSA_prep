# print  odd  numbers from  1 to 20


# for i in range(1,20,2):
# print([i for i in range(1,20,2)])
def prime_number(n):
    for i in range(2,n):
        # print(i,"is the i value")
        if n%i==0:
            return False 
        
    return True
# print(prime_number(100))


def list_prime(n):
    lis=[]
    for j in range (1,n):
        if prime_number(j):
            lis.append(j)
    return lis
print(list_prime(100))        

