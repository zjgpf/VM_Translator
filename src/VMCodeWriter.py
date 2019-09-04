class VMCodeWriter:
    def __init__(self):
        pass

    def writeArithmetic(self, cmd):
        if cmd == 'add': return self.writeAdd() 
        return []

    '''
    sp--
    D = *sp
    sp--
    *sp = D+*sp
    sp++
    '''
    def writeAdd(self):
        cmds = ["//add\n"]
        #sp--
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        #D=*sp
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]
        #sp--
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        #*sp=D+*sp 
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=M+D\n"]
        #sp++
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        return cmds
        
        

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
