import cv2
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_restful import Resource, Api
import shutil
import requests
import os
from werkzeug.utils import secure_filename


# POKAZYWANIE ZDJĘCIA

# img = cv2.imread('plaza1.jpg')
#
# img = cv2.resize(img, (1050, 650))
#
# print(type(img))
# print(img.shape)
#
# cv2.imshow('plaza1.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# WYKRYWANIE LUDZI NA ZDJĘCIU I POKAZYWANIE - ZE ZDJĘCIA W PROJEKCIE

# # initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# # load image
# image = cv2.imread('plaza.jpg')
# image = cv2.resize(image, (1050, 650))
#
# # detect people in the image
# (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#
# # draw the bounding boxes
# for (x, y, w, h) in rects:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#
# print(f'Found {len(rects)} humans')
#
# # show the output images
# cv2.imshow("People detector", image)
# cv2.waitKey(0)
