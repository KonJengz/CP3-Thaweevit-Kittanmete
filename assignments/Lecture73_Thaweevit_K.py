systemMenu = {"ข้าวมันไก่":50, "ข้าวขาหมู":60, "KFC":100, "โจ๊ก":40, "ข้าวผัด":55, "ไข่ดาว":10}

menuList = []
amountMenu = 0
while True:
    menuName = input("ใส่ชื่อเมนู: ")
    if (menuName.lower() == "exit"):
        break
    elif menuName in systemMenu.keys():
        amountMenu = int(input("จำนวน: "))
        menuPrice = systemMenu[menuName] * amountMenu
        menuList.append([menuName, menuPrice])
    else:
        print("คุณใส่รายการไม่ถูกต้อง")

def showBill():
    totalPrice = 0
    print("")
    print("------- menu food -------")
    for i in range(len(menuList)):
        print(menuList[i][0], amountMenu,"รายการ ราคา",menuList[i][1], "บาท")
        totalPrice += menuList[i][1]
    print("ราคารวมทั้งหมด", totalPrice, "บาท")

showBill()