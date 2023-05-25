num = int(input("Number * : "))

for x in range(num):
    print("   " * (num-x), ((x+1)+x) * " * ")