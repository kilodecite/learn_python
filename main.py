accounts = []
items = []
loops = [5, 2, 5, 2, 2]

for x in loops:
    string = ""
    for y in range(x):
        string = string + "x"
    print(string)

while True:
    user = input("Input name: ")
    accounts.append(user)
    command = input("stop(s)/next(n)/exit(e): ")
    if command == "s":
        print(accounts)
        break
    elif command == "n":
        ...
    elif command == "e":
        quit()
    else:
        print("Command not found!")

while True:
    index = input("Input index: ")
    if int(index) > len(accounts):
        print("ellement incorrect!")
    elif index.isdigit():
        print(accounts[int(index)])
        answer = input("stop(s)/next(n)/exit(e): ")
        if answer == "s":
            break
        elif answer == "n":
            ...
        elif answer == "e":
            quit()
        else:
            print("Please inputt correct command!")
    else:
        print("Please inputt correct index")

while True:
    while True:
        item = input("Input you item: ")
        item_convert = item.replace(".", "", 1)
        if item_convert.isdigit():
            item = float(item)
            break
        else:
            print("Please inputt correct digital")

    add = input("stop(s)/next(n)/exit(e): ")
    items.append(item)

    if add == "s":
        total = 0
        for price in items:
            total = total + price
        print(total)
        items.clear()
        while True:
            question = input("Countine program? (y/n): ")
            if question == "y":
                break
            elif question == "n":
                quit()
            else:
                print("Command not found!")

    elif add == "n":
        ...   
    elif add == "e":
        break
    else:
        print("Command not found!")

#end