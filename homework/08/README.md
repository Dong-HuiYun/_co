# Hack VM 轉 ASM 轉譯器 (vm2asm)

這是一個完整的 Hack VM 語言到 Hack 組合語言的轉譯器，基於 Nand2Tetris 課程的虛擬機架構。該專案實現了完整的 VM 指令集支援，包括函數呼叫、記憶體管理和程式流程控制。

## 專案檔案結構

### 核心檔案
- **`vm2asm.c`** - 主要的轉譯器程式 (C 語言實作)
- **`build.sh`** - 編譯腳本
- **`vm2asm.sh`** - 單一檔案轉譯腳本
- **`all2asm.sh`** - 批次轉譯腳本（包含完整測試案例）

### 範例與測試檔案
- **`test1.asm`** - 簡單加法測試範例
- **`vm2asm.md`** - 開發記錄和 AI 協助記錄

## 快速開始

### 1. 編譯轉譯器
```bash
./build.sh
```
或手動編譯：
```bash
gcc -std=c99 vm2asm.c -o vm2asm
```

### 2. 基本使用方式

#### 單一 VM 檔案轉換
```bash
# 使用腳本（自動生成同名的 .asm 檔案）
./vm2asm.sh <檔案基底名稱>

# 範例：轉譯 SimpleAdd.vm 生成 SimpleAdd.asm
./vm2asm.sh StackArithmetic/SimpleAdd/SimpleAdd

# 或直接使用轉譯器
./vm2asm output.asm input.vm
```

#### 多檔案轉換（用於專案）
```bash
# 合併多個 VM 檔案為一個 ASM 檔案
./vm2asm Program.asm Main.vm Math.vm Screen.vm

# 複雜專案範例
./vm2asm FunctionCalls/StaticsTest/StaticsTest.asm \
          FunctionCalls/StaticsTest/Sys.vm \
          FunctionCalls/StaticsTest/Class1.vm \
          FunctionCalls/StaticsTest/Class2.vm
```

### 3. 執行完整測試套件
```bash
# 轉譯所有預設測試案例
./all2asm.sh
```

## 功能特色

### 完整支援的 VM 指令集

#### 算術與邏輯指令
- **基本運算**: `add`, `sub`, `neg`
- **比較運算**: `eq`, `gt`, `lt`（自動生成唯一標記）
- **邏輯運算**: `and`, `or`, `not`

#### 記憶體存取指令
- **push**: `push segment index`
- **pop**: `pop segment index`

#### 程式流程控制
- `label labelName`
- `goto labelName` 
- `if-goto labelName`

#### 函數呼叫系統
- `function functionName nVars`
- `call functionName nArgs`
- `return`

### 支援的記憶體段
- `constant` - 常數段（直接值）
- `local` - 區域變數段（LCL 基底）
- `argument` - 參數段（ARG 基底）
- `this`, `that` - 物件段
- `temp` - 臨時變數段（固定位置 R5-R12）
- `pointer` - 指標段（THIS, THAT）
- `static` - 靜態變數段（檔案作用域）

## 轉譯範例

### VM 輸入 (SimpleAdd.vm)
```vm
push constant 7
push constant 8
add
```

### 組合語言輸出 (SimpleAdd.asm)
```asm
// push constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
```

## 測試案例分類

### 基礎測試（透過 all2asm.sh 執行）

#### 記憶體存取測試
- `MemoryAccess/BasicTest/BasicTest` - 基礎記憶體操作
- `MemoryAccess/PointerTest/PointerTest` - 指標操作測試
- `MemoryAccess/StaticTest/StaticTest` - 靜態變數測試

#### 堆疊運算測試
- `StackArithmetic/SimpleAdd/SimpleAdd` - 簡單算術運算
- `StackArithmetic/StackTest/StackTest` - 完整堆疊操作

#### 程式流程測試
- `ProgramFlow/BasicLoop/BasicLoop` - 基礎迴圈控制
- `ProgramFlow/FibonacciSeries/FibonacciSeries` - 費波那契數列

#### 函數呼叫測試
- `FunctionCalls/SimpleFunction/SimpleFunction` - 簡單函數呼叫
- `FunctionCalls/NestedCall/NestedCall` - 嵌套函數呼叫
- `FunctionCalls/FibonacciElement/FibonacciElement` - 遞迴函數呼叫
- `FunctionCalls/StaticsTest/StaticsTest` - 靜態變數與多類別

## 進階功能

### 自動 Bootstrap 程式碼
當轉譯多個檔案時，自動生成系統初始化程式碼：
```asm
// Bootstrap code
// Initialize SP = 256
@256
D=A
@SP
M=D
// Call Sys.init
@Sys.init$ret.0
D=A
// ... 完整的函數呼叫框架
```

### 智慧標記處理
- **比較運算**: 自動生成唯一標記（`TRUE_X`, `END_X`）
- **函數返回**: 生成唯一返回標記（`function$ret.X`）
- **命名空間**: 避免標記名稱衝突

### 靜態變數命名空間
靜態變數使用檔案名稱作為命名空間，避免衝突：
```asm
@FileName.3  // 對應 static 3
```

## 技術架構

### 核心轉譯模組
```c
// 算術與邏輯運算
void write_arithmetic(FILE* out, const char* command);

// 記憶體存取
void write_push(FILE* out, const char* segment, int index);
void write_pop(FILE* out, const char* segment, int index);

// 函數呼叫框架
void write_function(FILE* out, const char* func_name, int num_locals);
void write_call(FILE* out, const char* func_name, int num_args);
void write_return(FILE* out);

// 程式流程控制
void write_label(FILE* out, const char* label);
void write_goto(FILE* out, const char* label);
void write_if_goto(FILE* out, const char* label);
```

### 記憶體管理策略
- **暫存器使用**: R13-R14 作為框架暫存器
- **堆疊管理**: 自動維護 SP（堆疊指標）
- **框架指標**: 正確處理 LCL、ARG、THIS、THAT

### 預處理功能
- 自動移除註解和空白行
- 支援 Windows/Unix 路徑格式
- 錯誤處理和警告訊息

## 完整工作流程

```bash
# 1. 編譯轉譯器
./build.sh

# 2. 轉譯 VM 程式（單檔案或多檔案）
./vm2asm.sh MyProgram
# 或
./vm2asm Program.asm Main.vm Library.vm

# 3. 組譯為機器碼（使用 asm 組譯器）
./asm MyProgram

# 4. 在虛擬機中執行
./vm MyProgram.bin

# 5. 除錯（可選，使用反組譯器）
./dasm MyProgram.bin
```

## 錯誤處理與驗證

- **檔案操作**: 檢查檔案開啟失敗
- **指令解析**: 處理不完整的指令參數
- **記憶體範圍**: 驗證記憶體段索引有效性
- **標記唯一性**: 確保生成的標記不會衝突

## 開發記錄

詳細的開發過程記錄在 `vm2asm.md` 中，包含：

- **Claude AI 協助**: [對話記錄](https://claude.ai/chat/e77a2397-45df-464b-95c1-12d133437b02)
- **Gemini AI 協助**: [對話記錄](https://gemini.google.com/app/a47e3bb767674dea)

## 相關工具鏈

這個轉譯器是 Hack 計算機完整工具鏈的關鍵組件：

- **`asm`** - Hack 組合語言組譯器
- **`vm`** - Hack 虛擬機執行器
- **`dasm`** - Hack 反組譯器
- **`vm2asm`** - VM 到 ASM 轉譯器（本專案）

## 擴展與貢獻

歡迎改進建議！潛在的改進方向：

- 程式碼優化（減少指令數量）
- 增強錯誤檢查和診斷訊息
- 支援更多的 VM 指令變體
- 效能分析和改進

## 授權與教育用途

此專案基於教育目的開發，遵循 Nand2Tetris 課程的學術使用規範，適合學習：
- 編譯器設計與實作
- 虛擬機架構
- 中間語言轉譯
- 計算機系統軟體開發

---

透過這個轉譯器，您可以將高階的堆疊式虛擬機程式轉換為底層的組合語言，完整體驗從高階抽象到底層實作的編譯過程。