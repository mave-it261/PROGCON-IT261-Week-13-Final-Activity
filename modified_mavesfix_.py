def displayColors(colors):
    print("heres what you entered bro")
    for i in range(0, 6 + 1, 1):
        print(colors[i])

def enterColors(colors):
    for i in range(0, 6 + 1, 1):
        print("bruh would you mind entering the " + str(i + 1) + " of the rainbow bro?")
        colors[i] = input()

# Main
colors = [""] * (7)

enterColors(colors)
displayColors(colors)
