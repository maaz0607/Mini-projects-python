import random



print("--ROCK--PAPER--SCISSORS--GAME--")
while True:
    best=input("First to how many wins: ")
    if best.isdigit():
        best=int(best)
        if best<=0:
            print("Enter valid, positive integer.")
        else:
            break
    else:
        print("Enter valid integer.")
u_wins,c_wins=0,0

beats={"rock":["scissors","lizard"],
       "scissors":["paper","lizard"],
       "paper":["spock","rock"],
       "spock":["scissors","rock"],
       "lizard":["spock","paper"]}

while True:
    u_choice=input("Choose- ROCK / PAPER / SCISSORS / LIZARD / SPOCK / QUIT - ").strip().lower()

    if u_choice=="quit":
        print("\nExiting game.")
        break
    if u_choice not in beats:
        print("\nPlease enter valid option.")
        continue
    c_choice=random.choice(list(beats))
    print("\n--Computer picked--",c_choice)
    if u_choice==c_choice:
        print("\n--Tie between ",u_choice,"and",c_choice)

    elif c_choice in beats[u_choice]:
        u_wins+=1
        print("\n--You won--")  
        if u_wins==best:
            print("--You Won the Game")
            break
    
    else:
        print("\n--You lost--")
        c_wins+=1
        if c_wins==best:
            print("--You Lost the Game")
            break
    print("\n--Score--\n Your wins- ",u_wins,"\nComputer wins- ",c_wins)
print("\n--GAME OVER--\n--Final Score--\nYour wins- ",u_wins,"\nComputer wins- ",c_wins)
    
