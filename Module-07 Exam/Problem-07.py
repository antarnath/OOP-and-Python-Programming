def replace_comma_with_space(text):
    s = ""
    for i in text:
        if i==',':
            s += " "
        else:
            s += i
    return s

    
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

