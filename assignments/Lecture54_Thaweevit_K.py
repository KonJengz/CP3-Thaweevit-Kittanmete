# login
def login():
    userName = "admin"
    password = "123"
    userNameInput = input("Username = ")
    passwordInput = input("Password = ")
    if userNameInput == userName and passwordInput == password:
        return shoeMenu()
    else:
        return login()

# สินค้าทั้งหมด
def shoeMenu():
    item1 = "รหัสสินค้า 001 : iPhone15"
    item2 = "รหัสสินค้า 002 : iPhone15 Pro"
    item3 = "รหัสสินค้า 003 : Samsung S23+"
    item4 = "รหัสสินค้า 004 : Samsung S23 Ultra"
    # ราคาของสินค้าทั้งหมด
    priceItem1 = 40000
    priceItem2 = 50000
    priceItem3 = 35000
    priceItem4 = 45000
    print("- - - - - - - - - - - - - - -")
    print("เลือกสินค้าที่ต้องการสั่งซื้ิอ")
    print(item1,"ราคา",priceItem1,"บาท")
    print(item2,"ราคา",priceItem2,"บาท")
    print(item3,"ราคา",priceItem3,"บาท")
    print(item4,"ราคา",priceItem4,"บาท")

    # เงื่อนไขของโปรแกรมสั่งซื้อสินค้า
    selectItem = selectMenu()
    if selectItem == "001":
        print("- - - - - - - - - - - - - - -")
        print(item1)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("เป็นจำนวนเงิน =", amountItem*priceItem1, "บาท")
        print("VAT =", vatCalculate(amountItem*priceItem1), "บาท")
        result = print("รวมเป็นจำนวนเงินทั้งหมด =", amountItem*priceItem1+vatCalculate(amountItem*priceItem1), "บาท")
        return result
    elif selectItem == "002":
        print("- - - - - - - - - - - - - - -")
        print(item2)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem2, "บาท")
        print("VAT =", vatCalculate(amountItem*priceItem2), "บาท")
        result = print("รวมเป็นจำนวนเงินทั้งหมด =", amountItem*priceItem2+vatCalculate(amountItem*priceItem2), "บาท")
        return result
    elif selectItem == "003":
        print("- - - - - - - - - - - - - - -")
        print(item3)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem3, "บาท")
        print("VAT =", vatCalculate(amountItem*priceItem3), "บาท")
        result = print("รวมเป็นจำนวนเงินทั้งหมด =", amountItem*priceItem3+vatCalculate(amountItem*priceItem3), "บาท")
        return result

    elif selectItem == "004":
        print("- - - - - - - - - - - - - - -")
        print(item4)
        amountItem = int(input("จำนวนที่ต้องการสั่งซื้ิอ : "))
        print("รวมเป็นจำนวนเงิน =", amountItem*priceItem4, "บาท")
        print("VAT =", vatCalculate(amountItem*priceItem4), "บาท")
        return "รวมเป็นจำนวนเงินทั้งหมด =",amountItem*priceItem4+vatCalculate(amountItem*priceItem4)
    
    else:
        print("คุณใส่รหัสสินค้าไม่ถูกต้อง")
        shoeMenu()

# โปรแกรมเลือกเมนู
def selectMenu():
    return input("ใส่รหัสสินค้าที่ต้องการสั้งซื้อ (ตัวอย่างเช่น 001) : ")

# โปรแกรมคำนวณ VAT
def vatCalculate(totalPrice):
    vat = 7
    return totalPrice * vat /100

print(login())