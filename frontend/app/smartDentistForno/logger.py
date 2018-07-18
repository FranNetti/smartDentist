import datetime

class FileLogger:

    fileName = ""
    mode = ""

    def __init__(self, fileName = "myLog.txt", mode = "at+"):
        self.fileName = fileName
        self.mode = mode

    def log(self, msg):
        with open(self.fileName, self.mode) as myfile:
            msg = "{} | {}".format(datetime.datetime.utcnow(), msg)
            print(msg, file=myfile)
