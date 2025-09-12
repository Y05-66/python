class Phone:
    IMEI = None
    producer = "小米"

    def call_by_5G(self):
        print("使用5G网络进行通话")


class MyPhone(Phone):
    producer = "华为"

    def call_by_5G(self):
        print("开启CUP单核模式，确保通话的时候省电")
        print("使用5G网络进行通话")
        print("关闭CUP单核模式，确保性能")


phone = MyPhone()
phone.call_by_5G()
print(phone.producer)
