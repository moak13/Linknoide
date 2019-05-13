import csv
from flask import jsonify

class Model():
    def __init__(self):
        '''
        Initializes the two members the class holds:
        the data from csv file.
        the message to return back to the user on errors
        '''
        self.df = ""
        self.contents = ""
        self.msg = ""

    def setMsg(self, msg):
        ''' 
        Gets the parsed message
        '''
        self.msg = msg

    def setAttr(self, df, content):
        '''
        Get the file dataframe and as well as the file contents to be parsed back
        '''
        self.df = df
        self.contents = content

    def getDF(self):
        '''
        Returns the data.
        '''
        return self.df

    def getContents(self):
        '''
        Returns Contents of a file
        '''
        return self.contents

    def getMsg(self):
        '''
        Returns the message
        '''
        return self.msg