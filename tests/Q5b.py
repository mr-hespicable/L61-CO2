def displayMenu():
    menu = "Choose from these three options:\n" + "1. Enter data about town names and populations\n" + "2. Print out the name of the town with the largest population\n" + "3. End program\n"
    return input(menu)


def enterData():
    f = open("file.txt", "w")
    print("Enter records here, or enter 'exit' to return to the main program.")
    i = input()
    g = []
    while i != "exit":
        g.append(i)
        i = input()
    f.write('\n'.join(g))
    f.close()
             

def calculateData():
    f = open("file.txt", "r")
    mx = max([int(g.split(",")[1]) for g in f.readlines()])
    print("calculating data...")
    print(f"highest population is {mx}")
    f.close()


choice = displayMenu()

while True:
    match choice:
        case "1":
            enterData()
            print('\n') 
        case "2":
            calculateData()
            print('\n') 
        case "3":
            print("exiting program!")
            exit()

    choice = displayMenu()
