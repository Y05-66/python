class Phone:
    IMEI = None
    producer = "小米"

    def call_by_4G(self):
        print("4G通话")


class Phone2025(Phone):
    face_id = "10001"

    def call_by_5G(self):
        print("5G通话")


phone = Phone2025()
print(phone.producer)
phone.call_by_4G()
phone.call_by_5G()
