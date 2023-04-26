

data = {key:val for key in range(1, 6, 1) for val in [list(x for x in range(1, 6, 1) if x!=key)] }
print(data)

