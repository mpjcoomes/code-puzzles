a = "bottles of beer"
b = "on the wall"
c = "Take one down, pass it around"

for i in range(99, 0, -1):
    if i > 2:
        print(i, a, b, "\n" + str(i), a, "\n" + c, "\n" + str(i - 1), a, b, "\n")
    elif i == 2:
        print( i, a, b, "\n" + str(i), a, "\n" + c, "\n" + str(i - 1), a.replace("s", ""), b, "\n", )
    else:
        print( i, a.replace("s", ""), b, "\n" + str(i), a.replace("s", ""), "\n" + c, "\n" + str(i - 1), a, b, "\n", )
