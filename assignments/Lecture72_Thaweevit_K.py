menuList = []
while True:
    menuName = input("ใส่ชื่อเมนู: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("ราคา: "))
        menuList.append([menuName, menuPrice])

def showBill():
    totalPrice = 0
    print("")
    print("------ menu food ------")
    for i in range(len(menuList)):
        print(menuList[i][0], menuList[i][1], "บาท")
        totalPrice += menuList[i][1]
    print("ราคารวมทั้งหมด", totalPrice, "บาท")

showBill()