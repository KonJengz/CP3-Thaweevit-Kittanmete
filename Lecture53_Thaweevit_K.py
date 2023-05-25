def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*0.07)
    return result

priceItem = int(input("ราคาสินค้า : "))
print("ราคารวม VAT =",vatCalculate(priceItem))