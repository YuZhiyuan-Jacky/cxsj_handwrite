import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image

# IMAGES_PATH = r'C:\Users\Jacky\Desktop\shouxie\\'  # 图片集地址
# IMAGES_FORMAT = ['.png']  # 图片格式
# IMAGE_SIZE = 128  # 每张小图片的大小
# # IMAGE_ROW = 1  # 图片间隔，也就是合并成一张图后，一共有几行 原版用
# IMAGE_COLUMN = 7  # 图片间隔，也就是合并成一张图后，一共有几列
# IMAGE_SAVE_PATH = r'C:\Users\Jacky\Desktop\shouxie\result\final.jpg'  # 图片转换后的地址
#
#
# title="落霞与孤鹜齐飞秋水共长天一色"
# # 新版  计算生成图片行数
# IMAGE_ROW_yu = len(title) % IMAGE_COLUMN
# if IMAGE_ROW_yu == 0:
#     IMAGE_ROW = len(title) // IMAGE_COLUMN
# else:
#     IMAGE_ROW = len(title) // IMAGE_COLUMN + 1
#
#
#
# # 获取图片集地址下的所有图片名称
# image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
#                os.path.splitext(name)[1] == item]
# print("image_names", image_names)

# 原版规定行列数
# # 获取图片集地址下的所有图片名称
# image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
#                os.path.splitext(name)[1] == item]
#
# print("image_names", image_names)
# # 简单的对于参数的设定和实际图片集的大小进行数量判断
# if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
#     raise ValueError("合成图片的参数和要求的数量不能匹配！")
#



# 定义图像拼接函数

def image_compose(IMAGES_PATH, IMAGE_SAVE_PATH, IMAGE_COLUMN, title, IMAGE_SIZE=128):
    # 新版  计算生成图片行数
    IMAGE_ROW_yu = len(title) % IMAGE_COLUMN
    if IMAGE_ROW_yu == 0:
        IMAGE_ROW = len(title) // IMAGE_COLUMN
    else:
        IMAGE_ROW = len(title) // IMAGE_COLUMN + 1

    # 获取图片集地址下的所有图片名称
    # image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
    #                os.path.splitext(name)[1] == item]
    # print("image_names", image_names)

    to_image = Image.new('RGB', size=(IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE),color=(255,255,255))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    total_num = 0
    n = 0
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            # print(title[n])
            from_path = IMAGES_PATH + 'shouxie_' + hex(ord(title[n]))[2:] + '.png'
            # print(from_path)
            from_image = Image.open(from_path).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
            total_num += 1
            n += 1
            if total_num == len(title):
                break
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图

# 原版规定行列数
# # 定义图像拼接函数
# def image_compose():
#     to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
#     # 循环遍历，把每张图片按顺序粘贴到对应位置上
#     for y in range(1, IMAGE_ROW + 1):
#         for x in range(1, IMAGE_COLUMN + 1):
#             from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
#                 (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
#             to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
#     return to_image.save(IMAGE_SAVE_PATH)  # 保存新图
#

image_compose(IMAGES_PATH = r'C:\Users\Jacky\Desktop\shouxie\\',IMAGE_SAVE_PATH = r'C:\Users\Jacky\Desktop\shouxie\result\final.jpg',IMAGE_COLUMN = 7,title="落霞与孤鹜齐飞秋水共长天一色")  # 调用函数


