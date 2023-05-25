num = int(input("Number"))

for x in range(num):
    text = ""
    for i in range(x+1):
        textGap = "   " * (num - x)
        text = (x+(x+1)) * " * "
    print(textGap,text)
