import random


# Made with love for Alejandro Vaca


# I use this function for make the UX prettier.
def emoji(num):
    if num == 1:
        return "📄"
    elif num == 2:
        return "🪨"
    elif num == 3:
        return "✂️"
    elif num == 4:
        return "🦎"
    elif num == 5:
        return "🖖🏻"


name = input("Which are your name? ")
# I use this flag to controll the loop
Bandera = True

while Bandera:
    cp = random.randint(1, 5)
    print("Welcome to Paper, Rock, Scissors!")
    print("1. Paper 📄")
    print("2. Rock 🪨")
    print("3. Scissors ✂️")
    print("4. Lizard 🦎")
    print("5. Spock 🖖🏻")

    user = int(input("Choose: "))

    if user == 1:
        print(f"{name} chose Paper {emoji(user)} , CP chose {emoji(cp)}")
        if cp == 2 or cp == 5:
            print(f"The winner is: {name}")
        elif cp == 1:
            print("tie")
        else:
            print("CP wins")
    elif user == 2:
        print(f"{name} chose Rock {emoji(user)} , CP chose {emoji(cp)}")
        if cp == 4 or cp == 3:
            print(f"The winner is: {name}")
        elif cp == 2:
            print("tie")
        else:
            print("CP wins")
    elif user == 3:
        print(f"{name} chose Scissors {emoji(user)} , CP chose {emoji(cp)}")
        if cp == 4 or cp == 1:
            print(f"The winner is: {name}")
        elif cp == 3:
            print("tie")
        else:
            print("CP wins")
    elif user == 4:
        print(f"{name} chose Scissors {emoji(user)} , CP chose {emoji(cp)}")
        if cp == 5 or cp == 1:
            print(f"The winner is: {name}")
        elif cp == 4:
            print("tie")
        else:
            print("CP wins")
    elif user == 5:
        print(f"{name} chose Scissors {emoji(user)} , CP chose {emoji(cp)}")
        if cp == 3 or cp == 2:
            print(f"The winner is: {name}")
        elif cp == 5:
            print("tie")
        else:
            print("CP wins")
    else:
        print("Invalid option")

    print("You want to play again? (Y/N)")
    again = input().upper()
    if again == "Y":
        Bandera = True
    else:
        Bandera = False
