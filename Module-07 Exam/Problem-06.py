def clean_string(text):
    str = ""
    for ele in text:
        if ele.lower()>='a' and ele.lower()<='z':
            str += ele
    return str
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)