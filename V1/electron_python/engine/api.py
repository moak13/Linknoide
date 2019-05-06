from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from flask_restful import Resource, Api
from flask import  Flask, request
import pandas as pd
from utils.model import Model

app = Flask(__name__)
api = Api(app)
model = Model()

class UploadFile(Resource):
    def post(self):
        req_data = request.files['file']
        fileName = req_data.filename
        model.setFileName(fileName)
        print(fileName)
        return model.getFileContents()
