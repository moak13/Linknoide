class Model:
    def __init__(self):
        '''
        Initializes the three members the class holds:
        the file name and its contents.
        the message to return back to the user on errors
        '''
        self.fileName = None
        self.fileContent = ""
        self.msg = ""

    def passMsg(self, msg):
        ''' 
        Returns a specific message at error intervals
        '''
        return self.msg

    def isValid(self, fileName):
        '''
        Returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try:
            if fileName[-3] == ".csv" or ".xls":
                file = open(fileName, 'r').read()
                print(file)
                return file
            else:
                self.passMsg("Wrong File Extension")
        except:
            return False

    def setFileName(self, fileName):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid(fileName):
            self.fileName = fileName
            self.fileContents = open(fileName, 'r').read()
            print(self.fileName)
            print(self.fileContents)
        else:
            self.fileContents = "File Contents Can't be read"
            self.fileName = "No File Parsed!"
            self.passMsg("Can't Open File")
            
    def getFileName(self):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def getFileContents(self):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents