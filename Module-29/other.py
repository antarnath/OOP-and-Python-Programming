a = 0
def sum_odd(n, total):
    if n==1: return total
    elif n%2==0: return sum_odd(n-1, total)
    else: 
        # print(n)
        return sum_odd(n-2, total+n)

print(sum_odd(n=20, total=0))
print(a)