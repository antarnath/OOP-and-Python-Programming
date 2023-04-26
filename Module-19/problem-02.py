import os

file = open('Test.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.center(os.get_terminal_size().columns))