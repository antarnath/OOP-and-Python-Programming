
def create_list(dic):
    list = []
    for key, value in dic.items():
        list.append(key)
        list.append(value)
    return list
    
dic = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
list = create_list(dic)
print(list)