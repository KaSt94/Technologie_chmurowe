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

# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(POBRANE ZDJĘCIE Z NETA - URL ZASZYTY W KODZIE)

# # initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# app = Flask(__name__)
# api = Api(app)
#
#
# class PeopleDetector2(Resource):
#
#
#     def get(self):
#         url = 'https://wallpapercave.com/wp/wp7488219.jpg'
#         response = requests.get(url, stream=True)
#         with open('img.jpg', 'wb') as out_file:
#             shutil.copyfileobj(response.raw, out_file)
#
#         # load image
#         image = cv2.imread('img.jpg')
#
#         # detect people in the image
#         (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#
#         return {'PeopleCount2': len(rects)}
#
#
# api.add_resource(PeopleDetector2, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)

# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI ZE ZDJĘCIA W PROJEKCIE

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg',}

app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class PeopleDetector(Resource):
    def get(self):
        # load image
        image = cv2.imread('plaza.jpg')
        image = cv2.resize(image, (1050, 650))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'PeopleCount': len(rects)}


# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(POBRANE ZDJĘCIE Z NETA - URL PODAWANY W PRZEGLĄDARCE)

class PeopleDetector2(Resource):
    def get(self):
        url = request.args.get("url")
        print("url", url)
        response = requests.get(url, stream=True)
        with open('img.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        # load image
        image = cv2.imread('img.jpg')

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'PeopleCount2': len(rects)}

# PRZYKŁADOWE ZDJĘCIE
# https://thumbs.dreamstime.com/b/enamoured-couple-10989620.jpg


# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(PRZESŁANE ZDJĘCIE(wczytane z folderu w przeglądarce)

class PeopleDetector3(Resource):

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            files = request.files.getlist("file[]")
            filenames = []
            for file in files:
                if file:
                    filename = "Photo.jpg"
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    filenames.append(filename)

            flash("Uploaded files: {}".format(", ".join(filenames)))

        return render_template("file_upload.html")

    def get(self):

        # load image
        path = r"C:\Python_projekty\Technologie_chmurowe\static\uploads\Photo.jpg"
        image = cv2.imread(path)

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'PeopleCount3': len(rects)}


api.add_resource(PeopleDetector, '/static')

api.add_resource(PeopleDetector2, '/dynamic')

api.add_resource(PeopleDetector3, '/upload')

if __name__ == '__main__':
    app.run(debug=True)


# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(PRZESŁANE ZDJĘCIE(wczytane z folderu w przeglądarce)

# # initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# UPLOAD_FOLDER = os.path.join('static', 'uploads')
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg',}
#
# app = Flask(__name__)
# api = Api(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
#
# class PeopleDetector3(Resource):
#
#
#     @app.route('/', methods=['GET', 'POST'])
#     def upload_file():
#         if request.method == 'POST':
#             files = request.files.getlist("file[]")
#             filenames = []
#             for file in files:
#                 if file:
#                     filename = "Photo.jpg"
#                     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                     filenames.append(filename)
#
#             flash("Uploaded files: {}".format(", ".join(filenames)))
#
#         return render_template("file_upload.html")
#
#     def get(self):
#
#         # load image
#         path = r"C:\Python_projekty\Technologie_chmurowe\static\uploads\Photo.jpg"
#         image = cv2.imread(path)
#
#         # detect people in the image
#         (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#
#         return {'PeopleCount3': len(rects)}
#
#
# api.add_resource(PeopleDetector3, '/2')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI(PRZESŁANE ZDJĘCIE(wczytane z folderu w przeglądarce)

# # initialize the HOG descriptor/person detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# UPLOAD_FOLDER = os.path.join('static', 'uploads')
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg',}
#
# app = Flask(__name__)
# api = Api(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
#
# class PeopleDetector3(Resource):
#
#
#     @app.route('/', methods=['GET', 'POST'])
#     def upload_file():
#         if request.method == 'POST':
#             files = request.files.getlist("file[]")
#             filenames = []
#             for file in files:
#                 if file:
#                     filename = secure_filename(file.filename)
#                     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                     filenames.append(filename)
#
#             flash("Uploaded files: {}".format(", ".join(filenames)))
#
#         return render_template("file_upload.html")
#
#     def get(self):
#
#         # load image
#         image = cv2.imread()
#
#         # detect people in the image
#         (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#
#         return {'PeopleCount3': len(rects)}
#
#
# api.add_resource(PeopleDetector3, '/2')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)