import turtle
import math
import random


def setup_canvas():
    """设置画布"""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#f0f8ff")  # 使用更柔和的浅蓝色背景
    screen.title("花香自有人欣赏")
    screen.tracer(0)  # 关闭自动刷新，提高绘制速度
    return screen


def create_pen():
    """创建并配置画笔"""
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    return pen


def draw_rose_petals(t, radius, num_segments):
    """
    绘制玫瑰花的花瓣部分，带有渐变颜色效果
    """
    # 花瓣颜色从深红到粉红渐变
    colors = [
        "#8B0000", "#A52A2A", "#B22222", "#CD5C5C",
        "#DC143C", "#FF0000", "#FF6347", "#FF69B4"
    ]

    t.penup()
    t.goto(0, 80)
    t.pendown()

    for i in range(num_segments):
        # 根据进度选择颜色
        color_idx = min(int(i / num_segments * len(colors)), len(colors) - 1)
        t.pencolor(colors[color_idx])
        t.fillcolor(colors[color_idx])

        # 绘制花瓣
        t.begin_fill()
        t.circle(radius - i * (radius / num_segments * 0.7), 90)
        t.left(90)
        t.circle(radius - i * (radius / num_segments * 0.7), 90)
        t.left(18)
        t.end_fill()


def draw_stem(t, length):
    """绘制带有自然弯曲的花茎"""
    t.penup()
    t.goto(0, 0)
    t.setheading(270)
    t.pendown()

    # 花茎颜色渐变
    colors = ["#2E8B57", "#3CB371", "#20B2AA"]
    t.pensize(7)

    for i in range(length):
        if i % 30 == 0:
            # 轻微随机弯曲，使花茎更自然
            t.left(random.uniform(-5, 5))
        color_idx = min(int(i / length * len(colors)), len(colors) - 1)
        t.pencolor(colors[color_idx])
        t.forward(1)


def draw_leaf(t, x, y, angle, size):
    """绘制更真实的叶子"""
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    # 叶子颜色
    leaf_colors = ["#228B22", "#32CD32", "#008000"]
    t.fillcolor(random.choice(leaf_colors))
    t.pencolor("#006400")

    t.begin_fill()
    # 绘制更自然的叶子形状
    t.circle(size, 90)
    t.left(30)
    t.circle(size * 0.7, 60)
    t.left(60)
    t.circle(size * 0.9, 60)
    t.left(30)
    t.circle(size, 90)
    t.end_fill()

    # 添加叶脉
    t.penup()
    t.goto(x, y)
    t.setheading(angle + 45)
    t.pendown()
    t.pencolor("#556B2F")
    t.pensize(1)
    t.forward(size * 0.8)


def draw_thorns(t, stem_length):
    """在花茎上随机绘制刺"""
    t.pencolor("#654321")
    t.fillcolor("#8B4513")

    for i in range(10, stem_length, 30):
        if random.random() > 0.3:  # 70%概率绘制刺
            y_pos = -i
            x_pos = random.choice([-10, 10])  # 左右随机
            size = random.uniform(5, 15)

            t.penup()
            t.goto(x_pos, y_pos)
            t.setheading(270 + random.uniform(-30, 30))
            t.pendown()

            t.begin_fill()
            t.forward(size)
            t.left(135)
            t.forward(size / math.sqrt(2))
            t.left(135)
            t.forward(size)
            t.end_fill()


def draw_rose():
    """绘制完整的玫瑰花"""
    screen = setup_canvas()
    pen = create_pen()

    # 绘制花瓣
    draw_rose_petals(pen, 180, 180)

    # 绘制花茎
    draw_stem(pen, 350)

    # 绘制叶子
    draw_leaf(pen, -60, -100, 220, 60)
    draw_leaf(pen, 60, -200, 320, 55)
    draw_leaf(pen, -50, -180, 200, 45)  # 添加第三片叶子

    # 绘制刺
    draw_thorns(pen, 350)

    # 添加装饰性元素
    pen.penup()
    pen.goto(-300, 300)
    pen.pencolor("#FFD700")
    pen.write("花香自有人欣赏", font=("楷体", 24, "bold"))

    screen.update()  # 更新画布
    screen.mainloop()


if __name__ == "__main__":
    draw_rose()