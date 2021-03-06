import csv

class Model:
    def __init__(self):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.saveName = ""
        self.fileContent = ""
        self.msg = ""

    def passMsg(self, msg):
        ''' Returns a specific message at error intervals
        '''
        return self.msg

    def isValid(self, fileName):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try:
            if fileName[-3] == ".csv" or ".xls":
                file = open(fileName, 'r')
                file.close()
                return True
            else:
                self.passMsg("Wrong File Extension")
        except:
            return False

    def isNameValid(self, saveName):
        '''
        Checks if the inputted name is greater
        than Zero. Returns False otherwise.
        '''
        try:
            if saveName[-3] == ".png" or ".pdf":
                return saveName
            else:
                self.passMsg("File Name Can't Be Empty!")
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
        else:
            self.fileContents = ""
            self.fileName = ""
            self.passMsg("Can't Open File")

    def setSaveFileName(self, saveName):
        '''
        sets the file to be saved as the name inputted
        '''
        if self.isNameValid(saveName):
            self.saveName = saveName
        else:
            self.saveName = ""
            self.passMsg("Empty File Name!")
            
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

    def getSaveFileName(self):
        '''
        Returns the inputted text for the file
        '''
        return self.saveName