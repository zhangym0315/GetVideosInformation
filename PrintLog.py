class PrintLog():
    def __init__(self):
        self.logfile = "Log.txt"
        return None
    
    def printlog(self, string):
        print(string)
        with open(self.logfile, 'a') as f:
            f.write(string)
        return 0