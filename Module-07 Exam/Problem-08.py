

def make_upper(s):
    str = ""
    for ele in s:
        if ele>='a' and ele<='z':
            str += chr(ord(ele)-32)
        else:
            str += ele
    return str

def make_capital(s):
    length = len(s)
    str = ""
    if s[0]>='a' and s[0]<='z':
        str += chr(ord(s[0])-32)
    else:
        str += s[0]
    for i in range(1,length):
        if s[i]>='A' and s[i]<='Z':
            str += chr(ord(s[i])+32)
        else:
            str += s[i]
    str += '.'
    return str

def make_lower(s):
    str = ""
    for ele in s:
        if ele>='A' and ele<='Z':
            str += chr(ord(ele)+32)
        else:
            str +=  ele
    return str

def test_script(s):
    upper = make_upper(s)
    print(upper)

    lower = make_lower(s)
    print(lower)

    capitalized = make_capital(s)
    print(capitalized)

s = "PyTest"
test_script(s)
