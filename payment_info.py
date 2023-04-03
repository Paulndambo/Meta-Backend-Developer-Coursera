class PaySlip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount


    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
    
nathan = PaySlip("Nathan Kioko", "no", 1000)
roger = PaySlip("Rodgers Workfleek", "no", 34000)
nathan.pay()

print(nathan.status(), "\n", roger.status())
