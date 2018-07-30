# coding=utf-8
# 使用说明
# 执行脚本前需在train和val目录下分别创建JPEGImages和labels目录，并将原来train和val目录下的图片移到JPEGImages下

import shutil
import os
import json
import re
from PIL import Image
#import cv2
# 将ROI的坐标转换为yolo需要的坐标
# size是图片的w和h
# voc的box里保存的是ROI的坐标（x，y的最大值和最小值）
# 我们的box里保存的是[x,y,w,h]
# 返回值为ROI中心点相对于图片大小的比例坐标，和ROI的w、h相对于图片大小的比例
# yolo 中需要的[x,y,w,h] 是将原始[x,y,w,h]做归一化

#size [900, 430] box [482, 174, 52, 50]--->coco:x, y, width, height,our dataset is also same

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = box[0] + (box[2] / 2.0)
    y = box[1] + (box[3] / 2.0)
    w = box[2]
    h = box[3]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    #print("size",size,box)
    return (x, y, w, h)

    # 原voc_label 代码
    # dw = 1. / (size[0])
    # dh = 1. / (size[1])
    # x = (box[0] + box[1]) / 2.0 - 1
    # y = (box[2] + box[3]) / 2.0 - 1
    # w = box[1] - box[0]
    # h = box[3] - box[2]
    # x = x * dw
    # w = w * dw
    # y = y * dh
    # h = h * dh
    # return (x, y, w, h)

# 获取所需要的类名和id
# path为类名和id的对应关系列表的地址（标注文件中可能有很多类，我们只加载该path指向文件中的类）
# 返回值是一个字典，键名是类名，键值是id
def get_classes_and_index(path):
    D = {}
    f = open(path)
    for line in f:
        temp = line.rstrip().split(',', 2)
        print("temp[0]:" + temp[0] + "\n")
        print("temp[1]:" + temp[1] + "\n")
        D[temp[1]] = temp[0]
        print(D)
    return D


dataDir = "." # 数据集所在的路径
dataType = 'train'  # 要转换的数据集的子集名
#annFile = '%s/annotations/double201-300.json' % (dataDir, dataType)  # 数据集的标注文件路径
classes = get_classes_and_index('dataset_list.txt')   #有什么用

# labels 目录若不存在，创建labels目录。若存在，则清空目录
if not os.path.exists('%s/%s/labels/' % (dataDir, dataType)):
    os.makedirs('%s/%s/labels/' % (dataDir, dataType))
else:
    shutil.rmtree('%s/%s/labels/' % (dataDir, dataType))
    os.makedirs('%s/%s/labels/' % (dataDir, dataType))

# filelist 目录若不存在，创建filelist目录。
if not os.path.exists('%s/filelist/' % dataDir):
    os.makedirs('%s/filelist/' % dataDir)

list_file = open('%s/filelist/%s.txt' % (dataDir, dataType), 'w')  # 数据集的图片list保存路径
infor = open('infor.txt', 'w')
for i in range(0, 29):
    print('/annotations/via_region_data_%d.json' %i)
    with open ('./annotations/via_region_data_%d.json' %i) as f:  # 更改文件名
        file=json.loads(f.read())

        #width = 3000 # 获取图片尺寸  双打 width 1920 height 1080 单打900 430
        #height = 4000  # 获取图片尺寸   # !!!!!!需要改
        for keys in file:
            objCount = 0
            pic = file[keys]

            filename=pic["filename"]            # ex:208.png
            if filename == "JIMG_2601.jpg" or filename == "HIMG_2466":
                continue
            #I = cv2.imread('./train/JPEGImages/%s' %filename)
            I = Image.open('./train/JPEGImages/%s' %filename)
            my_size = I.size
            width = my_size[0]
            height = my_size[1]
            #height = my_size[0]
            #width = my_size[1]
            #imgnum = re.sub("\D", "", filename) # ex:208
            imgnum = re.sub(".jpg", "", filename)  # ex:208
            labels = pic["regions"]
            #print filename
            infor.write(filename + '\n')
            for key in labels :
                object_exist = labels[key]["region_attributes"].has_key("object")
                if not object_exist:
                    continue
                object =labels[key]["region_attributes"]["object"]  # ex:"ball","racket"
                #print("object",object)
                
                if object in classes:
                    #print("hello")
                    objCount = objCount + 1
                    out_file = open('%s/%s/labels/%s.txt' % (dataDir, dataType, imgnum), 'a')
                    cls_id = classes[object]  # 获取该类物体在yolo训练中的id
                    if labels[key]["shape_attributes"]["name"] ==  "rect":
                        x = labels[key]["shape_attributes"]["x"]
                        y = labels[key]["shape_attributes"]["y"]
                        width_b = labels[key]["shape_attributes"]["width"]
                        height_b = labels[key]["shape_attributes"]["height"]
                        box = [x, y, width_b, height_b]    # [482, 174, 52, 50]
                        size = [width, height]
                        #print width,height
                        infor.write(str(width) + ","+ str(height) +'\n')
                        bb = convert(size, box)  # convert
                        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
                        out_file.close()

            if objCount > 0:
                list_file.write('./datasets/%s/JPEGImages/%s.jpg\n' % (dataType, imgnum))  #png->jpg

list_file.close()
infor.close()
#size [900, 430] [486, 116, 33, 61]
