#! python

from PIL import Image
import sys, os


# 获取图片信息
def getImageInfo(filename):
    imageFile = Image.open(filename)
    print('ImageSize：' + str(imageFile.size))
    print('ImageName：' + str(imageFile.filename))
    print('ImageFormat:' + imageFile.format)
    print('ImageDescription:' + imageFile.format_description)


# 裁剪图片
def setImageSize():
    imageFile = Image.open(sys.argv[1])
    print('裁剪前的尺寸：' + str(imageFile.size))
    copyFile = imageFile.copy()
    print('复制文件：' + str(imageFile.size))
    saveFile = copyFile.resize((int(sys.argv[3]), int(sys.argv[4])))
    print('裁剪后的尺寸：' + str(saveFile.size))
    saveFile.save(sys.argv[2])


SQUARE_FIT_SIZE = 400
LOGO_FILENAME = 'logo.png'


def addLogo():
    # ： 遍历文件夹下所有的图片
    os.makedirs('withlogo', exist_ok=True)
    # 获取logo信息
    logoIm = Image.open(LOGO_FILENAME)
    logoWidth, logoHeight = logoIm.size
    for filename in os.listdir('.'):
        if not (filename.endswith('.png') or filename.endswith('.jpg')) \
                or filename == LOGO_FILENAME:
            continue

        im = Image.open(filename)
        width, height = im.size
        # 调整图像大小
        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE
            print('Resizing %s ...' % filename)
            im = im.resize((width,height))
            # 添加logo
            print('Adding logo to %s ...' % filename)
            im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)
            # Save
            im.save(os.path.join('withlogo',filename))


if __name__ == '__main__':

    addLogo()
