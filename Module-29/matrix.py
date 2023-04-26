import numpy as np


two_d = np.array([[3, 5], [5, 6], [8, 1]])

# print(two_d) 
three_d  = np.array([
    [[3, 5], [5, 6], [8, 1]],
    [[3, 5], [5, 6], [8, 1]],
    [[3, 5], [5, 6], [8, 1]]
])

# print(three_d)

one_d = np.array([1,2,3,4,5,6])
shaped = one_d.reshape(3,2)
# print(shaped)
change = np.flip(shaped)
# print(two_d)
# print()
# print(change)
# print()
add = two_d * change
# print(add)
# print(add)

back_to_one = add.flatten()
# check data type
print(back_to_one)
# print(back_to_one.dtype)
deff_type = back_to_one.astype('f')
# print(deff_type.dtype)
back_to_one_again = np.copy(back_to_one.astype('i'))
# print(back_to_one_again)
sorted = np.sort(back_to_one)
# print(sorted)

two_d = np.array([[1,2,3,1],[5,6,1,8]])
# print(two_d)
# print(two_d.max(axis=1))

print(np.unique(two_d, axis = 0))