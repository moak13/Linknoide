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
import networkx as nx
from networkx.readwrite import json_graph
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

class Generate(Resource):
    def get(self):
        g = makePlot()
        data = json_graph.node_link_data(g)
        return data

def makePlot():
    file = model.getFileName()
    df = pd.DataFrame(file)
    total = df['Duration'].sum() or df['duration'].sum()
    G = nx.DiGraph()
    for i, elrow in df.iterrows():
        G.add_edge(elrow[1], elrow[0], attr_dict=elrow[2:])
    return G, total
