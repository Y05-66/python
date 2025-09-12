import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    # 创建唱歌的线程
    t1 = threading.Thread(target=sing,args=("正在唱歌...",))
    #  创建跳舞的线程
    t2 = threading.Thread(target=dance,kwargs={"msg":"正在跳舞..."})
    t1.start()
    t2.start()
