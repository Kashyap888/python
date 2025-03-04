def main():
    bal=0
    while True:
        print("*******************BANK*************************")
        print("1.Deposit \n2.Withdraw \n3.Checkbalance \n4.Exit")
        print("************************************************")
        choic= choice("Enter your choice ? ")
        match choic:
            case 1:
                b=deposit("Enter the amount needs to be deposit ? $")
                bal=bal+b
                balance(bal)
            case 2:
                ba=withdraw("Enter the amount needs to be whithdrawn ? $")
                if ba>bal:
                    print("Insuffient Balance")
                else:
                    bal=bal-ba
                balance(bal)
            case 3:
                balance(bal)
            case 4:
                break
            case _:
                print("-----Invalid choice-----")

def choice(ch):
    while True:
        try:
            return int(input(ch))
        except ValueError:
            print("-----Invalid choice-----")

def deposit(d):
    while True:
        try:
            return float(input(d))
        except ValueError:
            print("Enter a valid amount")

def withdraw(w):
    while True:
        try:
            return float(input(w))
        except ValueError:
            print("Enter a valid amount")


def balance(balan):
    print(f"Balance = ${balan:.2f}")
    

main()