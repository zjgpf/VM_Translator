//push constant 9
//*sp=i
@9
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
//Not
//sp--
@SP
M=M-1
//*sp = -*sp
@SP
A=M
M=!M
//sp++
@SP
M=M+1
