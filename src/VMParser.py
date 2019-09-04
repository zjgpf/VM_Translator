ARITHMETIC_LOGICAL_COMMANDS = ['add','sub','neg','gt','lt','eq','and','or','not']
class VMParser:
    def __init__(self, content):
        self.content = content
        self.curCmd = None
        self.nextCmd = None
        self.curIdx = 0
        self.curCmdArr = []

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
                while curIdx < len(content) and content[curIdx] not in ['\r', '\n']: curIdx += 1
                self.nextCmd = content[startIdx:curIdx]
                ret = True
                break
        self.curIdx = curIdx
        return ret
                

    def advance(self):
        self.curCmd = self.nextCmd
        self.nextCmd = None
        self.curCmdArr = self.curCmd.split(' ')

    def commandType(self):
        _type = self.curCmdArr[0]
        if _type == 'push': return 'C_PUSH'
        elif _type == 'pop': return 'C_POP'
        elif _type in ARITHMETIC_LOGICAL_COMMANDS: return 'C_ARITHMETIC'

    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC': return self.curCmdArr[0]
        else: return self.curCmdArr[1]

    def arg2(self):
        return self.curCmdArr[2]

