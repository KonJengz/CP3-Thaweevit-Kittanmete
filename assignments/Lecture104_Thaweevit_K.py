class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to cart", self.name, self.lastName, self.age)

customer1 = Customer()
customer1.name = "Jengz"
customer1.lastName = "Thawee"
customer1.age = 30
customer1.addCart()

customer1 = Customer()
customer1.name = "Game"
customer1.lastName = "Pinya"
customer1.age = 35
customer1.addCart()

customer1 = Customer()
customer1.name = "Ball"
customer1.lastName = "Motionless"
customer1.age = 32
customer1.addCart()