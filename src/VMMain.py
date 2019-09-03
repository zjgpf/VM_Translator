from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
import sys

DEFAULTPATH='/Users/pengfeigao/git/vm_translator/test/MemoryAccess/BasicTest/BasicTest.vm'
class VMMain:
    def __init__(self, inputPath):
        with open(inputPath, 'r') as f:
            content = f.read()
        fileName = inputPath.split('/')[-1][:-3]
        outputName = fileName+'.asm'
        self.outputPath = inputPath.replace(fileName+'.vm', outputName)

        self.parser = VMParser(content)
        self.codeWriter = VMCodeWriter()
    
    def run(self):
        parser = self.parser
        codeWriter = self.codeWriter
        #parser.hasMoreCommands()
        #print(parser.nextCmd)
        while(parser.hasMoreCommands()):
            parser.advance()
            print(parser.curCmd)
            print(parser.commandType())
            print(parser.arg1())
            print('************************')
         
        

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    vm = VMMain(inputPath)
    vm.run()
