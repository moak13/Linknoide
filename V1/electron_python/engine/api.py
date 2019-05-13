from flask import jsonify
from utils.model import Model
from networkx.readwrite import json_graph
import networkx as nx
import pandas as pd
import itertools

from flask import Flask, request
from flask_restful import Resource, Api
from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


app = Flask(__name__)
api = Api(app)
model = Model()


class UploadFile(Resource):
    def post(self):
        f = request.files['file']
        data = pd.read_csv(f)
        cont = jsonify(data.to_json())
        model.setAttr(data, cont)
        return model.getContents()

class Generate(Resource):
    def get(self):
        g = self.makePlot()
        data = json_graph.node_link_data(g)
        print(data)
        return data

    def makePlot(self):
        df = model.getDF()
        G = nx.DiGraph()
        for i, elrow in df.iterrows():
            G.add_edge(elrow[1], elrow[0], attr_dict=elrow[2:].to_dict())

        for i, nlrow in df.iterrows():
            G.node[nlrow[0]].update(nlrow[1:].to_dict())
        return G


# data = pd.read_csv(f)
        # #response = jsonify(data.to_csv())
        # model.setData(data)
        # return model.getData()
