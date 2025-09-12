class Phone:
    __current_voltage = None

    def __keep_single_core(self):
        print("让CUP以单核模式运行")


phone = Phone()
# 错误的访问
print(phone.__current_voltage)
