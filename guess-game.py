import random
def main():
        print("********** GUESS  THE  NUMBER  GAME **********")
        st=int(input("ENTER THE STARTING RANGE : "))
        ed=int(input("ENTER THE ENDING RANGE : "))
        number = random.randint(st, ed)
        attempts=0
        while True:
                guess=int(input("Guess the number : "))
                attempts +=1
                if guess>number:
                        print("TOO HIGH !! TRY AGAIN !!")
                elif guess<number:
                        print("TOO LOW !! TRY AGAIN !!")
                else:
                        print(f"CORRECT !! \nYOU GUESSED THE NUMBER {number} in {attempts} Attempts")
                        break



main()