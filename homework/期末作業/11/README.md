# Project 11: Jack Compiler - Code Generation

## 項目概述

本項目是 Nand2Tetris 課程的 Project 11，目標是將 Project 10 構建的語法分析器（Syntax Analyzer）擴展為完整的 Jack 編譯器。編譯器將 Jack 源代碼（.jack 文件）編譯為可執行的 VM 代碼（.vm 文件）。

## 項目結構

```
11/
├── py/
│   ├── Compiler.py      # 主編譯器程序
│   ├── JackConstant.py  # Jack 語言常量定義
│   ├── Lex.py           # 詞法分析器
│   ├── Parser.py        # 語法分析器
│   ├── SymbolTable.py   # 符號表模塊
│   └── VMWriter.py      # VM 代碼生成器
│
└── jack/
    ├── Seven/           # 測試程序 1
    ├── ConvertToBin/    # 測試程序 2
    ├── Square/          # 測試程序 3
    ├── Average/         # 測試程序 4
    ├── Pong/            # 測試程序 5
    └── ComplexArrays/   # 測試程序 6
```

## 開發階段

### Stage 0: 備份
備份 Project 10 的語法分析器代碼。

### Stage 1: 符號表（Symbol Table）
構建 `SymbolTable` 模塊，擴展語法分析器以輸出每個標識符的信息：
- **name**: 標識符名稱
- **category**: field, static, local, arg, class, subroutine
- **index**: 運行索引（適用於 field, static, local, arg）
- **usage**: 聲明（declared）或使用（used）

### Stage 1.5: 備份
備份擴展後的語法分析器代碼。

### Stage 2: 代碼生成（Code Generation）
逐步將 XML 輸出替換為可執行的 VM 代碼生成。

## 測試程序

按照以下順序測試編譯器，每個程序測試不同的語言特性：

### 1. Seven（最簡單）
- **測試內容**: 整數常量的算術表達式、do 語句、return 語句
- **預期行為**: 計算 `1 + (3 * 2)` 並在屏幕左上角顯示 `7`
- **文件數量**: 1 個 .jack → 1 個 .vm

### 2. ConvertToBin
- **測試內容**: 函數、表達式（不含數組或方法調用）、if/while/do/let/return 語句
- **不測試**: methods, constructors, arrays, strings, static/field 變量
- **測試步驟**:
  1. 在 RAM[8000] 輸入十進制數（如 137）
  2. 運行幾秒後停止
  3. 檢查 RAM[8001] 到 RAM[8016] 是否包含正確的二進制位（0 或 1）
  4. 確認沒有 -1 殘留
- **文件數量**: 1 個 .jack → 1 個 .vm

### 3. Square
- **測試內容**: 構造函數（constructors）、方法（methods）、字段（fields）、包含方法調用的表達式
- **不測試**: static 變量
- **預期行為**: 
  - 使用方向鍵移動黑色方塊
  - 按 `z` 和 `x` 鍵放大/縮小方塊
  - 按 `q` 退出遊戲
- **測試設置**: 選擇 "no animation" 模式
- **文件數量**: 3 個 .jack → 3 個 .vm

### 4. Average
- **測試內容**: 數組（arrays）、字符串（strings）
- **預期行為**: 計算用戶輸入的整數序列的平均值
- **測試步驟**: 按照屏幕提示輸入數字，驗證平均值計算正確
- **文件數量**: 1 個 .jack → 1 個 .vm

### 5. Pong
- **測試內容**: 完整的面向對象應用、對象處理、靜態變量（static variables）
- **預期行為**: 經典 Pong 遊戲
  - 球隨機移動並從"牆壁"反彈
  - 用左右方向鍵移動擋板
  - 擊球得分，擋板縮小
  - 球落地則遊戲結束
- **測試重點**: 確認得分正確顯示
- **測試設置**: 選擇 "no animation" 模式
- **文件數量**: 4 個 .jack → 4 個 .vm

### 6. ComplexArrays
- **測試內容**: 複雜的數組引用和表達式
- **預期行為**: 執行 5 個複雜計算，每個計算顯示預期結果（Expected）和實際結果（Actual）
- **測試步驟**: 確認所有預期值和實際值完全相同
- **文件數量**: 1 個 .jack → 1 個 .vm

## 測試流程

對於每個測試程序，執行以下步驟：

### 1. 編譯程序
```bash
cd 11/py/
python Compiler.py ../jack/Seven/
```

這將為文件夾中的每個 `.jack` 文件生成對應的 `.vm` 文件。

### 2. 檢查生成的 VM 代碼
```bash
# 查看生成的 VM 文件
cat ../jack/Seven/Main.vm
```

檢查項目：
- 是否有明顯的語法錯誤
- push/pop 指令是否合理
- 函數調用格式是否正確

### 3. 準備 Jack OS 庫文件
將 Jack 操作系統的 `.vm` 文件複製到測試文件夾：

```bash
# 從 Nand2Tetris tools/OS/ 目錄複製
cp [nand2tetris_path]/tools/OS/*.vm jack/Seven/
```

所需的 OS 文件：
- Array.vm
- Keyboard.vm
- Math.vm
- Memory.vm
- Output.vm
- Screen.vm
- String.vm
- Sys.vm

### 4. 使用 VM Emulator 運行
1. 打開 **VM Emulator**（Nand2Tetris 提供）
2. Load Program → 選擇包含 `.vm` 文件的文件夾
3. 根據程序的具體測試要求運行
4. 驗證行為是否符合預期

### 5. 調試
如果出現問題：
- VM Emulator 報錯 → 修復代碼生成邏輯
- 行為不符預期 → 檢查編譯器實現
- 返回步驟 1 重新編譯


## 所需工具

- **編程語言**: 用於實現編譯器（本項目使用 Python）
- **VM Emulator**: Nand2Tetris 提供的虛擬機模擬器，用於測試生成的 VM 代碼
- **Jack OS 庫**: 標準庫的 .vm 文件（Array, Keyboard, Math, Memory, Output, Screen, String, Sys）

## 編譯規則

- 每個 `.jack` 源文件生成一個對應的 `.vm` 文件
- 文件名保持不變，只改變擴展名：
  - `Main.jack` → `Main.vm`
  - `Square.jack` → `Square.vm`


## 參考資料

- [Nand2Tetris](https://www.nand2tetris.org/course)
- [claude對話網址](https://claude.ai/share/93f63c42-8a08-42c0-8c6c-cd05fa61b75f)