import time
import threading


def sing():
    while True:
        print("正在唱歌...")
        time.sleep(1)


def dance():
    while True:
        print("正在跳舞...")
        time.sleep(1)


if __name__ == "__main__":
    # 创建唱歌的线程
    t1 = threading.Thread(target=sing)
    #  创建跳舞的线程
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
