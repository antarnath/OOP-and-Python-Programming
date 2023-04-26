# numbers = [12, 45, 56, 45, 12, 89]
marks = {'physics':12, 'chemistry':45, 'math':56,}
# print(marks)
marks['math'] = 56.5
marks['english'] = 89
# del marks['chemistry']
print(marks)
marks_keys = marks.keys()
marks_value = marks.values()
# print(marks_keys)
# print(marks_value)
# marks.pop('physics')
# print(marks)
# marks.clear()
# print(marks)
# marks_items = marks.items()
# print(marks_items)
# for key,value in marks.items():
#     print(key,value)

tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4127
# print(tel)
# print(list(tel))
# print(sorted(tel))
a = 'guido' in tel
# print(a)
# print('guido' in tel)