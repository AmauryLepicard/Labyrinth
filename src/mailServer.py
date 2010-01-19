class MailServer:
    def __init__(self):
        self.messageList = {}
    
    def addMessage(self, dest, orig, content):
        if dest not in self.messageList.keys():
            self.messageList[dest] = []        
        self.messageList[dest].append((orig, content))
    
    def getMessages(self, dest):
        return self.messageList.pop(dest, [])
    
    def getMailNumber(self):
        cpt = 0
        for dest in self.messageList.keys():
            cpt += len(self.messageList[dest])
        return cpt
        
    
mail = MailServer()
