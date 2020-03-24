from flask import Flask, request, render_template, make_response, redirect
from flask_restful import Resource, Api, reqparse
from json import dumps
from flask_jsonpify import jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

import cv2
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import math
from utils import *

app = Flask(__name__)
api = Api(app)

class GetCaption(Resource):
    def get(self):
        result = {'Upload an image by going to:':'/index'}
        print(result)
        return jsonify(result) # Fetches first column that is Employee ID

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        args = parse.parse_args()
        imgFile = args['file']

        fname = "your_file_name.jpg"
        imgFile.save(fname)

        caption = findCaption(fname)
        result = {'Caption': str(caption)}
        
        return jsonify(result)
        
api.add_resource(GetCaption, '/getCaption') # Route_1

if __name__ == '__main__':
     app.run(port='8000', threaded = False)