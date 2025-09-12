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


class NFCReader:
    nfc_type = "第五代"
    producer = "小米"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("遥控控制")


class MyPone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPone()
phone.call_by_4G()
phone.read_card()
phone.write_card()
phone.control()
