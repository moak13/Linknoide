class Model():
    def __init__(self):
        '''
        Initializes the two members the class holds:
        the data from csv file.
        the message to return back to the user on errors
        '''
        self.data = ""
        self.msg = ""

    def passMsg(self, msg):
        ''' 
        Returns a specific message at error intervals
        '''
        return self.msg

    def setData(self, data):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        self.data = data

    def getData(self):
        '''
        Returns the data.
        '''
        return self.data