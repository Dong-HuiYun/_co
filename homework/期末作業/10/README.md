# Jack Syntax Analyzer

## 專案簡介

這是一個針對 Jack 語言的語法分析器（Syntax Analyzer），作為 Nand2Tetris 課程 Project 10 的實作。該分析器能夠解析 Jack 程式碼並輸出 XML 格式的語法結構。

Jack 是一種類似 Java 的物件導向高階程式語言，本專案實作的語法分析器能夠：
- 將 Jack 原始碼進行詞法分析（Tokenization）
- 進行語法解析（Parsing）
- 輸出符合 Jack 語法規則的 XML 結構

## 專案結構

```
10/
├── JackAnalyzer/
│   ├── main.py                 # 主程式入口
│   ├── jackTokenizer.py        # 詞法分析器
│   ├── CompilationEngine.py    # 編譯引擎（語法分析）
│   └── utils.py                # 工具函數
│
└── test/
    ├── Square/                 # Square 程式測試檔案
    │   ├── Main.jack
    │   ├── Square.jack
    │   └── SquareGame.jack
    ├── ExpressionlessSquare/   # 簡化表達式的測試檔案
    │   ├── Main.jack
    │   ├── Square.jack
    │   └── SquareGame.jack
    └── ArrayTest/              # 陣列處理測試檔案
        └── Main.jack
```

## 功能特性

### 1. 詞法分析（Tokenizer）
- 識別 Jack 語言的五種 token 類型：
  - `keyword`: 關鍵字（class, method, function, let, if 等）
  - `symbol`: 符號（{, }, (, ), [, ], ., ,, ; 等）
  - `integerConstant`: 整數常數
  - `stringConstant`: 字串常數
  - `identifier`: 識別符（變數名、類別名等）

### 2. 語法分析（Parser）
- 完整支援 Jack 語法結構：
  - 類別定義（class）
  - 類別變數宣告（static, field）
  - 子程式宣告（constructor, function, method）
  - 參數列表
  - 變數宣告
  - 敘述（let, if, while, do, return）
  - 表達式（包含運算子優先順序）
  - 陣列操作

### 3. XML 輸出
- 生成結構化的 XML 檔案，反映程式碼的語法樹
- 自動處理 XML 特殊字元轉義：
  - `<` → `&lt;`
  - `>` → `&gt;`
  - `"` → `&quot;`
  - `&` → `&amp;`

## 系統需求

- Python 3.6 或以上版本
- 作業系統：Windows / macOS / Linux

## 安裝與設定

```bash
# 1. Clone 或下載專案
git clone <repository-url>

# 2. 進入專案目錄
cd 10

# 3. 確認 Python 版本
python --version
```

不需要安裝額外的套件，只使用 Python 標準函式庫。

## 使用方式

### 基本語法

```bash
python JackAnalyzer/main.py <source>
```

其中 `<source>` 可以是：
- 單一 `.jack` 檔案
- 包含多個 `.jack` 檔案的資料夾

### 使用範例

#### 1. 分析單一檔案

```bash
python JackAnalyzer/main.py test/Square/Main.jack
```

這會生成 `test/Square/Main.xml`

#### 2. 分析整個資料夾

```bash
python JackAnalyzer/main.py test/Square
```

這會處理 `Square` 資料夾中所有的 `.jack` 檔案，生成對應的 `.xml` 檔案：
- `Main.xml`
- `Square.xml`
- `SquareGame.xml`

#### 3. Windows 系統路徑

```bash
# 使用反斜線
python JackAnalyzer\main.py test\Square

# 或使用正斜線
python JackAnalyzer/main.py test/Square
```

## 測試流程

### 階段一：測試 Tokenizer

首先測試詞法分析是否正確：

```bash
python JackAnalyzer/main.py test/Square/Main.jack
```

檢查生成的 XML 檔案，確認 token 類型和內容是否正確。

### 階段二：測試 Parser（不含表達式）

使用簡化的測試檔案：

```bash
python JackAnalyzer/main.py test/ExpressionlessSquare
```

這些檔案中的表達式都被替換為單一變數，用來測試基本的語法結構。

### 階段三：完整測試

```bash
# 測試完整的 Square 程式
python JackAnalyzer/main.py test/Square

# 測試陣列處理
python JackAnalyzer/main.py test/ArrayTest
```

### 批次測試

```bash
# 測試所有資料夾
python JackAnalyzer/main.py test/Square
python JackAnalyzer/main.py test/ExpressionlessSquare
python JackAnalyzer/main.py test/ArrayTest
```

## 驗證結果

### 方法一：使用瀏覽器檢視

在瀏覽器中開啟生成的 XML 檔案：

```bash
# Windows
start test/Square/Main.xml

# macOS
open test/Square/Main.xml

# Linux
xdg-open test/Square/Main.xml
```

瀏覽器會以樹狀結構顯示 XML，方便檢查語法結構。

### 方法二：文字比較

使用文字比較工具比對生成的檔案與標準答案：

```bash
# 使用 diff（忽略空白字元）
diff -w test/Square/Main.xml test/Square/MainExpected.xml

# 使用 TextComparer（課程提供的工具）
TextComparer test/Square/Main.xml test/Square/MainExpected.xml
```

### 方法三：檢查清單

確認輸出檔案符合以下要求：

- ✅ XML 格式正確，可在瀏覽器中開啟
- ✅ 特殊字元正確轉義（`< > " &`）
- ✅ 字串常數不包含引號
- ✅ 空標籤格式正確（開閉標籤之間有換行）
- ✅ 語法結構與預期相符

## 輸出範例

### 輸入（Jack 程式碼）

```jack
class Main {
    function void main() {
        var int x;
        let x = 10;
        return;
    }
}
```

### 輸出（XML）

```xml
<class>
  <keyword> class </keyword>
  <identifier> Main </identifier>
  <symbol> { </symbol>
  <subroutineDec>
    <keyword> function </keyword>
    <keyword> void </keyword>
    <identifier> main </identifier>
    <symbol> ( </symbol>
    <parameterList>
    </parameterList>
    <symbol> ) </symbol>
    <subroutineBody>
      <symbol> { </symbol>
      <varDec>
        <keyword> var </keyword>
        <keyword> int </keyword>
        <identifier> x </identifier>
        <symbol> ; </symbol>
      </varDec>
      <statements>
        <letStatement>
          <keyword> let </keyword>
          <identifier> x </identifier>
          <symbol> = </symbol>
          <expression>
            <term>
              <integerConstant> 10 </integerConstant>
            </term>
          </expression>
          <symbol> ; </symbol>
        </letStatement>
        <returnStatement>
          <keyword> return </keyword>
          <symbol> ; </symbol>
        </returnStatement>
      </statements>
      <symbol> } </symbol>
    </subroutineBody>
  </subroutineDec>
  <symbol> } </symbol>
</class>
```

## 常見問題

### Q1: 找不到檔案或資料夾

**問題**：`錯誤: 路徑 test/ArrayTest 不存在`

**解決方案**：
- 檢查路徑拼寫是否正確
- Windows 使用反斜線 `\` 或正斜線 `/`
- 確認當前工作目錄在專案根目錄

### Q2: XML 檔案無法在瀏覽器中開啟

**問題**：瀏覽器顯示解析錯誤

**解決方案**：
- 檢查特殊字元是否正確轉義
- 確認所有標籤都有對應的閉合標籤
- 檢查是否有非法的 XML 字元

### Q3: 輸出與預期不符

**問題**：生成的 XML 與標準答案不同

**解決方案**：
- 使用 `diff -w` 忽略空白差異
- 檢查語法解析邏輯
- 確認 token 類型判斷正確

### Q4: 無法處理某些 Jack 程式碼

**問題**：程式執行時出現錯誤

**解決方案**：
- 確認輸入的 Jack 程式碼語法正確
- 檢查是否處理了所有的 Jack 語法元素
- 查看錯誤訊息並除錯

## 技術細節

### Jack 語言特性

- **關鍵字**：class, constructor, function, method, field, static, var, int, char, boolean, void, true, false, null, this, let, do, if, else, while, return
- **符號**：`{ } ( ) [ ] . , ; + - * / & | < > = ~`
- **整數範圍**：0 ~ 32767
- **字串**：使用雙引號包圍，不包含換行符

### XML 輸出規則

1. 所有 token 必須包含在對應的標籤中
2. 縮排使用兩個空格（可選，但建議使用）
3. 空標籤必須分行：
   ```xml
   <parameterList>
   </parameterList>
   ```
4. 不允許自閉合標籤（`<tag />`）

## 專案限制

- 本專案假設輸入的 Jack 程式碼**語法正確**
- 不進行錯誤檢查和錯誤處理
- 不執行程式碼，僅進行語法分析
- 註解和多餘空白會被移除

## 後續發展

本專案是編譯器開發的第一階段（語法分析）。在 Project 11 中，將擴展為完整的編譯器：

- 生成 VM 程式碼而非 XML
- 實作符號表（Symbol Table）
- 處理變數作用域
- 生成可執行的 VM 指令

## 參考資料

- [Nand2Tetris 官方網站](https://www.nand2tetris.org/)
- Jack 語言規格說明
- Project 10 規格文件
- [deepseek對話網址](https://chat.deepseek.com/share/3lz0950zcjfrmywdnx)
- [claude對話網址](https://claude.ai/share/8d86d7d1-b8f0-444a-a45a-d65876d7c466)