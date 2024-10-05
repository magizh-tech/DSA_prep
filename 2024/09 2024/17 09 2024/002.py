# generate the below pattern using for loop

#     ```
#     *
#     **
#     ***
#     ****
#     *****
#     ```

# n=5
# for i in range(1,n+1):
#     print("*"*i)



n = 5; 
[print("*" * i) for i in range(1, n + 1)]
