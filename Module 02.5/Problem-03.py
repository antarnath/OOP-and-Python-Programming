Player_1 = input()
Player_2 = input()

if(Player_1=="rock" and Player_2=="scissors")or(Player_1=="scissors" and Player_2=="rock"):
    print("Rock is the winner")
elif(Player_1=="paper" and Player_2=="rock")or(Player_1=="rock" and Player_2=="paper"):
    print("Paper is the winner")
elif(Player_1=="scissors" and Player_2=="paper")or(Player_1=="paper" and Player_2=="scissors"):
    print("Scissors is the winner")