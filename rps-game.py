import random
def main():
    while True:
        print("***********GAME*************")
        print("1.ROCK \n2.PAPER \n3.SCISSOR")
        print("*****************************")
        user=user_choice("enter your choice ? ")
        user=user.upper()
        comp=computer_choice()
        print("YOUR CHOICE : ",user)
        print("COMPUTER : ",comp)
        print("-------------",result(user,comp),"-----------------")


def computer_choice():
    return random.choice(["ROCK","PAPER","SCISSOR"])

def user_choice(uc):
    return (input(uc))
    

def result(u,c):
    match u:
        case "ROCK":
            if c=="ROCK":
                return "TIE !!"
            elif c=="PAPER":
                return "YOU LOST !!"
            else:
                return "YOU WON !!"
        case "PAPER":
            if c=="SCISSOR":
                return "YOU LOST !!"
            elif c=="ROCK":
                return "YOU WON !!"
            else:
                return "TIE !!"
        case "SCISSOR":
            if c=="SCISSOR":
                return "TIE !!"
            elif c=="ROCK":
                return "YOU LOST !!"
            else:
                return "YOU WON !!"
        case _:
            return "USER AS ENTERED AN INVALUD CHOICE"
main()