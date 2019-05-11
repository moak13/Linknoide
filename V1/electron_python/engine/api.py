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
from flask import jsonify

app = Flask(__name__)
api = Api(app)
model = Model()

class UploadFile(Resource):
	def post(self):
		f = request.files['file']
		data = pd.read_csv(f)
		filedata = f.read()
		fileName = f.filename
		model.setFileName(fileName)
		response = jsonify(data.to_json())
		response.status_code = 200
		return  response
