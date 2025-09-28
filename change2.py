import os
import shutil

def move_and_rename_images(src_folder, dest_folder):
    """
    将文件夹中名字包含 '_RGB' 的图像文件移动到目标文件夹，并将文件名中的 '_RGB' 替换为 '_PreviewData'。

    :param src_folder: 源文件夹路径
    :param dest_folder: 目标文件夹路径
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 获取源文件夹中所有图像文件
    for file_name in os.listdir(src_folder):
        if '_RGB' in file_name:
            # 构造源文件路径和目标文件路径
            src_path = os.path.join(src_folder, file_name)
            dest_file_name = file_name.replace('_RGB', '_PreviewData')  # 修改文件名
            dest_path = os.path.join(dest_folder, dest_file_name)

            # 移动文件
            shutil.move(src_path, dest_path)
            print(f"已移动: {file_name} -> {dest_file_name}")

if __name__ == "__main__":
    src_folder = r"G:\2024F_10_16\双光检测-Mambayolo\align\JPEGImages"  # 源文件夹路径
    dest_folder = r"G:\2024F_10_16\双光检测-Mambayolo\align\JPEGImages_vis"  # 目标文件夹路径

    # 调用函数将包含 '_RGB' 的图像文件移动并重命名
    move_and_rename_images(src_folder, dest_folder)
