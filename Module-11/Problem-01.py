def exp(a,n):
    return pow(a, n)


print("enter number: ",end="")
a, n = [int(x) for x in input().split()]  
result = exp(a, n)
print("result is:", result)