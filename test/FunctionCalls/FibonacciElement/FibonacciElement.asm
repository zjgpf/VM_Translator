//init
@256
D=A
@SP
M=D
//call Sys.init 0
//push FibonacciElement.$ret.0
@FibonacciElement.$ret.0
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
(FibonacciElement.$ret.0)
//functon Main.fibonacci 0
(Main.fibonacci)
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
//push constant 2
//*sp=i
@2
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//Lt
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
//D=*sp-D
@SP
A=M
D=M-D
//go to lt if D=0
@Main_Lt1
D;JLT
//*sp=0
@SP
A=M
M=0
//go to stop
@Main_STOP1
0;JMP
(Main_Lt1)
//*sp=-1
@SP
A=M
M=-1
(Main_STOP1)
//sp++
@SP
M=M+1
//if-goto IF_TRUE
//SP--
@SP
M=M-1
//D=*SP
@SP
A=M
D=M
@IF_TRUE
D;JNE
//goto IF_FALSE
@IF_FALSE
0;JMP
//label IF_TRUE
(IF_TRUE)
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
//label IF_FALSE
(IF_FALSE)
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
//push constant 2
//*sp=i
@2
D=A
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
//call Main.fibonacci 1
//push Main$ret.2
@Main$ret.2
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
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main$ret.2)
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
//push constant 1
//*sp=i
@1
D=A
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
//call Main.fibonacci 1
//push Main$ret.3
@Main$ret.3
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
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main$ret.3)
//add
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
//*sp=D+*sp 
@SP
A=M
M=M+D
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
//push constant 4
//*sp=i
@4
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//call Main.fibonacci 1
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
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
(Sys$ret.4)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP
