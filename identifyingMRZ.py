from imutils import paths
import numpy as np
import imutils
import cv2
import pytesseract
from GetPath import get_converted_img_path,get_tesseract_exe,get_forms,get_form_types

pytesseract.pytesseract.tesseract_cmd = get_tesseract_exe()


forms = get_forms()
forms_types = get_form_types()


def identify_MRZ(image_name):
    # initialize a rectangular and square structuring kernel
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))

    # loop over the input image paths
    # for imagePath in paths.list_images(r'C:\Users\dell\Documents\Capstone\TempImgs'):
    # load the image, resize it, and convert it to grayscale
    full_path= get_converted_img_path()+image_name
    image = cv2.imread(full_path)
    # image = imutils.resize(image, height=600)
    image_resized = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)


    # smooth the image using a 3x3 Gaussian, then apply the blackhat
    # morphological operator to find dark regions on a light background
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
 
    # compute the Scharr gradient of the blackhat image and scale the
    # result into the range [0, 255]
    gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")

    # apply a closing operation using the rectangular kernel to close
    # gaps in between letters -- then apply Otsu's thresholding method
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # perform another closing operation, this time using the square
    # kernel to close gaps between lines of the MRZ, then perform a
    # series of erosions to break apart connected components
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    thresh = cv2.erode(thresh, None, iterations=4)

    # find contours in the thresholded image and sort them by their
    # size
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    count = 1
    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and use the contour to
        # compute the aspect ratio and coverage ratio of the bounding box
        # width to the width of the image
        (x, y, w, h) = cv2.boundingRect(c)
        # ar = w / float(h)
        # crWidth = w / float(gray.shape[1])
        # check to see if the aspect ratio and coverage width are within
        # acceptable criteria
        pX = int((x + w) * 0.05)
        pY = int((y + h) * 0.05)
        (x, y) = (x - pX, y - pY)
        (w, h) = (w + (pX * 2), h + (pY * 2))
        # extract the ROI from the image and draw a bounding box
        # surrounding the MRZ
        roi = image_resized[y:y + h, x:x + w].copy()

        # convert the image to black and white for better OCR
        ret,thresh1 = cv2.threshold(roi,120,255,cv2.THRESH_BINARY)
        # pytesseract image to string to get results
        text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
        #checking if the text is the title of the form, if yes will return the path to the ImageProcessing module
        for s in forms_types:
            if s in text:
                return forms[s]
