money = 5000000
name = None
name = input("请输入你的名字：")

def query(show_header):
    if show_header:
        print("---------查询余额------------")
        print(f"{name},您好，你的余额剩余：{money}元")

def saving(num):
    global money
    money += num
    print("-------------存款-------------")
    print(f"{name},您好，您存款{num}元，成功！")

    query(False)

def get_money(num):
    global money
    money -= num
    print("-----------取款------------")
    print(f"{name},您好，您取款{num}元，成功！")
    query(False)

def main():
    print("----------主菜单------------")
    print(f"{name},您好，欢迎使用ATM机。请选择菜单：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择：")
while True:
    choice = main()
    if choice == "1":
        query(True)
        continue
    elif choice == "2":
        num = int(input("请输入存款金额："))
        saving(num)
        continue
    elif choice == "3":
        num = int(input("请输入取款金额："))
        get_money(num)
        continue
    else :
        print("欢迎下次再来！")
        break