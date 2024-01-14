import cv2
from flask import Flask
from flask_restful import Resource, Api
import shutil
import requests
from flask import request

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

# WYKRYWANIE LUDZI NA ZDJĘCIU

# initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# load image
# image = cv2.imread('plaza1.jpg')
# image = cv2.resize(image, (1050, 650))

# detect people in the image
# (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

# draw the bounding boxes
# for (x, y, w, h) in rects:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#
# print(f'Found {len(rects)} humans')

# show the output images
# cv2.imshow("People detector", image)
# cv2.waitKey(0)

# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI

# initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# app = Flask(__name__)
# api = Api(app)
#
#
# class PeopleDetector(Resource):
#     def get(self):
#         # load image
#         image = cv2.imread('plaza1.jpg')
#         image = cv2.resize(image, (1050, 650))
#
#         # detect people in the image
#         (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#
#         return {'PeopleCount': len(rects)}
#
#
# api.add_resource(PeopleDetector, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)

# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(POBRANE ZDJĘCIE Z NETA - wpisanie URL w API)

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

app = Flask(__name__)
api = Api(app)


#https://wallpapercave.com/wp/wp7488219.jpg


class PeopleDetector2(Resource):


    @app.route('/data')
    def data():
    # here we want to get the value of user (i.e. ?user=some-value)
        url = request.args.get('url')

    def get(self):
        url = 'https://wallpapercave.com/wp/wp7488219.jpg'
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        # load image
        image = cv2.imread('img.png')

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'PeopleCount2': len(rects)}


api.add_resource(PeopleDetector2, '/')

if __name__ == '__main__':
    app.run(debug=True)


# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(PRZESŁANE ZDJĘCIE(wczytane z folderu)

xxxxxxxxx
