import re

class JackTokenizer:
    # Jack語言關鍵字
    KEYWORDS = [
        'class', 'constructor', 'function', 'method', 'field', 'static',
        'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
        'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'
    ]
    
    # 符號
    SYMBOLS = [
        '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/',
        '&', '|', '<', '>', '=', '~'
    ]
    
    # 需要轉義的符號映射
    ESCAPE_MAP = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '&': '&amp;'
    }
    
    def __init__(self, input_file):
        """初始化tokenizer，讀取文件並預處理"""
        with open(input_file, 'r') as f:
            content = f.read()
        
        # 移除註釋和空行，並標準化空格
        self._tokens = self._tokenize(content)
        self._current_token = None
        self._index = -1
        self._total_tokens = len(self._tokens)
    
    def _remove_comments(self, content):
        """移除所有類型的註釋"""
        # 移除多行註釋 /* ... */
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        # 移除單行註釋 // ...
        content = re.sub(r'//.*', '', content)
        return content
    
    def _tokenize(self, content):
        """將內容轉換為tokens列表"""
        # 移除註釋
        content = self._remove_comments(content)
        
        # 將字符串常量單獨處理
        tokens = []
        i = 0
        n = len(content)
        
        while i < n:
            char = content[i]
            
            # 跳過空白字符
            if char.isspace():
                i += 1
                continue
            
            # 處理字符串常量
            if char == '"':
                j = i + 1
                while j < n and content[j] != '"':
                    j += 1
                string_content = content[i+1:j]
                tokens.append(('stringConstant', string_content))
                i = j + 1
                continue
            
            # 處理符號
            if char in self.SYMBOLS:
                tokens.append(('symbol', char))
                i += 1
                continue
            
            # 處理數字
            if char.isdigit():
                j = i
                while j < n and content[j].isdigit():
                    j += 1
                number = content[i:j]
                tokens.append(('integerConstant', number))
                i = j
                continue
            
            # 處理關鍵字和標識符
            if char.isalpha() or char == '_':
                j = i
                while j < n and (content[j].isalnum() or content[j] == '_'):
                    j += 1
                word = content[i:j]
                
                # 檢查是否是關鍵字
                if word in self.KEYWORDS:
                    tokens.append(('keyword', word))
                else:
                    tokens.append(('identifier', word))
                i = j
                continue
            
            # 其他字符（正常情況下不應該出現）
            i += 1
        
        return tokens
    
    def has_more_tokens(self):
        """是否還有更多tokens"""
        return self._index < self._total_tokens - 1
    
    def advance(self):
        """讀取下一個token"""
        if self.has_more_tokens():
            self._index += 1
            self._current_token = self._tokens[self._index]
        else:
            self._current_token = None
    
    def token_type(self):
        """返回當前token的類型"""
        if not self._current_token:
            return None
        return self._current_token[0]
    
    def keyword(self):
        """返回當前關鍵字token的關鍵字"""
        if self.token_type() == 'keyword':
            return self._current_token[1]
        return None
    
    def symbol(self):
        """返回當前符號token的符號"""
        if self.token_type() == 'symbol':
            symbol = self._current_token[1]
            # 返回轉義後的符號
            return self.ESCAPE_MAP.get(symbol, symbol)
        return None
    
    def identifier(self):
        """返回當前標識符token的標識符"""
        if self.token_type() == 'identifier':
            return self._current_token[1]
        return None
    
    def int_val(self):
        """返回當前整數常量的值"""
        if self.token_type() == 'integerConstant':
            return int(self._current_token[1])
        return None
    
    def string_val(self):
        """返回當前字符串常量的值"""
        if self.token_type() == 'stringConstant':
            return self._current_token[1]
        return None
    
    def peek_next_token(self):
        """查看下一個token但不移動指針"""
        if self._index < self._total_tokens - 1:
            return self._tokens[self._index + 1]
        return None
    
    def write_xml(self, output_file):
        """將所有tokens寫入XML文件"""
        with open(output_file, 'w') as f:
            f.write('<tokens>\n')
            
            # 重置索引以便重新讀取所有tokens
            original_index = self._index
            original_token = self._current_token
            self._index = -1
            self._current_token = None
            
            while self.has_more_tokens():
                self.advance()
                token_type = self.token_type()
                
                if token_type == 'keyword':
                    f.write(f'<keyword> {self.keyword()} </keyword>\n')
                elif token_type == 'symbol':
                    f.write(f'<symbol> {self.symbol()} </symbol>\n')
                elif token_type == 'identifier':
                    f.write(f'<identifier> {self.identifier()} </identifier>\n')
                elif token_type == 'integerConstant':
                    f.write(f'<integerConstant> {self.int_val()} </integerConstant>\n')
                elif token_type == 'stringConstant':
                    f.write(f'<stringConstant> {self.string_val()} </stringConstant>\n')
            
            f.write('</tokens>\n')
            
            # 恢復原始狀態
            self._index = original_index
            self._current_token = original_token