//push constant 111
//*sp=i
@111
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push constant 333
//*sp=i
@333
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push constant 888
//*sp=i
@888
D=A
@SP
A=M
M=D
//sp++
@SP
M=M+1
//pop static 8
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@StaticTest.8
M=D
//pop static 3
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@StaticTest.3
M=D
//pop static 1
//SP--
@SP
M=M-1
//className.index=*sp
@SP
A=M
D=M
@StaticTest.1
M=D
//push static 3
//*SP=className.index
@StaticTest.3
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
//push static 1
//*SP=className.index
@StaticTest.1
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
//push static 8
//*SP=className.index
@StaticTest.8
D=M
@SP
A=M
M=D
//sp++
@SP
M=M+1
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