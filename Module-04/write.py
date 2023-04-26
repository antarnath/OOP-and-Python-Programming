# with open("message.txt","w") as fileWrite:
#     fileWrite.write("Hello Antar Chandra Nath")


# import itertools
# for i in itertools.count(start=1):
#     if 

temp = {}
for i in range(1, 500):
    students_name = input()
    students_mark = input()
    temp[students_name]=students_mark
id = 1
with open("text.txt","w") as fileWrite:
    for key, val in temp.items():
        fileWrite.write("%s: name:%s,marks=%s\n" % (id,key,val))
        id+=1
