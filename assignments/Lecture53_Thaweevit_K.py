def vatCalculate(totalPrice):
    return totalPrice + (totalPrice*0.07)

priceItem = int(input("ราคาสินค้า : "))
print("ราคารวม VAT =",vatCalculate(priceItem))