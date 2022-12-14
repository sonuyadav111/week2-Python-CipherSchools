guess=1
winning_no=41
a=int(input("Enter a number between 1 to 100:"))
game_over= False
while not game_over:
    if a == winning_no:
        print(f"you won,you guessed the number in {guess} times")
        game_over= True
    else:
        if a<winning_no:
            print("low guess")
            guess+=1
            a=int(input("guess again:"))
        else:
            print("high guess")
            guess+=1
            a=int(input("guess again"))

