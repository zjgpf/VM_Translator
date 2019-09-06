from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
import sys
import pdb

DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/SimpleAdd/SimpleAdd.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/MyTest/SimpleAdd.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/StackTest/StackTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/BasicTest/BasicTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/PointerTest/PointerTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/StaticTest/StaticTest.vm'

class VMMain:
    def __init__(self, inputPath):
        with open(inputPath, 'r') as f:
            content = f.read()
        fileName = inputPath.split('/')[-1][:-3]
        outputName = fileName+'.asm'
        self.outputPath = inputPath.replace(fileName+'.vm', outputName)

        self.parser = VMParser(content)
        self.codeWriter = VMCodeWriter(fileName)

        self.asmCmds = []
    
    def run(self):
        parser = self.parser
        codeWriter = self.codeWriter
        asmCmds = self.asmCmds
        while(parser.hasMoreCommands()):
            parser.advance()
            commandType = parser.commandType()

            if commandType in ['C_PUSH','C_POP']: 
                segment,index = parser.arg1(),parser.arg2()
                asmCmds += codeWriter.writePushPop(commandType, segment, index)

            elif commandType == 'C_ARITHMETIC':
                cmd = parser.arg1()
                asmCmds += codeWriter.writeArithmetic(cmd)
        with open(self.outputPath, 'w') as f:
            f.write(''.join(asmCmds))
         
        

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    vm = VMMain(inputPath)
    vm.run()
