from threading import Thread
import time
from utils.config import globalconfig
class basetext:
    def __init__(self,textgetmethod)  : 
        self.suspending=False
        self.textgetmethod=textgetmethod
        self.t=Thread(target=self.gettextthread_)
        self.t.setDaemon(True)
        self.t.start()
    def gettextthread_(self):
        while True:
            if self.ending:
                
                break
            if globalconfig['sourcestatus'][self.typename]==False:
                break
            if globalconfig['autorun']==False  :
                time.sleep(1)
                continue
            self.gettextthread()
         
    def gettextthread(self):
        pass
    def runonce(self):
        pass
    def end(self):
        self.ending=True
 