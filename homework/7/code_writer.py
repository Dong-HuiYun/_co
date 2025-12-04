# code_writer.py

from constants import SEGMENTS, ARITHMETIC_COMMANDS

class CodeWriter:
    def __init__(self, output_file):
        self.output = open(output_file, 'w')
        self.label_counter = 0

    def write_arithmetic(self, command):
        asm_code = ""
        if command == "add":
            asm_code = self._binary_operation("+")
        elif command == "sub":
            asm_code = self._binary_operation("-")
        elif command == "neg":
            asm_code = self._unary_operation("-")
        elif command in ["eq", "gt", "lt"]:
            asm_code = self._comparison(command)
        elif command == "and":
            asm_code = self._binary_operation("&")
        elif command == "or":
            asm_code = self._binary_operation("|")
        elif command == "not":
            asm_code = self._unary_operation("!")
        self.output.write(asm_code)

    def _binary_operation(self, op):
        return f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M{op}D\n@SP\nM=M+1\n"

    def _unary_operation(self, op):
        return f"@SP\nM=M-1\nA=M\nM={op}M\n@SP\nM=M+1\n"

    def _comparison(self, comp):
        label_true = f"TRUE_{self.label_counter}"
        label_end = f"END_{self.label_counter}"
        self.label_counter += 1
        return f"""@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@{label_true}
D;J{comp.upper()}
@SP
A=M
M=0
@{label_end}
0;JMP
({label_true})
@SP
A=M
M=-1
({label_end})
@SP
M=M+1
"""

    def write_push_pop(self, command, segment, index):
        if command == "push":
            asm_code = self._push_segment(segment, index)
        else:  # pop
            asm_code = self._pop_segment(segment, index)
        
        # 確保 asm_code 不是 None
        if asm_code is None:
            raise ValueError(f"Unsupported operation: {command} {segment} {index}")
        
        self.output.write(asm_code)

    def _push_segment(self, segment, index):
        if segment == "constant":
            return f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment in ["local", "argument", "this", "that"]:
            base = SEGMENTS[segment]
            return f"@{base}\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "temp":
            base = 5  # R5 的位址
            addr = base + index
            return f"@{addr}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "pointer":
            base = 3  # R3 的位址
            addr = base + index
            return f"@{addr}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "static":
            addr = 16 + index
            return f"@{addr}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        else:
            return None  # 不支援的 segment

    def _pop_segment(self, segment, index):
        if segment in ["local", "argument", "this", "that"]:
            base = SEGMENTS[segment]
            return f"@{base}\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n"
        elif segment == "temp":
            base = 5  # R5 的位址
            addr = base + index
            return f"@SP\nM=M-1\nA=M\nD=M\n@{addr}\nM=D\n"
        elif segment == "pointer":
            base = 3  # R3 的位址
            addr = base + index
            return f"@SP\nM=M-1\nA=M\nD=M\n@{addr}\nM=D\n"
        elif segment == "static":
            addr = 16 + index
            return f"@SP\nM=M-1\nA=M\nD=M\n@{addr}\nM=D\n"
        else:
            return None  # 不支援的 segment

    def close(self):
        self.output.close()