import os
from PIL import Image, ImageDraw

# 配置颜色接口，每个类别可指定一个颜色
CLASS_COLORS = {
    0: (0, 0, 255),  # 类别 0：蓝色
    1: (135, 206, 235),  # 类别 1：天蓝色
    2: (211, 211, 211),  # 类别 2：灰色
    3: (34, 139, 34),  # 类别 3：森林绿
    4: (255, 165, 0),  # 类别 4：橙色
    5: (255, 0, 0)  # 类别 5：红色

    # 可以添加更多类别颜色
}

def visualize_yolo_labels(image_folder, label_folder, output_folder, class_colors=CLASS_COLORS):
    """
    将 YOLO 格式的检测标签可视化到图像上，并保存到指定文件夹中。

    :param image_folder: 包含图像的文件夹路径
    :param label_folder: 包含 YOLO 格式标签的文件夹路径
    :param output_folder: 输出图像的文件夹路径
    :param class_colors: 字典，指定每个类别的颜色
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取图像和标签文件列表
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])
    label_files = sorted([f for f in os.listdir(label_folder) if f.endswith('.txt')])

    for image_file, label_file in zip(image_files, label_files):
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, label_file)
        output_path = os.path.join(output_folder, image_file)

        # 加载图像
        image = Image.open(image_path)
        # 如果图像是灰度图，将其转换为 RGB 图像
        if image.mode != 'RGB':
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)

        # 获取图像宽高
        w, h = image.size

        # 读取标签并绘制矩形框
        with open(label_path, 'r') as f:
            for line in f.readlines():
                data = line.strip().split()
                if len(data) < 5:
                    print(f"标签格式错误: {label_path}, 行: {line}")
                    continue

                class_id = int(data[0])  # 类别索引
                x_center, y_center, bbox_width, bbox_height = map(float, data[1:])

                # 转换 YOLO 格式为像素坐标
                x1 = int((x_center - bbox_width / 2) * w)
                y1 = int((y_center - bbox_height / 2) * h)
                x2 = int((x_center + bbox_width / 2) * w)
                y2 = int((y_center + bbox_height / 2) * h)

                # 获取指定类别的颜色
                color = class_colors.get(class_id, (255, 255, 255))  # 默认为白色

                # 绘制矩形框
                draw.rectangle([x1, y1, x2, y2], outline=color, width=4)
                # 可以在矩形框旁边绘制类别标签（如需要）
                #draw.text((x1, y1 - 10), f"Class {class_id}", fill=color)

        # 保存可视化图像
        image.save(output_path)
        print(f"保存可视化图像: {output_path}")

if __name__ == "__main__":
    # 示例文件夹路径
    image_folder = r"G:\2024F_10_16\双光检测-Mambayolo\可视化\vis_m3fd\test"  # 图像文件夹路径
    label_folder = r"G:\2024F_10_16\双光检测-Mambayolo\可视化\vis_m3fd\labels"  # YOLO 标签文件夹路径
    output_folder = r"G:\2024F_10_16\双光检测-Mambayolo\可视化\vis_m3fd\test_gt"  # 输出文件夹路径

    # 可视化并保存图像
    visualize_yolo_labels(image_folder, label_folder, output_folder)
