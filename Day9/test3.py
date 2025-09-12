class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(1000, 500)


clock1 = Clock()
clock1.id = 1
clock1.price = 100
print(f"闹钟{clock1.id}的价格是{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = 1
clock2.price = 100
print(f"闹钟{clock2.id}的价格是{clock2.price}")
clock2.ring()
