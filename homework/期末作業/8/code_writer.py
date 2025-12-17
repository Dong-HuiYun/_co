from constants import SEGMENTS

class CodeWriter:
    def __init__(self, output_path, is_multi_file=False):
        self.output_file = open(output_path, 'w')
        self.label_counter = 0
        self.current_function = None
        self.current_file = None
        self.is_multi_file = is_multi_file
        if is_multi_file:
            self.write_bootstrap()

    def set_file_name(self, filename):
        """設置當前處理的文件名（用於 static 變數命名）"""
        self.current_file = filename.replace('.vm', '')

    def write_bootstrap(self):
        """引導代碼：設置 SP=256，調用 Sys.init"""
        self.output_file.write("@256\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=D\n")
        self.write_call("Sys.init", 0)

    def write_arithmetic(self, command):
        """處理算術和邏輯指令"""
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
        else:
            raise ValueError(f"Unknown arithmetic command: {command}")
        self.output_file.write(asm_code)

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
        """處理 push/pop 指令"""
        # 處理 Enum 或字符串
        if hasattr(command, 'name'):
            cmd_str = command.name.split('_')[1].lower()
        elif hasattr(command, 'value'):
            cmd_str = command.value.split('_')[1].lower()
        else:
            cmd_str = str(command).split('_')[1].lower()
        
        if cmd_str == "push":
            asm_code = self._push_segment(segment, int(index))
        else:  # pop
            asm_code = self._pop_segment(segment, int(index))
        
        if asm_code is None:
            raise ValueError(f"Unsupported operation: {cmd_str} {segment} {index}")
        
        self.output_file.write(asm_code)

    def _push_segment(self, segment, index):
        if segment == "constant":
            return f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment in ["local", "argument", "this", "that"]:
            base = SEGMENTS[segment]
            return f"@{base}\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "temp":
            addr = 5 + index
            return f"@{addr}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "pointer":
            addr = 3 + index
            return f"@{addr}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif segment == "static":
            return f"@{self.current_file}.{index}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return None

    def _pop_segment(self, segment, index):
        if segment in ["local", "argument", "this", "that"]:
            base = SEGMENTS[segment]
            return f"@{base}\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D\n"
        elif segment == "temp":
            addr = 5 + index
            return f"@SP\nM=M-1\nA=M\nD=M\n@{addr}\nM=D\n"
        elif segment == "pointer":
            addr = 3 + index
            return f"@SP\nM=M-1\nA=M\nD=M\n@{addr}\nM=D\n"
        elif segment == "static":
            return f"@SP\nM=M-1\nA=M\nD=M\n@{self.current_file}.{index}\nM=D\n"
        return None

    def write_label(self, label):
        """生成標籤"""
        if self.current_function:
            # 在函數內部：使用 function$label 格式
            self.output_file.write(f"({self.current_function}${label})\n")
        else:
            # 全局標籤：直接使用 label
            self.output_file.write(f"({label})\n")

    def write_goto(self, label):
        """生成無條件跳轉"""
        if self.current_function:
            self.output_file.write(f"@{self.current_function}${label}\n")
        else:
            self.output_file.write(f"@{label}\n")
        self.output_file.write("0;JMP\n")

    def write_if(self, label):
        """生成條件跳轉"""
        self.output_file.write("@SP\n")
        self.output_file.write("AM=M-1\n")
        self.output_file.write("D=M\n")
        if self.current_function:
            self.output_file.write(f"@{self.current_function}${label}\n")
        else:
            self.output_file.write(f"@{label}\n")
        self.output_file.write("D;JNE\n")

    def write_function(self, function_name, num_locals):
        """生成函數定義"""
        self.current_function = function_name
        self.output_file.write(f"({function_name})\n")
        for _ in range(int(num_locals)):
            # 初始化局部變數為 0
            self.output_file.write("@SP\n")
            self.output_file.write("A=M\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@SP\n")
            self.output_file.write("M=M+1\n")

    def write_call(self, function_name, num_args):
        """生成函數調用"""
        return_label = f"RETURN_{self.label_counter}"
        self.label_counter += 1

        # 推送返回地址
        self.output_file.write(f"@{return_label}\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=M+1\n")

        # 推送 LCL、ARG、THIS、THAT
        for reg in ["LCL", "ARG", "THIS", "THAT"]:
            self.output_file.write(f"@{reg}\n")
            self.output_file.write("D=M\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M\n")
            self.output_file.write("M=D\n")
            self.output_file.write("@SP\n")
            self.output_file.write("M=M+1\n")

        # 設置新的 ARG = SP - n - 5
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.output_file.write(f"@{int(num_args) + 5}\n")
        self.output_file.write("D=D-A\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")

        # 設置 LCL = SP
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")

        # 跳轉到目標函數
        self.output_file.write(f"@{function_name}\n")
        self.output_file.write("0;JMP\n")

        # 返回標籤
        self.output_file.write(f"({return_label})\n")

    def write_return(self):
        """生成函數返回"""
        # FRAME = LCL (保存到 R14)
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@R14\n")
        self.output_file.write("M=D\n")

        # RET = *(FRAME-5) (保存返回地址到 R13)
        self.output_file.write("@5\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@R13\n")
        self.output_file.write("M=D\n")

        # *ARG = pop() (將返回值放入 ARG[0])
        self.output_file.write("@SP\n")
        self.output_file.write("AM=M-1\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")

        # SP = ARG + 1
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M+1\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=D\n")

        # 恢復 THAT、THIS、ARG、LCL
        regs = ["THAT", "THIS", "ARG", "LCL"]
        for i, reg in enumerate(regs, start=1):
            self.output_file.write("@R14\n")
            self.output_file.write("D=M\n")
            self.output_file.write(f"@{i}\n")
            self.output_file.write("A=D-A\n")
            self.output_file.write("D=M\n")
            self.output_file.write(f"@{reg}\n")
            self.output_file.write("M=D\n")

        # 跳回調用者
        self.output_file.write("@R13\n")
        self.output_file.write("A=M\n")
        self.output_file.write("0;JMP\n")

    def close(self):
        """關閉輸出文件"""
        self.output_file.close()