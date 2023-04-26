number = int(input())
fast=0
second=1
# nextValue
if number >= 1:
    print(fast,end=" ")
if number >= 2:
    print(second,end=" ")
if number > 2:
    for i in range(0,number-2):
        nextValue=fast+second
        print(nextValue,end=" ")
        fast=second
        second=nextValue