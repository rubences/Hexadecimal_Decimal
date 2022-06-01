choice = input("Enter [H] to change hexadecimal to decimal or [D] to change decimal to hexadecimal: ")

def hextodec(x):
    num = 0
    counter = 0
    total = 0
    if x.isnumeric() == False:
        hexlist = alphatonum(x)
        for i in range(len(hexlist)):
            num = int(hexlist[i]) * (16 ** counter)
            total += num
            counter += 1
        return total
    else:
        for i in range(len(x)):
            num = int(x[i]) * (16 ** counter)
            total += num
            counter += 1
        return total

def dectohex(x):
    result = x
    num = int(x)
    hexlist = []
    answer = ""
    while result != 0:
        result = num // 16
        remainder = str(num % 16).split(" ")
        num = result
        hexlist = remainder + hexlist
    for i in range(len(hexlist)):
        if int(hexlist[i]) > 9:
            hexlist = numtoalpha(hexlist, i)
    for j in range(len(hexlist)):
        answer += str(hexlist[j])
    return answer

def alphatonum(y):
    hexlist = list(y)
    if y.find("A") != -1:
        location = hexlist.index("A")
        hexlist[location] = 10
    if y.find("B") != -1:
        location = hexlist.index("B")
        hexlist[location] = 11
    if y.find("C") != -1:
        location = hexlist.index("C")
        hexlist[location] = 12
    if y.find("D") != -1:
        location = hexlist.index("D")
        hexlist[location] = 13
    if y.find("E") != -1:
        location = hexlist.index("E")
        hexlist[location] = 14
    if y.find("F") != -1:
        location = hexlist.index("F")
        hexlist[location] = 15
    return hexlist

def numtoalpha(y, z):
    hexlist = y
    if int(y[z]) == 10:
        hexlist[z] = "A"
        return hexlist
    if int(y[z]) == 11:
        hexlist[z] = "B"
        return hexlist
    if int(y[z]) == 12:
        hexlist[z] = "C"
        return hexlist
    if int(y[z]) == 13:
        hexlist[z] = "D"
        return hexlist
    if int(y[z]) == 14:
        hexlist[z] = "E"
        return hexlist
    if int(y[z]) == 15:
        hexlist[z] = "F"
        return hexlist
        
if choice == "H":
    hexnum = input("\nEnter a hexadecimal number: ")
    hnum = hexnum[::-1]
    answer = hextodec(hnum)
    print("\n" + hexnum + " in decimal: " + str(answer))
elif choice == "D":
    decnum = input("\nEnter a decimal number: ")
    answer = dectohex(decnum)
    print("\n" + decnum + " in hexadecimal: " + answer)
else:
    print("\nInvalid input.")