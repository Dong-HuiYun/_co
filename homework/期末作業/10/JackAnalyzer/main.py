import os
import sys
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine

class JackAnalyzer:
    def __init__(self):
        pass
    
    def analyze_file(self, input_path, output_path=None):
        """分析單個.jack文件"""
        if not input_path.endswith('.jack'):
            print(f"錯誤: 文件 {input_path} 必須以 .jack 結尾")
            return
        
        if output_path is None:
            output_path = input_path.replace('.jack', '.xml')
        
        print(f"分析文件: {input_path} -> {output_path}")
        
        try:
            # 創建tokenizer
            tokenizer = JackTokenizer(input_path)
            
            # 可選：生成token輸出（用於調試）
            token_output = input_path.replace('.jack', 'T.xml')
            tokenizer.write_xml(token_output)
            
            # 創建compilation engine
            engine = CompilationEngine(tokenizer, output_path)
            
            # 編譯整個class
            engine.compile_class()
            
            # 關閉文件
            engine.close()
            
            print(f"分析完成: {output_path}")
            
        except Exception as e:
            print(f"分析文件 {input_path} 時出錯: {e}")
    
    def analyze_directory(self, directory_path):
        """分析目錄中的所有.jack文件"""
        print(f"分析目錄: {directory_path}")
        
        # 獲取所有.jack文件
        jack_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.jack'):
                    jack_files.append(os.path.join(root, file))
        
        if not jack_files:
            print(f"警告: 目錄 {directory_path} 中沒有找到 .jack 文件")
            return
        
        print(f"找到 {len(jack_files)} 個 .jack 文件")
        
        # 分析每個文件
        for jack_file in jack_files:
            self.analyze_file(jack_file)
    
    def run(self):
        """主運行函數"""
        if len(sys.argv) != 2:
            print("用法: python main.py <source>")
            print("  <source> 可以是 .jack 文件或包含 .jack 文件的目錄")
            sys.exit(1)
        
        source = sys.argv[1]
        
        # 檢查路徑是否存在
        if not os.path.exists(source):
            print(f"錯誤: 路徑 {source} 不存在")
            sys.exit(1)
        
        # 判斷是文件還是目錄
        if os.path.isfile(source):
            self.analyze_file(source)
        elif os.path.isdir(source):
            self.analyze_directory(source)
        else:
            print(f"錯誤: {source} 不是有效的文件或目錄")
            sys.exit(1)

if __name__ == "__main__":
    analyzer = JackAnalyzer()
    analyzer.run()