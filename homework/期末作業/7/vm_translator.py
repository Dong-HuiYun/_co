# vm_translator.py

import sys
from parser import Parser
from code_writer import CodeWriter


def translate_vm_file(vm_file, asm_file):
    parser = Parser(vm_file)
    writer = CodeWriter(asm_file)

    while parser.has_more_commands():
        parser.advance()
        cmd_type = parser.command_type()
        
        # 加入除錯輸出
        print(f"Processing: {parser.current_command}, Type: {cmd_type}")
        
        if cmd_type == "C_ARITHMETIC":
            writer.write_arithmetic(parser.arg1())
        elif cmd_type in ["C_PUSH", "C_POP"]:
            command = cmd_type.split("_")[1].lower()
            segment = parser.arg1()
            index = parser.arg2()
            print(f"  -> {command} {segment} {index}")
            writer.write_push_pop(command, segment, index)
    
    writer.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vm_translator.py <vm_file>")
        sys.exit(1)
    
    vm_file = sys.argv[1]
    asm_file = vm_file.replace(".vm", ".asm")
    
    translate_vm_file(vm_file, asm_file)
    print(f"Translated {vm_file} to {asm_file}")