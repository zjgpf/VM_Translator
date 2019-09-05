class VMCodeWriter:
    def __init__(self):
        pass

    def writeArithmetic(self, cmd):
        if cmd == 'add': return self.writeAdd() 
        elif cmd == 'sub': return self.writeSub() 
        elif cmd == 'eq': return self.writeEq() 
        elif cmd == 'lt': return self.writeLt() 
        elif cmd == 'gt': return self.writeGt() 
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

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//*sp=D+*sp \n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=M+D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        return cmds
        
    '''
    sp--
    D = *sp
    sp--
    *sp = *sp-D
    sp++
    '''
    def writeSub(self):
        cmds = ["//sub\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        cmds += ["//D=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//*sp=*sp-D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=M-D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        return cmds

    '''
    sp--
    D=*sp
    sp--
    D=*sp-D
    @go to eq if D=0
    *sp=0
    goto stop
    (eq)
    *sp=-1
    (stop)
    sp++
    '''
    def writeEq(self):    
        cmds = ["//Eq\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp-D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M-D\n"]

        cmds += ["//go to eq if D=0\n"]
        cmds += ["@EQ\n"]
        cmds += ["D;JEQ\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += ["@STOP\n"]
        cmds += ["0;JMP\n"]

        cmds += ["(EQ)\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += ["(STOP)\n"]
        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds

    '''
    sp--
    D=*sp
    sp--
    D=*sp-D
    @go to lt if D<0
    *sp=0
    goto stop
    (lt)
    *sp=-1
    (stop)
    sp++
    '''
    def writeLt(self):    
        cmds = ["//Lt\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp-D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M-D\n"]

        cmds += ["//go to lt if D=0\n"]
        cmds += ["@LT\n"]
        cmds += ["D;JLT\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += ["@STOP\n"]
        cmds += ["0;JMP\n"]

        cmds += ["(LT)\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += ["(STOP)\n"]
        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds

    '''
    sp--
    D=*sp
    sp--
    D=*sp-D
    @go to gt if D>0
    *sp=0
    goto stop
    (gt)
    *sp=-1
    (stop)
    sp++
    '''
    def writeGt(self):    
        cmds = ["//Gt\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//D=*sp-D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M-D\n"]

        cmds += ["//go to gt if D>0\n"]
        cmds += ["@GT\n"]
        cmds += ["D;JGT\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += ["@STOP\n"]
        cmds += ["0;JMP\n"]

        cmds += ["(GT)\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += ["(STOP)\n"]
        cmds += ["//sp++\n"]
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

        cmds += ["//*sp=i\n"]
        cmds += [f"@{number}\n"]
        cmds += ["D=A\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        return cmds
