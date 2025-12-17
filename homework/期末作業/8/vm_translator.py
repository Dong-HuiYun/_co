import os
import sys
from parser import Parser
from code_writer import CodeWriter
from command_type import CommandType

class VMTranslator:
    def __init__(self, input_path):
        if os.path.isdir(input_path):
            self.files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".vm")]
            self.is_multi_file = len(self.files) > 1
            output_name = os.path.basename(input_path.rstrip("/\\"))
            self.output_path = os.path.join(input_path, output_name + ".asm")
        else:
            self.files = [input_path]
            self.is_multi_file = False
            self.output_path = input_path.replace(".vm", ".asm")

    def translate(self):
        code_writer = CodeWriter(self.output_path, self.is_multi_file)

        for file_path in self.files:
            print(f"Processing: {file_path}")
            parser = Parser(file_path)
            code_writer.set_file_name(os.path.basename(file_path))

            while parser.has_more_commands():
                parser.advance()
                if parser.current_command is None:
                    continue
                    
                cmd_type = parser.command_type()
                print(f"  Command: {parser.current_command}, Type: {cmd_type}")

                if cmd_type == CommandType.C_ARITHMETIC:
                    code_writer.write_arithmetic(parser.arg1())
                elif cmd_type in [CommandType.C_PUSH, CommandType.C_POP]:
                    code_writer.write_push_pop(cmd_type, parser.arg1(), parser.arg2())
                elif cmd_type == CommandType.C_LABEL:
                    code_writer.write_label(parser.arg1())
                elif cmd_type == CommandType.C_GOTO:
                    code_writer.write_goto(parser.arg1())
                elif cmd_type == CommandType.C_IF:
                    code_writer.write_if(parser.arg1())
                elif cmd_type == CommandType.C_FUNCTION:
                    code_writer.write_function(parser.arg1(), parser.arg2())
                elif cmd_type == CommandType.C_CALL:
                    code_writer.write_call(parser.arg1(), parser.arg2())
                elif cmd_type == CommandType.C_RETURN:
                    code_writer.write_return()

        code_writer.close()
        print(f"\nTranslation completed: {self.output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vm_translator.py <file.vm or directory>")
        sys.exit(1)

    translator = VMTranslator(sys.argv[1])
    translator.translate()