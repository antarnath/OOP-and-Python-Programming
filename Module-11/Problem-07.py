def sub_sets(my_set):
    return subserRecur([], sorted(my_set))

def subserRecur(curr, my_set):
    if my_set:
        return subserRecur(curr, my_set[1:])+subserRecur(curr+[my_set[0]], my_set[1:])
    return [curr]

my_set = [4,5,6]
print(sub_sets(my_set))