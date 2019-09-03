import pdb
class VMParser:
    def __init__(self, content):
        self.content = content
        self.curCmd = None
        self.nextCmd = None
        self.curIdx = 0

    def hasMoreCommands(self):
        if self.nextCmd: return True
        else:
            hasNextCmd = self.getNextCmd()
            return hasNextCmd

    def getNextCmd(self):
        content = self.content
        curIdx = self.curIdx
        ret = False
        while curIdx < len(content):
            while content[curIdx] in ['\n','\r']: 
                curIdx += 1
                if curIdx == len(content): break
            if curIdx == len(content): break
            if content[curIdx] == '/' and content[curIdx+1] == '/':
                while curIdx < len(content):
                    if content[curIdx] == '\n': 
                        curIdx += 1
                        break
                    curIdx+=1
                if curIdx == len(content): break
            else:
                startIdx = curIdx
                while curIdx < len(content) and content[curIdx] != '\r': curIdx += 1
                self.nextCmd = content[startIdx:curIdx]
                ret = True
                break
        self.curIdx = curIdx
        return ret
                

    def advance(self):
        self.curCmd = self.nextCmd
        self.nextCmd = None

    def commandType(self):
        pass

    def arg1(self):
        pass

    def arg2(self):
        pass

