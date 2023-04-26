def replace_word(s, replace_with):
    word = s.split(' ')
    str = ""
    for ele in word:
        str += ele
        str += " "
    next = str.split('.')
    str1=""
    for a in next:
        str1 += a
    
    word = str1.split(" ")
    
    for index, value in enumerate(word):
        for index1, value1 in enumerate(replace_with):
            if value == value1:
                word[index] = replace_with[index1+1]
        
    final_string = ""
    for ele in word:
        final_string += ele + " "

    return final_string



replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
final_strign  = replace_word(s, replace_with)
print(final_strign)
