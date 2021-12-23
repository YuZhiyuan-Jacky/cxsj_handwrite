import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import img_update as iu
import Bold as bl
import time
import scipy

IMAGES_INPUT_PATH = r'shouxie\input\\'
IMAGES_PATH = r'./shouxie\\'
IMAGE_SAVE_PATH = r'./shouxie\result\final.jpg'




# 上传图片并展示
uploaded_file = st.file_uploader("上传一张图片", type="jpg")
if uploaded_file is None:
    st.warning('请上传模仿字迹图片')
    st.stop()
if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    # opencv_image = cv2.imdecode(file_bytes, 1)

    # 将传入的文件转为numpy.array格式
    # 改变字迹粗细
    img = np.array(Image.open(uploaded_file))
    img = Image.fromarray(img)
    img = img.convert('L')
    ImArray = np.array(img)
    # 滑动改变大小
    strength = st.slider('加粗强度', 0, 10)
    strength = strength + 1
    BoldArray = bl.Bold(ImArray, strength)
    st.image(BoldArray)
    # 展示图片
    # st.image(opencv_image, channels="BGR")
# 保存图片

    cv2.imwrite(IMAGES_INPUT_PATH+'test.png', BoldArray)
#     cv2.imwrite(IMAGES_INPUT_PATH+'test.jpg',opencv_image)
# 然后就可以用这个图片进行一些操作了



#输入生成信息
title = st.text_input('生成文字')
IMAGE_COLUMN = st.text_input('每行字数')
if not title:
    st.warning('请输入生成文字')
    st.stop()
if not IMAGE_COLUMN:
    st.warning('请输入每行字数')
    st.stop()
# st.success('Thank you for inputting')
# st.write(type(title))
# st.write(type(IMAGE_COLUMN))

# 开始按钮
if st.button('生成'):
    pass
else:
    st.stop()


#等待
my_bar = st.progress(0)
for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)


#调用学习算法生成图片



#生成图片展示
iu.image_compose(IMAGES_PATH,IMAGE_SAVE_PATH,int(IMAGE_COLUMN),title)  # 调用函数合并图片
img=Image.open(IMAGE_SAVE_PATH)
st.image(img)


