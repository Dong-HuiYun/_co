class CompilationEngine:
    def __init__(self, tokenizer, output_file):
        self.tokenizer = tokenizer
        self.output_file = open(output_file, 'w')
        self.indent_level = 0
    
    def _write_tag(self, tag, value=None, is_open=True):
        """寫入XML標籤"""
        indent = '  ' * self.indent_level
        
        if is_open:
            if value is not None:
                self.output_file.write(f'{indent}<{tag}> {value} </{tag}>\n')
            else:
                self.output_file.write(f'{indent}<{tag}>\n')
                self.indent_level += 1
        else:
            self.indent_level -= 1
            indent = '  ' * self.indent_level
            self.output_file.write(f'{indent}</{tag}>\n')
    
    def _write_current_token(self):
        """寫入當前token"""
        token_type = self.tokenizer.token_type()
        
        if token_type == 'keyword':
            self._write_tag('keyword', self.tokenizer.keyword())
        elif token_type == 'symbol':
            self._write_tag('symbol', self.tokenizer.symbol())
        elif token_type == 'identifier':
            self._write_tag('identifier', self.tokenizer.identifier())
        elif token_type == 'integerConstant':
            self._write_tag('integerConstant', str(self.tokenizer.int_val()))
        elif token_type == 'stringConstant':
            self._write_tag('stringConstant', self.tokenizer.string_val())
    
    def _advance_and_write(self):
        """前進並寫入當前token"""
        self._write_current_token()
        if self.tokenizer.has_more_tokens():
            self.tokenizer.advance()
    
    def compile_class(self):
        """編譯完整的class"""
        # class className { classVarDec* subroutineDec* }
        self.tokenizer.advance()  # 跳過初始token
        self._write_tag('class')
        
        # 'class' keyword
        self._advance_and_write()
        
        # className
        self._advance_and_write()
        
        # '{'
        self._advance_and_write()
        
        # classVarDec*
        while self.tokenizer.has_more_tokens() and self.tokenizer.token_type() == 'keyword':
            keyword = self.tokenizer.keyword()
            if keyword in ['static', 'field']:
                self.compile_class_var_dec()
            else:
                break
        
        # subroutineDec*
        while self.tokenizer.has_more_tokens() and self.tokenizer.token_type() == 'keyword':
            keyword = self.tokenizer.keyword()
            if keyword in ['constructor', 'function', 'method']:
                self.compile_subroutine()
            else:
                break
        
        # '}'
        self._advance_and_write()
        
        self._write_tag('class', is_open=False)
    
    def compile_class_var_dec(self):
        """編譯class變量聲明"""
        # (static | field) type varName (',' varName)* ';'
        self._write_tag('classVarDec')
        
        # static | field
        self._advance_and_write()
        
        # type
        self._advance_and_write()
        
        # varName
        self._advance_and_write()
        
        # (',' varName)*
        while self.tokenizer.has_more_tokens() and self.tokenizer.symbol() == ',':
            self._advance_and_write()  # ','
            self._advance_and_write()  # varName
        
        # ';'
        self._advance_and_write()
        
        self._write_tag('classVarDec', is_open=False)
    
    def compile_subroutine(self):
        """編譯subroutine"""
        # (constructor | function | method) void | type subroutineName '(' parameterList ')' subroutineBody
        self._write_tag('subroutineDec')
        
        # constructor | function | method
        self._advance_and_write()
        
        # void | type
        self._advance_and_write()
        
        # subroutineName
        self._advance_and_write()
        
        # '('
        self._advance_and_write()
        
        # parameterList
        self.compile_parameter_list()
        
        # ')'
        self._advance_and_write()
        
        # subroutineBody
        self.compile_subroutine_body()
        
        self._write_tag('subroutineDec', is_open=False)
    
    def compile_parameter_list(self):
        """編譯參數列表"""
        # ((type varName) (',' type varName)*)?
        self._write_tag('parameterList')
        
        # 檢查是否有參數
        if self.tokenizer.token_type() != 'symbol' or self.tokenizer.symbol() != ')':
            # type
            self._advance_and_write()
            
            # varName
            self._advance_and_write()
            
            # (',' type varName)*
            while self.tokenizer.has_more_tokens() and self.tokenizer.symbol() == ',':
                self._advance_and_write()  # ','
                self._advance_and_write()  # type
                self._advance_and_write()  # varName
        
        self._write_tag('parameterList', is_open=False)
    
    def compile_subroutine_body(self):
        """編譯subroutine體"""
        # '{' varDec* statements '}'
        self._write_tag('subroutineBody')
        
        # '{'
        self._advance_and_write()
        
        # varDec*
        while self.tokenizer.has_more_tokens() and self.tokenizer.token_type() == 'keyword':
            if self.tokenizer.keyword() == 'var':
                self.compile_var_dec()
            else:
                break
        
        # statements
        self.compile_statements()
        
        # '}'
        self._advance_and_write()
        
        self._write_tag('subroutineBody', is_open=False)
    
    def compile_var_dec(self):
        """編譯變量聲明"""
        # 'var' type varName (',' varName)* ';'
        self._write_tag('varDec')
        
        # 'var'
        self._advance_and_write()
        
        # type
        self._advance_and_write()
        
        # varName
        self._advance_and_write()
        
        # (',' varName)*
        while self.tokenizer.has_more_tokens() and self.tokenizer.symbol() == ',':
            self._advance_and_write()  # ','
            self._advance_and_write()  # varName
        
        # ';'
        self._advance_and_write()
        
        self._write_tag('varDec', is_open=False)
    
    def compile_statements(self):
        """編譯語句列表"""
        self._write_tag('statements')
        
        while self.tokenizer.has_more_tokens() and self.tokenizer.token_type() == 'keyword':
            keyword = self.tokenizer.keyword()
            
            if keyword == 'let':
                self.compile_let()
            elif keyword == 'if':
                self.compile_if()
            elif keyword == 'while':
                self.compile_while()
            elif keyword == 'do':
                self.compile_do()
            elif keyword == 'return':
                self.compile_return()
            else:
                break
        
        self._write_tag('statements', is_open=False)
    
    def compile_let(self):
        """編譯let語句"""
        # 'let' varName ('[' expression ']')? '=' expression ';'
        self._write_tag('letStatement')
        
        # 'let'
        self._advance_and_write()
        
        # varName
        self._advance_and_write()
        
        # ('[' expression ']')?
        if self.tokenizer.token_type() == 'symbol' and self.tokenizer.symbol() == '[':
            self._advance_and_write()  # '['
            self.compile_expression()  # expression
            self._advance_and_write()  # ']'
        
        # '='
        self._advance_and_write()
        
        # expression
        self.compile_expression()
        
        # ';'
        self._advance_and_write()
        
        self._write_tag('letStatement', is_open=False)
    
    def compile_if(self):
        """編譯if語句"""
        # 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
        self._write_tag('ifStatement')
        
        # 'if'
        self._advance_and_write()
        
        # '('
        self._advance_and_write()
        
        # expression
        self.compile_expression()
        
        # ')'
        self._advance_and_write()
        
        # '{'
        self._advance_and_write()
        
        # statements
        self.compile_statements()
        
        # '}'
        self._advance_and_write()
        
        # ('else' '{' statements '}')?
        if (self.tokenizer.has_more_tokens() and 
            self.tokenizer.token_type() == 'keyword' and 
            self.tokenizer.keyword() == 'else'):
            
            # 'else'
            self._advance_and_write()
            
            # '{'
            self._advance_and_write()
            
            # statements
            self.compile_statements()
            
            # '}'
            self._advance_and_write()
        
        self._write_tag('ifStatement', is_open=False)
    
    def compile_while(self):
        """編譯while語句"""
        # 'while' '(' expression ')' '{' statements '}'
        self._write_tag('whileStatement')
        
        # 'while'
        self._advance_and_write()
        
        # '('
        self._advance_and_write()
        
        # expression
        self.compile_expression()
        
        # ')'
        self._advance_and_write()
        
        # '{'
        self._advance_and_write()
        
        # statements
        self.compile_statements()
        
        # '}'
        self._advance_and_write()
        
        self._write_tag('whileStatement', is_open=False)
    
    def compile_do(self):
        """編譯do語句"""
        # 'do' subroutineCall ';'
        self._write_tag('doStatement')
        
        # 'do'
        self._advance_and_write()
        
        # subroutineCall
        self.compile_subroutine_call()
        
        # ';'
        self._advance_and_write()
        
        self._write_tag('doStatement', is_open=False)
    
    def compile_return(self):
        """編譯return語句"""
        # 'return' expression? ';'
        self._write_tag('returnStatement')
        
        # 'return'
        self._advance_and_write()
        
        # expression?
        if self.tokenizer.token_type() != 'symbol' or self.tokenizer.symbol() != ';':
            self.compile_expression()
        
        # ';'
        self._advance_and_write()
        
        self._write_tag('returnStatement', is_open=False)
    
    def compile_expression(self):
        """編譯表達式"""
        # term (op term)*
        self._write_tag('expression')
        
        # term
        self.compile_term()
        
        # (op term)*
        while self.tokenizer.has_more_tokens() and self.tokenizer.token_type() == 'symbol':
            symbol = self.tokenizer.symbol()
            # 檢查是否是運算符
            if symbol in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
                self._advance_and_write()  # op
                self.compile_term()  # term
            else:
                break
        
        self._write_tag('expression', is_open=False)
    
    def compile_term(self):
        """編譯項"""
        # integerConstant | stringConstant | keywordConstant | varName | 
        # varName '[' expression ']' | subroutineCall | '(' expression ')' | unaryOp term
        self._write_tag('term')
        
        token_type = self.tokenizer.token_type()
        
        if token_type == 'integerConstant':
            self._advance_and_write()
        
        elif token_type == 'stringConstant':
            self._advance_and_write()
        
        elif token_type == 'keyword':
            # keywordConstant: true, false, null, this
            self._advance_and_write()
        
        elif token_type == 'identifier':
            # 可能是varName, varName[expression], 或subroutineCall
            # 先保存標識符
            identifier = self.tokenizer.identifier()
            self._advance_and_write()
            
            # 檢查下一個符號
            next_token = self.tokenizer.peek_next_token()
            if next_token and next_token[0] == 'symbol':
                next_symbol = next_token[1]
                
                if next_symbol == '[':
                    # varName[expression]
                    self._advance_and_write()  # '['
                    self.compile_expression()  # expression
                    self._advance_and_write()  # ']'
                
                elif next_symbol in ['(', '.']:
                    # subroutineCall
                    # 回退一個token以便compile_subroutine_call能正確處理
                    self.tokenizer._index -= 1
                    self.tokenizer._current_token = (token_type, identifier)
                    self.compile_subroutine_call()
        
        elif token_type == 'symbol':
            symbol = self.tokenizer.symbol()
            
            if symbol == '(':
                # '(' expression ')'
                self._advance_and_write()  # '('
                self.compile_expression()  # expression
                self._advance_and_write()  # ')'
            
            elif symbol in ['-', '~']:
                # unaryOp term
                self._advance_and_write()  # unaryOp
                self.compile_term()  # term
        
        self._write_tag('term', is_open=False)
    
    def compile_subroutine_call(self):
        """編譯subroutine調用（輔助函數）"""
        # subroutineName '(' expressionList ')' | (className | varName) '.' subroutineName '(' expressionList ')'
        
        # 第一種情況：subroutineName或(className|varName)
        self._advance_and_write()
        
        if self.tokenizer.token_type() == 'symbol' and self.tokenizer.symbol() == '.':
            # (className | varName) '.' subroutineName '(' expressionList ')'
            self._advance_and_write()  # '.'
            self._advance_and_write()  # subroutineName
        
        # '('
        self._advance_and_write()
        
        # expressionList
        self.compile_expression_list()
        
        # ')'
        self._advance_and_write()
    
    def compile_expression_list(self):
        """編譯表達式列表"""
        # (expression (',' expression)*)?
        self._write_tag('expressionList')
        
        # 檢查是否有表達式
        if (self.tokenizer.token_type() != 'symbol' or 
            self.tokenizer.symbol() != ')'):
            
            # expression
            self.compile_expression()
            
            # (',' expression)*
            while self.tokenizer.has_more_tokens() and self.tokenizer.symbol() == ',':
                self._advance_and_write()  # ','
                self.compile_expression()  # expression
        
        self._write_tag('expressionList', is_open=False)
    
    def close(self):
        """關閉輸出文件"""
        self.output_file.close()