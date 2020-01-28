import cv2
import os
import glob
from PIL import Image

os.chdir('/home/slightowl/Desktop/opencv_workspace/shopsnbars')


def rename():
    i = 1
    for file in list(glob.glob('.')):
        if os.path.isdir(file):
            for i, filename in enumerate(os.listdir(file)):
                os.rename(file + "/" + filename, file + "/" + str(i) + ".png")


def convert_to_png():
    for file in list(glob.glob('*.jpeg')):
        Image.open(file).save(file + ".png")


# iterates through files of given dir
# converts to grayscale and shows output
# change file type for needs
def image_to_grey():
    for file in list(glob.glob('*.png')):
        img = cv2.imread(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("converted", gray)
        cv2.waitKey(200)

        # overwrite img with converted grayscale
        cv2.imwrite(file, gray)


def resize():
    for file in list(glob.glob('*.png')):
        img = cv2.imread(file)
        re = cv2.resize(img, (200, 200))
        cv2.imshow("Resized", re)
        cv2.waitKey(200)
        cv2.destroyAllWindows()

        # overwrite img with reszied
        cv2.imwrite(file, re)


rename()
#convert_to_png()
image_to_grey()
resize()
