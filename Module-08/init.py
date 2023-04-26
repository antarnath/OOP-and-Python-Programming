class Phone:

    manufactured = "china"

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def send_sms(self, number, text):
        sms = f"sending: {text} to {number}"
        return sms

my_phone = Phone("samsung", 390000, "Black")
print(my_phone.manufactured)