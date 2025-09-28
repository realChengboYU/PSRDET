import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo(xml_folder, image_folder, output_folder, class_mapping):
    """
    将 Pascal VOC 格式的 XML 标签转换为 YOLO 格式。

    :param xml_folder: 存放 XML 标签文件的文件夹路径
    :param image_folder: 存放图像文件的文件夹路径
    :param output_folder: 转换后的 YOLO 标签文件保存路径
    :param class_mapping: 类别映射字典，将类别名称映射为整数
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取 XML 文件列表
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]

    for xml_file in xml_files:
        xml_path = os.path.join(xml_folder, xml_file)
        image_path = os.path.join(image_folder, xml_file.replace('.xml', '.jpg'))  # 假设图像为 .jpg 格式
        output_path = os.path.join(output_folder, xml_file.replace('.xml', '.txt'))

        # 解析 XML 文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 获取图像尺寸
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # 打开输出文件
        with open(output_path, 'w') as output_file:
            # 遍历所有的 object 标签
            for obj in root.findall('object'):
                class_name = obj.find('name').text  # 获取类别名称
                if class_name not in class_mapping:
                    print(f"警告：在类映射中找不到类别: {class_name}")
                    continue
                class_id = class_mapping[class_name]  # 类别映射为 ID

                # 获取边界框坐标
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)

                # 将边界框转换为 YOLO 格式（中心点坐标和宽高归一化）
                x_center = (xmin + xmax) / 2.0 / width
                y_center = (ymin + ymax) / 2.0 / height
                bbox_width = (xmax - xmin) / float(width)
                bbox_height = (ymax - ymin) / float(height)

                # 写入 YOLO 格式的标签
                output_file.write(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")

        print(f"转换完成：{output_path}")

if __name__ == "__main__":
    # 示例文件夹路径
    xml_folder = r"G:\2024F_10_16\双光检测-Mambayolo\align\Annotations"  # XML 标签文件夹路径
    image_folder = r"G:\2024F_10_16\双光检测-Mambayolo\align\JPEGImages"  # 图像文件夹路径
    output_folder = r"G:\2024F_10_16\双光检测-Mambayolo\align\labels"  # YOLO 标签输出文件夹路径

    # 类别映射：将类别名称映射为整数 ID
    class_mapping = {
        'person': 0,
        'car': 1,
        'bicycle': 2,
        # 在此处添加更多类别映射
    }

    # 转换 XML 标签为 YOLO 格式
    convert_xml_to_yolo(xml_folder, image_folder, output_folder, class_mapping)
