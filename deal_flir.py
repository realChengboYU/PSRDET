import os
import shutil

# 文件夹路径
image_folder = "/home/dell/桌面/sdd/gmdetr_flir/align_dual/images/test"  # 图像文件所在文件夹
txt_folder = "/home/dell/桌面/sdd/gmdetr_flir/align/labels"    # TXT 文件所在文件夹
output_folder = "/home/dell/桌面/sdd/gmdetr_flir/align_dual/labels/test" # 目标文件夹

# 确保目标文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 获取 a 文件夹中所有图像文件的名称（去掉扩展名）
image_names = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))}

# 遍历 b 文件夹，找到同名的 .txt 文件并复制到 c 文件夹
for txt_file in os.listdir(txt_folder):
    if txt_file.endswith(".txt"):
        txt_name = os.path.splitext(txt_file)[0]  # 提取文件名（不带扩展名）
        if txt_name in image_names:  # 检查是否与 a 文件夹中的图像同名
            src_path = os.path.join(txt_folder, txt_file)
            dst_path = os.path.join(output_folder, txt_file)
            shutil.copy(src_path, dst_path)
            print(f"Copied {txt_file} to {output_folder}")
