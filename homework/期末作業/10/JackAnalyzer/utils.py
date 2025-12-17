# utils.py
import os

# 導入 JackTokenizer
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine

def compare_files_ignore_whitespace(file1, file2):
    """比較兩個文件，忽略空白字符"""
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            # 移除空白字符
            content1_no_ws = ''.join(content1.split())
            content2_no_ws = ''.join(content2.split())
            
            return content1_no_ws == content2_no_ws
    except FileNotFoundError:
        return False

def test_tokenizer():
    """測試tokenizer"""
    # 使用正確的相對路徑
    test_files = [
        "../test/Square/Main.jack",
        "../test/Square/Square.jack", 
        "../test/Square/SquareGame.jack"
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\n測試: {test_file}")
            
            try:
                tokenizer = JackTokenizer(test_file)
                
                output_file = test_file.replace('.jack', 'T.xml')
                tokenizer.write_xml(output_file)
                
                print(f"生成的token文件: {output_file}")
                
                # 檢查文件是否成功創建
                if os.path.exists(output_file):
                    print(f"文件大小: {os.path.getsize(output_file)} bytes")
                    
                    # 顯示前幾行
                    with open(output_file, 'r') as f:
                        print("前5行內容:")
                        for i, line in enumerate(f):
                            if i < 5:
                                print(f"  {line.rstrip()}")
                            else:
                                break
                else:
                    print("警告: 輸出文件未創建")
                    
            except Exception as e:
                print(f"錯誤: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"警告: 文件 {test_file} 不存在")
            print(f"完整路徑: {os.path.abspath(test_file)}")

def test_parser():
    """測試parser"""
    test_dirs = [
        "../test/ExpressionlessSquare",
        "../test/Square",
        "../test/ArrayTest"
    ]
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            print(f"\n測試目錄: {test_dir}")
            
            # 查找所有.jack文件
            for root, dirs, files in os.walk(test_dir):
                for file in files:
                    if file.endswith('.jack'):
                        jack_file = os.path.join(root, file)
                        print(f"\n處理文件: {jack_file}")
                        
                        try:
                            # 創建tokenizer
                            tokenizer = JackTokenizer(jack_file)
                            
                            # 創建compilation engine
                            output_file = jack_file.replace('.jack', '.xml')
                            engine = CompilationEngine(tokenizer, output_file)
                            
                            # 編譯整個class
                            engine.compile_class()
                            engine.close()
                            
                            print(f"生成的XML文件: {output_file}")
                            
                            if os.path.exists(output_file):
                                print(f"文件大小: {os.path.getsize(output_file)} bytes")
                                
                        except Exception as e:
                            print(f"錯誤: {e}")
        else:
            print(f"警告: 目錄 {test_dir} 不存在")