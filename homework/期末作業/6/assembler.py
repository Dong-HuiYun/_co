import re
import sys

class HackAssembler:
    def __init__(self):
        # 预定义的符号表（Hack 语言规范）
        self.symbol_table = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5,
            "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10,
            "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
            "SCREEN": 16384, "KBD": 24576
        }
        
        # C 指令的 comp 部分二进制映射
        self.comp_table = {
            "0": "0101010", "1": "0111111", "-1": "0111010",
            "D": "0001100", "A": "0110000", "M": "1110000",
            "!D": "0001101", "!A": "0110001", "!M": "1110001",
            "-D": "0001111", "-A": "0110011", "-M": "1110011",
            "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
            "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
            "D+A": "0000010", "D+M": "1000010", "D-A": "0010011",
            "D-M": "1010011", "A-D": "0000111", "M-D": "1000111",
            "D&A": "0000000", "D&M": "1000000", "D|A": "0010101",
            "D|M": "1010101"
        }
        
        # dest 部分二进制映射
        self.dest_table = {
            "null": "000", "M": "001", "D": "010", "MD": "011", "DM": "011",
            "A": "100", "AM": "101", "AD": "110", "ADM": "111", "AMD": "111"
        }
        
        # jump 部分二进制映射
        self.jump_table = {
            "null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
        }
        
        self.next_variable_address = 16  # 变量从地址 16 开始分配

    def remove_comments_and_whitespace(self, line):
        """移除注释和前后空白"""
        line = line.split("//")[0].strip()
        return line

    def first_pass(self, lines):
        """第一遍扫描：处理标签符号"""
        clean_lines = []
        line_number = 0
        
        for line in lines:
            clean_line = self.remove_comments_and_whitespace(line)
            if not clean_line:
                continue
            
            # 检查是否是标签定义，如 (LOOP)
            if clean_line.startswith("(") and clean_line.endswith(")"):
                label = clean_line[1:-1]
                self.symbol_table[label] = line_number
            else:
                clean_lines.append(clean_line)
                line_number += 1
        
        return clean_lines

    def second_pass(self, lines):
        """第二遍扫描：翻译指令"""
        binary_lines = []
        
        for line in lines:
            if line.startswith("@"):
                # A 指令
                binary = self.translate_a_instruction(line)
            else:
                # C 指令
                binary = self.translate_c_instruction(line)
            binary_lines.append(binary)
        
        return binary_lines

    def translate_a_instruction(self, line):
        """翻译 A 指令：@value"""
        symbol = line[1:]  # 移除 @
        
        # 如果是数字，直接使用
        if symbol.isdigit():
            address = int(symbol)
        else:
            # 如果是符号，从符号表中查找或添加
            if symbol not in self.symbol_table:
                self.symbol_table[symbol] = self.next_variable_address
                self.next_variable_address += 1
            address = self.symbol_table[symbol]
        
        # 转换为 16 位二进制，前面补 0
        binary = format(address, '016b')
        return binary

    def translate_c_instruction(self, line):
        """翻译 C 指令：dest=comp;jump"""
        dest = "null"
        comp = line
        jump = "null"
        
        # 解析 dest 部分
        if "=" in line:
            dest, comp = line.split("=")
        
        # 解析 jump 部分
        if ";" in comp:
            comp, jump = comp.split(";")
        
        # 特殊处理：DM 和 MD 等价，ADM 和 AMD 等价
        if dest == "DM":
            dest = "MD"
        elif dest == "ADM":
            dest = "AMD"
        
        # 查找二进制码
        comp_bits = self.comp_table.get(comp, "0000000")
        dest_bits = self.dest_table.get(dest, "000")
        jump_bits = self.jump_table.get(jump, "000")
        
        # 组合成 16 位指令
        binary = "111" + comp_bits + dest_bits + jump_bits
        return binary

    def assemble(self, asm_file_path):
        """主汇编函数"""
        # 读取源文件
        with open(asm_file_path, 'r') as f:
            lines = f.readlines()
        
        # 第一遍扫描：处理标签
        clean_lines = self.first_pass(lines)
        
        # 第二遍扫描：生成二进制码
        binary_lines = self.second_pass(clean_lines)
        
        # 输出到 .hack 文件
        hack_file_path = asm_file_path.replace('.asm', '.hack')
        with open(hack_file_path, 'w') as f:
            for binary_line in binary_lines:
                f.write(binary_line + "\n")
        
        print(f"Assembly complete! Output saved to {hack_file_path}")
        return hack_file_path

# 主程序入口
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python assembler.py <file.asm>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not input_file.endswith('.asm'):
        print("Error: Input file must have .asm extension")
        sys.exit(1)
    
    assembler = HackAssembler()
    assembler.assemble(input_file)