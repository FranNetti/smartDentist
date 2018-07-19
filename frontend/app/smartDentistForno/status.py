from sender import MsgSender
from logger import FileLogger

class StatusHandler:
    status = False
    statusFile = None
    sender = None
    id = ""
    loopContinue = True

    def __init__(self, msgSender, id):
        self.statusFile = FileLogger("app/smartDentistForno/doc/statusFile.txt", "wt+")
        self.sender = msgSender
        self.id = id


    def saveStatus(self,newStatus):
        if self.changeStatus({'id' : self.id, 'status' : str(newStatus)}):
            self.sender.sendStatusChangeApp(self.id, self.status)
            self.loopContinue = True

    #function for changing state when detecting a new command from server
    def changeStatus(self,data):
        newStatus = data["status"].lower() == "true"
        if(data["id"] == self.id and self.status != newStatus):
            self.status = newStatus
            self.loopContinue = newStatus;
            statusMsg = "ON" if self.status else "OFF"
            self.statusFile.log("Switch {}".format(statusMsg))
            print("Device {} - Switch {}".format(self.id, statusMsg))
            return True
        return False

    def hasToLoop(self):
        return self.loopContinue
