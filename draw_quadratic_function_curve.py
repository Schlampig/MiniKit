import numpy as np
import matplotlib.pyplot as plt


def name_y(a, b, c):
    """
    根据二次函数系数，生成并返回二次函数表达式字符串
    """
    a_part = "" if a == 0 else str(a) + "x^2"

    if b < 0:
        b_part = str(b) + "x"
    elif b == 0:
        b_part = ""
    else:
        b_part = str(b) + "x" if len(a_part) == 0 else "+" + str(b) + "x"

    if c < 0:
        c_part = str(c)
    elif c == 0:
        c_part = ""
    else:
        c_part = str(c) if len(a_part) == 0 and len(b_part) == 0 else "+" + str(c)

    y_name = a_part + b_part + c_part
    return y_name


def draw_quadratic_function_curve(coef, n_points=1000, x_size=[-10, 10], fig_size=[6, 6], is_grid=False, is_save=False):
    """
    根据输入的二次函数系数，绘制二次函数曲线（包含一次函数和常数）
    :param coef: list[int/float, int/float, int/float], 二次函数表达式 ax^2 + bx + c 的系数列表
    :param n_points: int, 绘制的样本点个数
    :param x_size: list[int/float, int/float], 定义域
    :param fig_size: list[int, int], 画布尺寸（高与宽）
    :param is_save: bool, 是否保存画布
    :return: None
    """
    # 设置画布
    fig_width, fig_height = fig_size[0], fig_size[1]
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # 计算函数（曲线）相关值
    a, b, c = coef[0], coef[1], coef[2]
    x = np.linspace(x_size[0], x_size[1], n_points)

    # 绘制曲线
    y = a*(x**2) + b*x + c
    y_name = name_y(a, b, c)
    if is_grid:
        ax.plot(x, y)
        ax.grid(color="skyblue", ls="--")
        ax.set_title(y_name)
    else:
        ax.plot(x, y, label=y_name, color="steelblue")
        ax.legend()
    if is_save:
        plt.draw()
        y_name += ".png"
        plt.savefig(y_name)
    else:
        plt.show()
    plt.close()
    return None


if __name__ == "__main__":
    draw_quadratic_function_curve(coef=[-2, 3, 0.1], is_grid=True, is_save=True)
