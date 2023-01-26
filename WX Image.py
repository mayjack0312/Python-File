import os
from PIL import Image

# from shutil import copyfile
# from math import ceil

path = r"C:\Users\13552\Desktop\Luban-Py\test.png"
new_path = "c_test.png"  # 缩放好的图片保存路径

img = Image.open(path)  # 读取原图
width, height = img.size[0], img.size[1]  # 读取原图的宽和高 .[0] 是宽，.[1] 是高
if img.size[0] < img.size[1]: 
    new_width = 1080
    new_height = int(new_width * height / width)  # 计算新高
    new_img = img.resize((new_width, new_height), Image.ANTIALIAS)  # 缩放
elif img.size[0] > img.size[1]: 
    new_height = 1080
    new_width = int(new_height * width / height)  # 计算新高
    new_img = img.resize((new_width, new_height), Image.ANTIALIAS)  # 缩放

new_img.save(new_path)  # 保存缩放后的图片


'''
if __name__ == '__main__':
    path = r""
'''
