
Language Design: 

    Assembly extension: .vasm 
    Compiled bin extension: .vbin 

Syntax Design:

$ -> register directions
# -> number literals 
, -> optional commas between the arguments

What instructions are available?:

    The instruction set we are going to use
    is a reduced MIPS32 set, if the project
    gets big, then we are gonna support all
    MIPS instructions

Assembly Example:

    # This is a comment
    ADD $save $num1 $num2
    SUB $save $num1 $num2
    ADDI $save $num1 imm
