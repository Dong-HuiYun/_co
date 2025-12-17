# parser.py

# 正确导入 ARITHMETIC_COMMANDS
try:
    from constants import ARITHMETIC_COMMANDS
except ImportError:
    # 如果导入失败，直接定义
    ARITHMETIC_COMMANDS = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

class Parser:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        self.lines = [self._clean_line(line) for line in lines if self._clean_line(line)]
        self.current_index = 0
        self.current_command = None

    def _clean_line(self, line):
        line = line.strip()
        if "//" in line:
            line = line[:line.index("//")].strip()
        return line

    def has_more_commands(self):
        return self.current_index < len(self.lines)

    def advance(self):
        self.current_command = self.lines[self.current_index]
        self.current_index += 1

    def command_type(self):
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if not parts:  # 空行
            return None
            
        if parts[0] in ARITHMETIC_COMMANDS:
            return "C_ARITHMETIC"
        elif parts[0] == "push":
            return "C_PUSH"
        elif parts[0] == "pop":
            return "C_POP"
        return None

    def arg1(self):
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if self.command_type() == "C_ARITHMETIC":
            return parts[0]
        elif len(parts) > 1:
            return parts[1]
        return None

    def arg2(self):
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if len(parts) > 2:
            try:
                return int(parts[2])
            except ValueError:
                return parts[2]
        return None