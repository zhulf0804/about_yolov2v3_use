from PIL import Image, ImageDraw


im01 = Image.open("/Users/zhulf/code/IMG_20180313_152256_180.jpg")
#im01 = Image.open("1_90.jpg")
size = im01.size
width = size[0]
height = size[1]

print width, height

# 0.450625 0.427333333333 0.04475 0.0433333333333

x = 0.5855 * width
y = 0.417875 * height
w = 0.0483333333333 * width
h = 0.05125 * height

#0.543 0.504333333333 0.0345 0.0546666666667
# 0.5855 0.417875 0.0483333333333 0.05125

t1 = int(x - w/2)
t2 = int(y - h/2)
t3 = int(x + w/2)
t4 = int(y + h/2)

print t1, t2, t3, t4

draw = ImageDraw.Draw(im01)

draw.rectangle((int(t1), int(t2), int(t3), int(t4)), fill = (255,0,0))

#draw.rectangle([100,200,300,500],fill = (0,255,0))

#draw.rectangle([(300,500),(600,700)], fill = (0,0,255))

im01.show()



#x = 0.427333333333
#y = 0.549375
#w = 0.0433333333333
#h = 0.04475
