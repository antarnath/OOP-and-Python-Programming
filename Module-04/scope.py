balance = 580

def total_cost(price,quentity):
    global balance
    cost=price*quentity
    balance=balance-cost
    return cost

print(f"balanced: outside befor {balance}")
pay = total_cost(10, 3)
print(pay)

print(f"balanced: outside after {balance}")