import re
from command_type import CommandType

class Parser:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.lines = f.readlines()
        self.current_line = 0
        self.current_command = None

    def has_more_commands(self):
        return self.current_line < len(self.lines)

    def advance(self):
        """讀取下一條指令，跳過空行和註釋"""
        while self.has_more_commands():
            line = self.lines[self.current_line].strip()
            self.current_line += 1
            
            # 跳過空行
            if not line:
                continue
                
            # 跳過純註釋行
            if line.startswith("//"):
                continue
                
            # 去掉行內註釋
            line = re.sub(r"//.*", "", line).strip()
            
            if line:  # 確保處理後還有內容
                self.current_command = line
                return
        
        self.current_command = None

    def command_type(self):
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if not parts:
            return None
            
        cmd = parts[0]
        
        if cmd in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]:
            return CommandType.C_ARITHMETIC
        elif cmd == "push":
            return CommandType.C_PUSH
        elif cmd == "pop":
            return CommandType.C_POP
        elif cmd == "label":
            return CommandType.C_LABEL
        elif cmd == "goto":
            return CommandType.C_GOTO
        elif cmd == "if-goto":
            return CommandType.C_IF
        elif cmd == "function":
            return CommandType.C_FUNCTION
        elif cmd == "call":
            return CommandType.C_CALL
        elif cmd == "return":
            return CommandType.C_RETURN
        else:
            raise ValueError(f"Unknown command: {cmd}")

    def arg1(self):
        """返回第一個參數"""
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if self.command_type() == CommandType.C_ARITHMETIC:
            return parts[0]
        elif len(parts) > 1:
            return parts[1]
        return None

    def arg2(self):
        """返回第二個參數（數字）"""
        if not self.current_command:
            return None
            
        parts = self.current_command.split()
        if len(parts) > 2:
            return parts[2]
        return None