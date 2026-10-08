def displayColors(colors):
    # "displayColors" function displays the seven variables inputted from enterColors function.
    print("heres what you entered bro")
    for i in range(0, 6 + 1, 1):
        print(colors[i])

def enterColors(colors):
    # "enterColors" function allows inputting 7 items in an array variable.
    for i in range(0, 6 + 1, 1):
        print("bruh would you mind entering the " + str(i + 1) + " of the rainbow bro?")
        colors[i] = input()

# Main
# Main function declares "colors" variable then calls the functions necessary to the program.
colors = [""] * (7)

enterColors(colors)
displayColors(colors)
