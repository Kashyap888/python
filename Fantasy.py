def main():

    getdata=register()
    status_window(getdata)

def register():

    print("--------WELCOME TO THE TOWER--------")
    name=input("Enter Your Name : ")
    age=int(input("Enter your age : "))
    print("Select your class ? ")
    while True:
        job=int(input(("1.WARRIOR  2.MAGICIAN \n")))
        match job:
            case 1:
                job="WARRIOR"
                break
            case 2:
                job="MAGICIAN"
                break
            case _:
                print("Invaild choice")
    ui={"Name     ":name,
        "Age      ":age,
        "Class    ":job
        }
    return ui

def status_window(info):
    
    print("-------------------STATUS WINDOW------------------")
    for key, value in info.items():
        print(f"{key}: {value}")
    level()
    stats()
    print("---------------------------------------------------")

def stats():
    
    st={
        "Strength":1,
        "Agility ":1,
        "Hp      ":10,
        "Mp      ":5,
        "Wisdom  ":1,
        "                                 Unused points":0
    }
    print("\nSTATS : ")
    for key, value in st.items():
        print(f"{key} : {value}")

def level():
    lvl=[0,100]
    while True:
        if lvl[1]>=100:
            lvl[0]=lvl[0]+1
            lvl[1]=lvl[1]-100
        else:
            break

    print(f"Level    : {lvl[0]} \nExp      : {lvl[1]}")

def skills():
    return 0

def warrior():
    return 0

def magician():
    return 0

def inventory():
    return 0

def user_health():
    return 0

def monsters():
    return 0

def monsters_health():
    return 0

def shop():
    return 0

def rewards():
    return 0

if __name__ =="__main__":
    main()