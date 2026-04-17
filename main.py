from parser import parse
from compiler_error import VASMCompilationError
from sys import argv

def main():
    try:
        if(len(argv) == 2):
            parse(argv[1])
        if(len(argv) == 3):
            parse(argv[1], argv[2])
        if(len(argv) == 1):
            print("[VASM Compiler for MIPS32]")
            print(f"--> Compilation error (Target file not found):")
            print(f"Expected: File name")
    
    except VASMCompilationError as err:
        err.print_error()

if __name__ == "__main__":
    main()
