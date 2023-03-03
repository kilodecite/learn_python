items = []

loops = [5, 2, 5, 2, 2]

for x in loops:
    string = ""
    for y in range(x):
        string = string + "x"
    print(string)

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