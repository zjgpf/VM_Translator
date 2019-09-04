class VMCodeWriter:
    def __init__(self):
        pass

    def writeArithmetic(self, cmd, *numbers):
        return []

    def writePushPop(self, cmdType, segment, index):
        if cmdType == 'C_PUSH':
            if segment == 'constant':
                return self.pushConstant(index)
        else:
            print(cmdType) 

    '''
    push constant number
    *sp= i; sp++
    '''
    def pushConstant(self,number):
        cmds = [f"//push constant {number}\n"]
        #*sp=i
        cmds += [f"@{number}\n"]
        cmds += ["D=A\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]
        #sp++
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        return cmds
