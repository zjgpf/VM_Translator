//init
@256
D=A
@SP
M=D
//call Sys.init 0
//push StaticsTest.$ret.0
@StaticsTest.$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP-5-nArgs
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Sys.init
@Sys.init
0;JMP
(StaticsTest.$ret.0)
//functon Class1.set 0
(Class1.set)
//repeat 0 times: push 0
//push argument 0
//D=segmentPointer+i
@0
D=A
@ARG
D=M+D
//*sp=*D
A=D
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//pop static 0
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@Class1.0
M=D
//push argument 1
//D=segmentPointer+i
@1
D=A
@ARG
D=M+D
//*sp=*D
A=D
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//pop static 1
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@Class1.1
M=D
//push constant 0
//*sp=i
@0
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//return
//endFrame=LCL
@LCL
D=M
@endFrame
M=D
//retAddr=*(endFrame-5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG=pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//SP=ARG+1
@ARG
D=M+1
@SP
M=D
//THAT=*(endFrame-1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS=*(endFrame-2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG=*(endFrame-3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL=*(endFrame-4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
//functon Class1.get 0
(Class1.get)
//repeat 0 times: push 0
//push static 0
//*SP=className.index
@Class1.0
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push static 1
//*SP=className.index
@Class1.1
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//sub
//sp--
@SP
M=M-1
//D=*sp
@SP
A=M
D=M
//sp--
@SP
M=M-1
//*sp=*sp-D
@SP
A=M
M=M-D
//sp++
@SP
M=M+1
//return
//endFrame=LCL
@LCL
D=M
@endFrame
M=D
//retAddr=*(endFrame-5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG=pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//SP=ARG+1
@ARG
D=M+1
@SP
M=D
//THAT=*(endFrame-1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS=*(endFrame-2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG=*(endFrame-3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL=*(endFrame-4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
//functon Sys.init 0
(Sys.init)
//repeat 0 times: push 0
//push constant 6
//*sp=i
@6
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push constant 8
//*sp=i
@8
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//call Class1.set 2
//push Sys$ret.1
@Sys$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP-5-nArgs
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class1.set
@Class1.set
0;JMP
(Sys$ret.1)
//pop temp 0
//addr=5+i
@0
D=A
@5
D=A+D
@addr
M=D
//sp--
@SP
M=M-1
//*addr=*sp
@SP
A=M
D=M
@addr
A=M
M=D
//push constant 23
//*sp=i
@23
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push constant 15
//*sp=i
@15
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//call Class2.set 2
//push Sys$ret.2
@Sys$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP-5-nArgs
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class2.set
@Class2.set
0;JMP
(Sys$ret.2)
//pop temp 0
//addr=5+i
@0
D=A
@5
D=A+D
@addr
M=D
//sp--
@SP
M=M-1
//*addr=*sp
@SP
A=M
D=M
@addr
A=M
M=D
//call Class1.get 0
//push Sys$ret.3
@Sys$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP-5-nArgs
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class1.get
@Class1.get
0;JMP
(Sys$ret.3)
//call Class2.get 0
//push Sys$ret.4
@Sys$ret.4
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP-5-nArgs
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class2.get
@Class2.get
0;JMP
(Sys$ret.4)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP
//functon Class2.set 0
(Class2.set)
//repeat 0 times: push 0
//push argument 0
//D=segmentPointer+i
@0
D=A
@ARG
D=M+D
//*sp=*D
A=D
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//pop static 0
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@Class2.0
M=D
//push argument 1
//D=segmentPointer+i
@1
D=A
@ARG
D=M+D
//*sp=*D
A=D
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//pop static 1
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@Class2.1
M=D
//push constant 0
//*sp=i
@0
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//return
//endFrame=LCL
@LCL
D=M
@endFrame
M=D
//retAddr=*(endFrame-5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG=pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//SP=ARG+1
@ARG
D=M+1
@SP
M=D
//THAT=*(endFrame-1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS=*(endFrame-2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG=*(endFrame-3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL=*(endFrame-4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
//functon Class2.get 0
(Class2.get)
//repeat 0 times: push 0
//push static 0
//*SP=className.index
@Class2.0
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push static 1
//*SP=className.index
@Class2.1
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//sub
//sp--
@SP
M=M-1
//D=*sp
@SP
A=M
D=M
//sp--
@SP
M=M-1
//*sp=*sp-D
@SP
A=M
M=M-D
//sp++
@SP
M=M+1
//return
//endFrame=LCL
@LCL
D=M
@endFrame
M=D
//retAddr=*(endFrame-5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG=pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//SP=ARG+1
@ARG
D=M+1
@SP
M=D
//THAT=*(endFrame-1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS=*(endFrame-2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG=*(endFrame-3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL=*(endFrame-4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
