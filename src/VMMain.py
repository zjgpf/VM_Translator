from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
import sys
import pdb

ARITHMETIC_LOGICAL_SINGLE = ['neg', 'not']
ARITHMETIC_LOGICAL_DOUBLE = ['add','sub','gt','lt','and','or','eq']

DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/BasicTest/BasicTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/SimpleAdd/SimpleAdd.vm'
class VMMain:
    def __init__(self, inputPath):
        with open(inputPath, 'r') as f:
            content = f.read()
        fileName = inputPath.split('/')[-1][:-3]
        outputName = fileName+'.asm'
        self.outputPath = inputPath.replace(fileName+'.vm', outputName)

        self.parser = VMParser(content)
        self.codeWriter = VMCodeWriter()

        self.stack = []
        self.asmCmds = []
    
    def run(self):
        parser = self.parser
        codeWriter = self.codeWriter
        stack = self.stack
        asmCmds = self.asmCmds
        while(parser.hasMoreCommands()):
            parser.advance()
            commandType = parser.commandType()

            if commandType in ['C_PUSH','C_POP']: 
                segment,index = parser.arg1(),parser.arg2()
                if commandType == 'C_PUSH': stack += [index]
                else: stack.pop()
                asmCmds += codeWriter.writePushPop(commandType, segment, index)

            elif commandType == 'C_ARITHMETIC':
                cmd = parser.arg1()
                if cmd in ARITHMETIC_LOGICAL_SINGLE:
                    num = stack.pop()
                    asmCmds += codeWriter.writeArithmetic(cmd, num)
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    asmCmds += codeWriter.writeArithmetic(cmd, num1, num2)
        print('aaa')
        print(asmCmds)
         
        

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    vm = VMMain(inputPath)
    vm.run()
