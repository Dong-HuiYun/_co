# Project 8: Full-Scale VM Translator

這是我為 **Nand2Tetris** 課程（Project 8）實作的完整版虛擬機翻譯器（VM Translator）。此程式擴充了 Project 7 的基礎功能，加入了流程控制與函數調用的翻譯能力，並支援多檔案專案的編譯，作為編譯器的後端（Backend）使用。

## 📝 專案目標 (Objective)

本專案將建構一個全功能的 VM Translator，能夠將符合 VM 規範的程式碼翻譯成 Hack 組合語言。程式必須處理錯誤排除後的 VM 代碼，並支援跨檔案的函數調用與全域堆疊操作。

## ⚙️ 新增功能 (New Features)

在 Project 7 的算術與記憶體存取功能之上，本版本新增了以下功能：

### 1. 流程控制指令 (Branching Commands)
支援程式流程的跳轉與條件執行：
* `label label`
* `goto label`
* `if-goto label`

### 2. 函數調用指令 (Function Commands)
支援函數定義、調用與返回，並處理記憶體狀態的保存與恢復：
* `function functionName nVars`
* `call functionName nArgs`
* `return`

### 3. 多檔案與引導代碼 (Multi-file & Bootstrap)
* **多檔案支援**：可以接受一個「目錄」作為輸入，將該目錄下所有的 `.vm` 檔案合併編譯成單一的 `.asm` 檔案。
* **Bootstrap Code**：當輸入為目錄時，自動生成引導代碼（初始化 `SP=256` 並呼叫 `Sys.init`）。

## 🚀 如何執行 (Usage)

程式支援單一檔案或整個目錄的翻譯。

### 環境需求
* [填寫你的程式語言，例如：Python 3.8+ / Java 11]

### 執行指令

#### 翻譯整個目錄 (Generates Bootstrap Code)

python VMTranslator.py FibonacciElement

#### 執行BasicLoop.vm檔

```bash

python vm_translator.py test_vm/BasicLoop.vm

```

#### 執行FibonacciElement.vm檔

```bash

python vm_translator.py test_vm/FibonacciElement.vm

```
#### 執行FibonacciSeries.vm檔

```bash

python vm_translator.py test_vm/FibonacciSeries.vm

```

#### 執行SimpleFunction.vm檔

```bash

python vm_translator.py test_vm/SimpleFunction.vm

```

#### 執行Class1.vm檔

```bash

python vm_translator.py test_vm/StaticsTest/Class1.vm

```

## 參考資源

*   [nand2tetris](https://drive.google.com/file/d/1CITliwTJzq19ibBF5EeuNBZ3MJ01dKoI/view)
*   [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)