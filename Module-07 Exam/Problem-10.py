def create_new_string(s,a):
    word = s.split(' ')
    str = ""
    for ele in word:
        str += ele + " "
    word = str.split('.')
    str=""
    for ele in word:
        str += ele 
    
    word = str.split(" ")
    str=""
    for ele in word:
        str += ele+" "
    word = str.split(',')
    
    str = ""
    for ele in word:
        str += ele+" "
 

    word = str.split(" ")
    new_word = []
    for ele in word:
        if ele != "":
            new_word.append(ele)
    
    final_string  = ""
    next = ""
    print(new_word)
    for ele in a:
        for index, val in enumerate(new_word):
            if ele.lower() == val.lower():
                next = new_word[index+1]
        final_string += next + " "

    return final_string



a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

final_string = create_new_string(s,a)
print(final_string)

