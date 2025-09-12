import turtle
import math

# --- 1. 设置画布 ---
screen = turtle.Screen()
screen.setup(width=800, height=800)  # 设置窗口大小
screen.bgcolor("lightblue")  # 设置背景颜色
screen.title("花香自有人欣赏")  # 设置窗口标题

# --- 2. 创建画笔 ---
pen = turtle.Turtle()
pen.speed(0)  # 0 是最快速度，方便观看生成过程
pen.hideturtle()  # 隐藏乌龟图标


# --- 3. 绘制花瓣函数 ---
def draw_rose_petals(t, radius, num_segments, color):
    """
    绘制玫瑰花的花瓣部分，通过重复绘制弧线和旋转来形成螺旋状的花朵。
    t: turtle画笔对象
    radius: 初始弧线半径
    num_segments: 组成花朵的弧线段数量，越多越密
    color: 花瓣颜色
    """
    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(2)

    # 移动到花朵中心偏上位置开始绘制
    t.penup()
    t.goto(0, 80)  # 将花朵起始位置设置在画布中央偏上
    t.pendown()

    for i in range(num_segments):
        # 渐变色效果 (可选，取决于你的turtle版本和需求)
        # 这里尝试模拟一个从深到浅的红色渐变
        # R值从0.8 (深红) 逐渐增加到1.0 (亮红)
        # G和B值保持0，使得颜色始终在红色系
        # try:
        #    t.pencolor(0.8 + i * 0.2 / num_segments, 0, 0) # 逐渐变亮
        # except turtle.TurtleGraphicsError:
        #    pass # 某些turtle版本不支持RGB元组，跳过

        # 绘制一个弧线，半径逐渐减小，形成向内收缩的效果
        t.circle(radius - i * (radius / num_segments * 0.8), 90)

        # 旋转，使下一段弧线形成花瓣重叠效果
        t.left(90)  # 向左转90度
        t.circle(radius - i * (radius / num_segments * 0.8), 90)  # 绘制第二段弧线
        t.left(18)  # 向左转18度，控制花瓣的旋转密度


# --- 4. 绘制花茎函数 ---
def draw_stem(t, stem_length, stem_thickness, color):
    """
    绘制花茎。
    t: turtle画笔对象
    stem_length: 花茎长度
    stem_thickness: 花茎粗细
    color: 花茎颜色
    """
    t.penup()
    t.goto(0, 0)  # 定位到花朵下方
    t.setheading(270)  # 面朝下方
    t.pendown()

    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(stem_thickness)
    t.forward(stem_length)


# --- 5. 绘制叶子函数 ---
def draw_leaf(t, x, y, angle, leaf_size, color):
    """
    绘制一片叶子。
    t: turtle画笔对象
    x, y: 叶子起始位置
    angle: 叶子方向
    leaf_size: 叶子大小
    color: 叶子颜色
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle)

    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(1)

    t.begin_fill()
    # 绘制叶子形状（两个半圆拼接）
    t.circle(leaf_size, 90)
    t.left(90)
    t.circle(leaf_size, 90)
    t.end_fill()


# --- 6. 绘制刺函数 (可选) ---
def draw_thorn(t, x, y, angle, thorn_size, color):
    """
    绘制一个玫瑰刺。
    t: turtle画笔对象
    x, y: 刺的起始位置
    angle: 刺的方向
    thorn_size: 刺的大小
    color: 刺的颜色
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle)

    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(1)

    t.begin_fill()
    t.forward(thorn_size)
    t.left(135)
    t.forward(thorn_size / math.sqrt(2))  # 根据勾股定理计算斜边
    t.left(135)
    t.forward(thorn_size)
    t.end_fill()


# --- 7. 调用函数绘制玫瑰花 ---
if __name__ == "__main__":
    # 绘制花瓣
    draw_rose_petals(pen, 150, 150, "red")  # 半径150，150段弧线，红色

    # 绘制花茎
    draw_stem(pen, 300, 7, "forestgreen")  # 长度300，粗细7，森林绿

    # 绘制叶子
    # 左侧叶子
    draw_leaf(pen, -60, -100, 220, 50, "green")
    # 右侧叶子
    draw_leaf(pen, 60, -200, 320, 50, "green")

    # 绘制刺
    draw_thorn(pen, 15, -150, 270 + 45, 15, "darkgray")  # 右侧上方
    draw_thorn(pen, -15, -250, 270 - 45, 15, "darkgray")  # 左侧下方

    # 保持窗口显示直到手动关闭
    screen.mainloop()