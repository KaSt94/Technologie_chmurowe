import cv2
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_restful import Resource, Api
import shutil
import requests
import os
from werkzeug.utils import secure_filename


# ZWRACANIE INFORMACJI HTTPS - WYKRYWANIE LUDZI ZE ZDJĘCIA W PROJEKCIE

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
api = Api(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


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


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class PeopleDetector3(Resource):

    @app.route('/')
    def upload_form():
        return render_template('upload.html')

    @app.route('/', methods=['POST'])
    def upload_image():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = cv2.imread(filename)
            (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

            return {'PeopleCount3': len(rects)}

        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return redirect(request.url)


api.add_resource(PeopleDetector, '/static')

api.add_resource(PeopleDetector2, '/dynamic')

api.add_resource(PeopleDetector3, '/')

if __name__ == '__main__':
    app.run(debug=True)
