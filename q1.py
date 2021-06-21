import numpy as np 
from PIL import Image , ImageOps , ImageEnhance
import matplotlib.pyplot as plt 
import os

def create_folder():
    cwd = os.getcwd()
    cwd = cwd + '/'
    new_folder = ["greyImage" , "sepiaImage" , "highContrastImage" , "brightImage" , "sharpImage" , "resizedImage"]

    for folder in new_folder :
        path = os.path.join(cwd , folder)
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)


def read_image(root):
    img_path = np.array([])
    for root , dirs , files in os.walk(root):
        for f in files:
            img_path = np.append(img_path , os.path.join(root,f))

    return img_path

def get_name(img_path):
    txt = img_path.split("\\")
    name = txt[-1]
    name = name.replace('.jpg','')
    return name


def grey_image(img_path):
    im = Image.open(img_path)
    gray_scale = ImageOps.grayscale(im)
    gray_scale.show()
    name = get_name(img_path)
    name = os.getcwd() + '/' + "greyImage/"+ name + "grey_scale.jpg"
    gray_scale.save(name)


def get_sepia_pixel(red ,  green , blue):
    tRed = int((0.759 * red) + (0.398 * green) + (0.194 * blue))
    tGreen = int((0.676 * red) + (0.354 * green) + (0.173 * blue))
    tBlue = int((0.524 * red) + (0.277 * green) + (0.136 * blue))

    if(tBlue > 255):
        tBlue = 255
    if tRed > 255 :
        tRed = 255
    if tGreen > 255:
        tGreen = 255

    return tRed , tGreen , tBlue


def sepia_image(img_path):
    im = Image.open(img_path)
    width , height = im.size
    new_img = Image.new(mode = "RGB" , size = (width , height))

    pixels = new_img.load()
    pix = im.load()

    for i in range(width):
        for j in range(height):
            p = im.getpixel((i,j))
            pixels[i,j] = get_sepia_pixel(p[0] , p[1] , p[2])

    name = get_name(img_path)
    name = os.getcwd() + '/' + "sepiaImage/"+ name + "sepia_tone.jpg"
    name = name + "sepia_tone.jpg"
    new_img.show()
    new_img.save(name)


def high_contrast_image(img_path):
    img = Image.open(img_path)
    new_img = ImageEnhance.Contrast(img).enhance(2)
    
    name = get_name(img_path)
    name = os.getcwd() + '/' + "highcontrastImage/"+ name + "high_contrast.jpg"
    new_img.show()
    new_img.save(name)


def brighten_image(img_path):
    img = Image.open(img_path)
    new_img = ImageEnhance.Brightness(img).enhance(2)

    name = get_name(img_path)
    name = os.getcwd() + '/' + "brightImage/"+ name + "bright.jpg"
    new_img.show()
    new_img.save(name)


def sharpen_image(img_path):
    img = Image.open(img_path)
    new_img = ImageEnhance.Sharpness(img).enhance(1.5)

    name = get_name(img_path)
    name = os.getcwd() + '/' + "sharpImage/"+ name + "sharp.jpg"
    new_img.show()
    new_img.save(name)


def resize(img_path):
    im = Image.open(img_path)
    new_img = im.resize((480,640))

    name = get_name(img_path)
    name = os.getcwd() + '/' + "resizedImage/"+ name + "resized.jpg"
    new_img.show()
    new_img.save(name)



source = "E:\\Image Processing Project\\Imageset"
create_folder()
data = read_image(source)  
for img in data:
    grey_image(img)
    sepia_image(img)
    high_contrast_image(img)
    brighten_image(img)
    sharpen_image(img)
    resize(img)
