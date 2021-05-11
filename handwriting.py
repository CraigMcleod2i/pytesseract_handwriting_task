import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\cmcleod\AppData\Local\Programs\Tesseract-OCR\tesseract'

img1 = 'writing.jpg'
img2 = 'writing2.jpg'
img3 = '2.jpg'
img4 = '3.jpg'
img5 = '6.jpg'
img6 = '7.jpg'

def getBoxes(img):
    d = pytesseract.image_to_data(img,config='--psm 11', output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# def processImage(img):
#     img_cv = cv2.imread(img)
#     width, height = img_cv.shape[:2]
#     if(width > 1000 and height > 1000):
#         blurred_img = cv2.GaussianBlur(img_cv, (5, 7), 13)
#     else:
#         blurred_img = cv2.GaussianBlur(img_cv, (3, 7), 15)
#     resized_img = cv2.resize(blurred_img,( 280, 300))
#     grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
#     mono_img = cv2.adaptiveThreshold(grayscale_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 55, 39)
#     print(pytesseract.image_to_string(mono_img, config="--psm 4, get.images"))
#     getBoxes(mono_img)
#     cv2.imshow('img', mono_img)
#     cv2.waitKey(1000)

def processImage_2(img):
    img_cv = cv2.imread(img)
    width, height = img_cv.shape[:2]
    if(width > 1000 and height > 1000):
        blurred_img = cv2.GaussianBlur(img_cv, (5, 11), 7)
    else:
        blurred_img = cv2.GaussianBlur(img_cv, (5, 7), 25)
    resized_img = cv2.resize(blurred_img,( 280, 300))
    grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    if(width > 1000 and height > 1000):
        mono_img = cv2.adaptiveThreshold(grayscale_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 81, 17)
    else:
        mono_img = cv2.adaptiveThreshold(grayscale_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 55, 39)
    print(pytesseract.image_to_string(mono_img, config="--psm 4, get.images"))
    getBoxes(mono_img)
    cv2.imshow('img', mono_img)
    cv2.waitKey(1000)

processImage_2(img1)
processImage_2(img2)
processImage_2(img3)
processImage_2(img4)
processImage_2(img5)
processImage_2(img6)

