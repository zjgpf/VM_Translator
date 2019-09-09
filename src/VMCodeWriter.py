label_count = 0
SEGMENT_POINT_MAP={'local':'LCL','argument':'ARG','this':'THIS','that':'THAT'}
class VMCodeWriter:
    def __init__(self, className):
        #className for static field
        self.className = className

    def writeArithmetic(self, cmd):
        if cmd == 'add': return self.writeAdd() 
        elif cmd == 'sub': return self.writeSub() 
        elif cmd == 'eq': return self.writeEq() 
        elif cmd == 'lt': return self.writeLt() 
        elif cmd == 'gt': return self.writeGt() 
        elif cmd == 'and': return self.writeAnd() 
        elif cmd == 'or': return self.writeOr() 
        elif cmd == 'neg': return self.writeNeg() 
        elif cmd == 'not': return self.writeNot() 
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
        global label_count
        LABEL_EQ = self.className+'_'+"EQ"+str(label_count)
        LABEL_STOP = self.className+ '_'+"STOP"+str(label_count)
        label_count+=1

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
        cmds += [f"@{LABEL_EQ}\n"]
        cmds += ["D;JEQ\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += [f"@{LABEL_STOP}\n"]
        cmds += ["0;JMP\n"]

        cmds += [f"({LABEL_EQ})\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += [f"({LABEL_STOP})\n"]
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
        global label_count
        LABEL_LT = self.className+'_'+"Lt"+str(label_count)
        LABEL_STOP = self.className+'_'+"STOP"+str(label_count)
        label_count+=1

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
        cmds += [f"@{LABEL_LT}\n"]
        cmds += ["D;JLT\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += [f"@{LABEL_STOP}\n"]
        cmds += ["0;JMP\n"]

        cmds += [f"({LABEL_LT})\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += [f"({LABEL_STOP})\n"]
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
        global label_count
        LABEL_GT = self.className+'_'+"GT"+str(label_count)
        LABEL_STOP = self.className+'_'+"STOP"+str(label_count)
        label_count+=1

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
        cmds += [f"@{LABEL_GT}\n"]
        cmds += ["D;JGT\n"]

        cmds += ["//*sp=0\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=0\n"]

        cmds += ["//go to stop\n"]
        cmds += [f"@{LABEL_STOP}\n"]
        cmds += ["0;JMP\n"]

        cmds += [f"({LABEL_GT})\n"]
        cmds += ["//*sp=-1\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-1\n"]

        cmds += [f"({LABEL_STOP})\n"]
        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]

        return cmds

    '''
    sp--
    D=*sp
    sp--
    *sp = *sp&D
    sp++
    '''
    def writeAnd(self):    
        cmds = ["//And\n"]

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

        cmds += ["//*sp=*sp&D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=M&D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds

    '''
    sp--
    D=*sp
    sp--
    *sp = *sp|D
    sp++
    '''
    def writeOr(self):    
        cmds = ["//Or\n"]

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

        cmds += ["//*sp=*sp&D\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=M|D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds

    '''
    sp--
    *sp = -*sp
    sp++
    '''
    def writeNeg(self):    
        cmds = ["//Neg\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//*sp = -*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=-M\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]

        return cmds

    '''
    sp--
    *sp = !*sp
    sp++
    '''
    def writeNot(self):    
        cmds = ["//Not\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//*sp = -*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=!M\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]

        return cmds
        
    def writePushPop(self, cmdType, segment, index):
        if cmdType == 'C_PUSH':
            if segment == 'constant':
                return self.pushConstant(index)
            elif segment in ['local','argument','this','that']:
                return self.pushLocArgThisThat(segment,index)
            elif segment == 'temp':
                return self.pushTemp(index)
            elif segment == 'pointer':
                return self.pushPointer(index)
            elif segment == 'static':
                return self.pushStatic(index)
        else:
            if segment in ['local','argument','this','that']:
                return self.popLocArgThisThat(segment,index)
            elif segment == 'temp':
                return self.popTemp(index)
            elif segment == 'pointer':
                return self.popPointer(index)
            elif segment == 'static':
                return self.popStatic(index)

    '''
    push local/argument/this/that
    D=segmentPointer+i;*sp=*D;sp++
    '''
    def pushLocArgThisThat(self, segment, index):
        pointer = SEGMENT_POINT_MAP[segment]
        cmds = [f"//push {segment} {index}\n"]

        cmds += ["//D=segmentPointer+i\n"]
        cmds += [f"@{index}\n"]
        cmds += ["D=A\n"]
        cmds += [f"@{pointer}\n"]
        cmds += ["D=M+D\n"]
        
        cmds += ["//*sp=*D\n"]
        cmds += ["A=D\n"]
        cmds += ["D=M\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds
        
    '''
    pop local/argument/this/that
    addr=segmentPointer+i;sp--;*addr=*sp;
    '''
    def popLocArgThisThat(self, segment, index):
        pointer = SEGMENT_POINT_MAP[segment]
        cmds = [f"//pop {segment} {index}\n"]

        cmds += ["//addr=segmentPointer+i\n"]
        cmds += [f"@{index}\n"]
        cmds += ["D=A\n"]
        cmds += [f"@{pointer}\n"]
        cmds += ["D=M+D\n"]
        cmds += ["@addr\n"]
        cmds += ["M=D\n"]

        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        
        cmds += ["//*addr=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]
        cmds += ["@addr\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]
        
        return cmds

    '''
    push temp
    D=5+i;*sp=*D;sp++
    '''
    def pushTemp(self,index):
        cmds = [f"//push temp {index}\n"]

        cmds += ["//D=5+i\n"]
        cmds += [f"@{index}\n"]
        cmds += ["D=A\n"]
        cmds += [f"@5\n"]
        cmds += ["D=A+D\n"]
        
        cmds += ["//*sp=*D\n"]
        cmds += ["A=D\n"]
        cmds += ["D=M\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]
        
        return cmds
        
    '''
    pop temp index
    addr=5+i;sp--;*addr=*sp
    '''
    def popTemp(self,index):
        cmds = [f"//pop temp {index}\n"]

        cmds += ["//addr=5+i\n"]
        cmds += [f"@{index}\n"]
        cmds += ["D=A\n"]
        cmds += [f"@5\n"]
        cmds += ["D=A+D\n"]
        cmds += ["@addr\n"]
        cmds += ["M=D\n"]
        
        cmds += ["//sp--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//*addr=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]
        cmds += ["@addr\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]
        
        return cmds

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

    '''
    push pointer 0/1
    *SP=THIS/THAT;SP++
    '''
    def pushPointer(self, index):
        pointer = 'THIS' if str(index) == '0' else 'THAT'
        cmds = [f"//push pointer {index}\n"]

        cmds += ["//*SP=THIS/THAT\n"]
        cmds += [f"@{pointer}\n"]
        cmds += ["D=M\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]

        cmds += ["//SP++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]

        return cmds

    '''
    pop pointer 0/1
    SP--;THIS/THAT=*SP
    '''
    def popPointer(self, index):
        pointer = 'THIS' if str(index) == '0' else 'THAT'
        cmds = [f"//pop pointer {index}\n"]

        cmds += ["//SP--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]

        cmds += ["//THIS/THAT=*SP\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]
        cmds += [f"@{pointer}\n"]
        cmds += ["M=D\n"]

        return cmds

    '''
    push static index
    *sp = className.index; sp++
    '''
    def pushStatic(self, index):
        addr = self.className+'.'+str(index)
        cmds = [f"//push static {index}\n"]

        cmds += ["//*SP=className.index\n"]
        cmds += [f"@{addr}\n"]
        cmds += ["D=M\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["M=D\n"]

        cmds += ["//sp++\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M+1\n"]

        return cmds

    '''
    pop static index
    sp--;className.index=*sp
    '''
    def popStatic(self, index):
        addr = self.className+'.'+str(index)
        cmds = [f"//pop static {index}\n"]
        
        cmds += ["//SP--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        
        cmds += ["//className.index=*sp\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]

        cmds += [f"@{addr}\n"]
        cmds += ["M=D\n"]

        return cmds

    def writeLabel(self,label):
        cmds = [f"//label {label}\n"]
        cmds += [f"({label})\n"]

        return cmds

    def writeGoto(self,label):
        cmds = [f"//goto {label}\n"]
        cmds += [f"@{label}\n"]
        cmds += ["0;JMP\n"]

        return cmds

    '''
    SP--;D=*SP;@label;D;JGT
    '''
    def writeIf(self,label):
        cmds = [f"//if-goto {label}\n"]
        cmds += ["//SP--\n"]
        cmds += ["@SP\n"]
        cmds += ["M=M-1\n"]
        cmds += ["//D=*SP\n"]
        cmds += ["@SP\n"]
        cmds += ["A=M\n"]
        cmds += ["D=M\n"]
        cmds += [f"@{label}\n"]
        cmds += ["D;JGT\n"]
        
        return cmds

        

