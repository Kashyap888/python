name=(input("Enter your name ? "))
# writing to the file
with open("files.txt","a") as file:
    file.write(f"{name}\n")

# reading from the file
names =[]
with open("files.txt","r") as file:
    for line in file:
        names.append(line.rstrip())
for _ in sorted(names):
    print(f"Hello , {_}")