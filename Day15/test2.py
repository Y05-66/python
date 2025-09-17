from turtle import *
# 绘制一个五角星

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 255, 50):
    drawStar(x, 0)

done()
