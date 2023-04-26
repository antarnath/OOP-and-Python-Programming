class Phone:
    color = "black"
    features = ["camera", "water proof", "can be used as a hamar"]

    def call(self):
        print("ring ring ring")
    def send_sms(self, sms):
        print(sms)

my_phone = Phone()
my_phone.call()
my_phone.send_sms("Antar you are a bad guy")