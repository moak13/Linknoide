from flask import jsonify
from utils.model import Model
from networkx.readwrite import json_graph
import networkx as nx
import pandas as pd
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
        response = jsonify(data.to_json())
        model.setData(response)
        return model.getData()

class Generate(Resource):
    def get(self):
        g = self.makePlot()
        data = json_graph.node_link_data(g)
        return data

    def makePlot(self):
        file = model.getData()
        df = pd.read_json(file)
        print(df)
        total = df['Duration'].sum() or df['duration'].sum()
        G = nx.DiGraph()
        for i, elrow in df.iterrows():
            G.add_edge(elrow[1], elrow[0], attr_dict=elrow[2:])
        return G, total
