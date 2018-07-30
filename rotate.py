#coding=utf-8
import os
from PIL import Image
def rotate_image(img_name):
    img = Image.open(img_name)
    base_name = os.path.basename(img_name)[:-4]
    dir_name = os.path.dirname(img_name) + '/'
    out_90 = img.transpose(Image.ROTATE_90)
    out_180 = img.transpose(Image.ROTATE_180)
    out_270 = img.transpose(Image.ROTATE_270)
    post_fix = ".jpg"
    rotate_90 = dir_name + base_name + "_90" + ".jpg"
    rotate_180 = dir_name + base_name + "_180" + ".jpg"
    rotate_270 = dir_name + base_name + "_270" + ".jpg"

    out_90.save(rotate_90)
    out_180.save(rotate_180)
    out_270.save(rotate_270)

    filename_lists = open(filelist_name, 'a')
    filelist_name.write(img_name + "\n")
    filelist_name.write(rotate_90 + "\n")
    filelist_name.write(rotate_180 + "\n")
    filelist_name.write(rotate_270 + "\n")

def rotate_label(file_name):
    f = open(file_name, 'r')
    base_name = os.path.basename(file_name)[:-4]
    dir_name = os.path.dirname(file_name) + '/'

    f_90 = open(dir_name + base_name + "_90.txt", 'w')
    f_180 = open(dir_name + base_name + "_180.txt", 'w')
    f_270 = open(dir_name + base_name + "_270.txt", 'w')

    # .txt information
    # label x y w h

    # 90
    # (x, y) -> (y ,1 - x)
    # (w, h) -> (h, w)
    # 180
    # (x, y) -> (1 - x, 1 - y)
    # (w, h) -> (w, h)
    # 270
    # (x, y) -> (1 - y, x)
    # (w, h) -> (h, w)

    for line in f.readlines():
        z = line.strip().split()
        x = float(z[1])
        y = float(z[2])
        w = float(z[3])
        h = float(z[4])

        label_90 = z[0] + " " + str(y) + " " + str(1 - x) + " " + str(h) + " " + str(w) + "\n"
        label_180 = z[0] + " " + str(1 - x) + " " + str(1 - y) + " " + str(w) + " " + str(h) + "\n"
        label_270 = z[0] + " " + str(1 - y) + " " + str(x) + " " + str(h) + " " + str(w) + "\n"

        f_90.write(label_90)
        f_180.write(label_180)
        f_270.write(label_270)
    f_90.close()
    f_180.close()
    f_270.close()


img_dirname = "./daimule_30_classes_rotate/train/JPEGImages/"
label_dirname = "./daimule_30_classes_rotate/train/labels"

filelist_name = "./daimule_30_classes_rotate/filelist/all.txt"

#index = 1
#for img_file in os.listdir(img_dirname):
#    if img_file.endswith(".jpg"):
#        img_file = os.path.join(img_dirname, img_file)
#        rotate_image(img_file)
#        print str(index) + ", " + img_file + " rotates ok!"
#        index = index + 1

for label_file in os.listdir(label_dirname):
    if label_file.endswith(".txt"):
        label_file = os.path.join(label_dirname, label_file)
        rotate_label(label_file)
        print label_file + " rotates ok!"

#rotate_label('./IMG_20180313_152256.txt')
#img_name = "./IMG_20180313_152256.jpg"
#rotate_image(img_name)
