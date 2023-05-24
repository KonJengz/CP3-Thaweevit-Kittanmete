# login
userNameInput = input("Username = ")
passwordInput = input("Password = ")

userName = "admin"
password = "1234"

# สินค้าทั้งหมด
item1 = "รหัสสินค้า 001 : iPhone15"
item2 = "รหัสสินค้า 002 : iPhone15 Pro"
item3 = "รหัสสินค้า 003 : Samsung S23+"
item4 = "รหัสสินค้า 004 : Samsung S23 Ultra"

# ราคาของสินค้าทั้งหมด
priceItem1 = 40000
priceItem2 = 50000
priceItem3 = 35000
priceItem4 = 45000

# เงื่อนไขของโปรแกรมสั่งซื้อสินค้า
if userNameInput == userName and passwordInput == password:
    print("- - - - - - - - - - - - - - -")
    print("เลือกสินค้าที่ต้องการสั่งซื้ิอ")
    print(item1,"ราคา",priceItem1,"บาท")
    print(item2,"ราคา",priceItem2,"บาท")
    print(item3,"ราคา",priceItem3,"บาท")
    print(item4,"ราคา",priceItem4,"บาท")
    selectItem = input("ใส่รหัสสินค้าที่ต้องการสั้งซื้อ (ตัวอย่างเช่น 001) : ")
    if selectItem == "001":
        print("- - - - - - - - - - - - - - -")
        print(item1)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem1, "บาท")
    elif selectItem == "002":
        print("- - - - - - - - - - - - - - -")
        print(item2)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem2, "บาท")
    elif selectItem == "003":
        print("- - - - - - - - - - - - - - -")
        print(item3)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem3, "บาท")
    elif selectItem == "004":
        print("- - - - - - - - - - - - - - -")
        print(item4)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem4, "บาท")
    else:
        print("คุณใส่รหัสสินค้าไม่ถูกต้อง")