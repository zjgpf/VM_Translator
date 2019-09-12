from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
import sys
import os
import pdb

DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/SimpleAdd/SimpleAdd.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/MyTest/SimpleAdd.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/BasicTest/BasicTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/PointerTest/PointerTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/StaticTest/StaticTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/StackArithmetic/StackTest/StackTest.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/ProgramFlow/BasicLoop/BasicLoop.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/ProgramFlow/FibonacciSeries/FibonacciSeries.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/FunctionCalls/SimpleFunction/SimpleFunction.vm'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/FunctionCalls/FibonacciElement'
DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/FunctionCalls/StaticsTest'

class VMMain:
    def __init__(self, inputPath):
        isDir = True
        if inputPath[-3:] == '.vm': isDir = False
        self.isDir = isDir

        if not isDir:
            with open(inputPath, 'r') as f:
                self.content = f.read()
            fileName = inputPath.split('/')[-1][:-3]
            self.className = fileName
            outputName = fileName+'.asm'
            self.outputPath = inputPath.replace(fileName+'.vm', outputName)

        else:
            contents = {}
            self.fileName = inputPath.split('/')[-1] + '.asm'
            self.outputPath = os.path.join(inputPath,self.fileName)
            files = os.listdir(inputPath)   
            for file in files:
                if not file[-3:] == '.vm': continue
                with open(os.path.join(inputPath,file), 'r') as f:
                    contents[file[:-3]] = f.read()
            
            self.contents = contents

        self.asmCmds = []
    
    def run(self):
        if not self.isDir: self.runSingleFile()
        else: self.runDir()

    def runDir(self):
        contents = self.contents       
        asmCmds = self.asmCmds
        initClassName = self.fileName[:-3]
        codeWriter = VMCodeWriter(initClassName)
        self.asmCmds += codeWriter.writeInit()

        for className, content in contents.items():
            self.content = content
            self.className = className
            self.runSingleFile(False)
        
        with open(self.outputPath, 'w') as f:
            f.write(''.join(asmCmds))
        
        

    def runSingleFile(self, isWrite=True):
        parser = VMParser(self.content)
        codeWriter = VMCodeWriter(self.className)
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

            elif commandType == 'C_LABEL':
                cmd = parser.arg1()
                asmCmds += codeWriter.writeLabel(cmd)

            elif commandType == 'C_GOTO':
                cmd = parser.arg1()
                asmCmds += codeWriter.writeGoto(cmd)

            elif commandType == 'C_IF':
                cmd = parser.arg1()
                asmCmds += codeWriter.writeIf(cmd)

            elif commandType == 'C_FUNCTION':
                functionName,numVars = parser.arg1(),parser.arg2()
                asmCmds += codeWriter.writeFunction(functionName, numVars)

            elif commandType == 'C_CALL':
                functionName,numArgs = parser.arg1(),parser.arg2()
                asmCmds += codeWriter.writeCall(functionName, numArgs)

            elif commandType == 'C_RETURN':
                asmCmds += codeWriter.writeReturn()
            
        if isWrite:
            with open(self.outputPath, 'w') as f:
                f.write(''.join(asmCmds))
         
        

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    vm = VMMain(inputPath)
    vm.run()
