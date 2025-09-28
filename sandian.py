import matplotlib.pyplot as plt
import numpy as np


def plot_scatter_with_labels_and_styles(x_coords, y_coords, labels, markers, colors, sizes, title='Scatter Plot',
                                        xlabel='X-Axis', ylabel='Y-Axis'):
    """
    绘制带有标签的散点图，每个散点的形状、颜色和大小都不同
    :param x_coords: 散点的X坐标（列表或数组）
    :param y_coords: 散点的Y坐标（列表或数组）
    :param labels: 每个散点的标签（列表或数组）
    :param markers: 每个散点的形状（列表或数组，如'o', 's', 'D', etc.）
    :param colors: 每个散点的颜色（列表或数组，颜色可以是字符串或RGB元组）
    :param sizes: 每个散点的大小（列表或数组，散点的面积）
    :param title: 图表标题（默认为 'Scatter Plot'）
    :param xlabel: X轴标签（默认为 'X-Axis'）
    :param ylabel: Y轴标签（默认为 'Y-Axis'）
    """
    # 绘制每个散点
    for i in range(len(x_coords)):
        plt.scatter(x_coords[i], y_coords[i], marker=markers[i], color=colors[i], s=sizes[i],
                    label=labels[i])  # 每个散点形状、颜色和大小不同

    plt.title(title)  # 设置图表标题
    plt.xlabel(xlabel)  # 设置X轴标签
    plt.ylabel(ylabel)  # 设置Y轴标签

    # 添加每个散点的标签
    for i, label in enumerate(labels):
        # 增加标签位置的偏移量，避免标签超出图表范围
        plt.text(x_coords[i], y_coords[i], label, fontsize=9, ha='left', va='bottom')

    plt.grid(True)  # 显示网格
    #plt.legend()  # 显示图例
    #plt.show()  # 显示图表
    plt.savefig('M3FD.svg')


# 示例：输入坐标、标签、形状、颜色和大小
x_coords = [142, 55, 33, 84, 36, 111, 60, 65]
y_coords = [52.4, 53.1, 54.2, 51.0, 57.7, 58.0, 39.8, 60.7]
labels = ['MambaYOLO', 'RTDETR', 'GMDETR', 'SLBAF', 'CFT', 'DEFCF', 'ICAFusion', 'Ours']
markers = ['o', 's', '^', 'o', 'd', 'h', 'H', '*']  # 每个散点的形状
colors = ['cyan', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'red']  # 每个散点的颜色
# 自动生成 sizes
sizes = 100 + 100 * (np.array(y_coords) - np.min(y_coords)) / (np.max(y_coords) - np.min(y_coords))  # 映射到 100 到 1000 之间


# 绘制带标签的散点图，每个散点的形状、颜色和大小都不一样
plot_scatter_with_labels_and_styles(x_coords, y_coords, labels, markers, colors, sizes, title='On M3FD', xlabel='FPS', ylabel='mAP50:95')
