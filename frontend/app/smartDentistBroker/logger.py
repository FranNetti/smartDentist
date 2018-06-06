import datetime

class FileLogger:

    fileName = ""

    def __init__(self, fileName = "myLog.txt"):
        self.fileName = fileName
    
    def log(self, msg):
        with open(fileName, "at") as myfile:
            msg = "{} | {}".format(datetime.datetime.utcnow(), msg)
            print(msg, file=myfile)


