menuList = []
priceList = []
while True:
    menuName = input("ใส่ชื่อเมนู: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("ราคาของสินค้า: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    totalPrice = 0
    print("----- menu food -----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        totalPrice += priceList[i]
    print("ราคารวมทั้งหมด", totalPrice)

showBill()