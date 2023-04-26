def create_string(l):
    str = ""
    for ele in l:
        str += ele+" "
    
    return str

    
l = ["This", "is", "very", "fantastic"]
print(create_string(l))