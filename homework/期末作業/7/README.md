# Project 7: VM Translator (Basic)

這是為 **Nand2Tetris** 課程（Project 7）實作的虛擬機翻譯器（VM Translator）。此程式作為編譯器的後端（Backend），負責將堆疊式虛擬機代碼（VM Code）翻譯成 Hack 組合語言（Assembly Code）。

## 📝 專案目標 (Objective)

本專案的目標是建構一個基礎的 VM Translator，能夠處理算術邏輯運算以及記憶體堆疊存取指令。程式會讀取 `.vm` 檔案，並產生符合 Hack 平台標準映射的 `.asm` 檔案。

## ⚙️ 功能特性 (Features)

本實作支援以下 VM 指令與記憶體區段：

### 1. 算術與邏輯指令 (Arithmetic & Logical Commands)
支援所有標準的堆疊運算指令：
* `add`, `sub`, `neg`
* `eq`, `gt`, `lt`
* `and`, `or`, `not`

### 2. 記憶體存取指令 (Memory Access Commands)
支援 `push` 與 `pop` 指令，並處理以下虛擬記憶體區段 (Memory Segments) [cite: 118, 120, 121]：
* `constant`
* `local`, `argument`, `this`, `that`
* `temp`
* `pointer` (0/1)
* `static`

## 🛠️ 開發環境與執行 (Usage)

### 環境需求
* Python

### 執行指令

創建測試檔文件夾test_vm，建立測試檔`SimpleAdd.vm`、`BasicTest.vm`、`PointerTest.vm`、`StaticTest.vm`，輸出為同名的 `.asm` 檔案。

#### SimpleAdd.vm ：測試 VM 翻譯器是否正確工作
1. 建立測試檔`SimpleAdd.vm`
2. 在終端機上輸入指令

```bash
python vm_translator.py test_vm/SimpleAdd.vm
```
3. 輸出 `SimpleAdd.asm` 檔案


#### BasicTest.vm ：測試各種堆疊操作
1. 建立測試檔`BasicTest.vm`
2. 在終端機上輸入指令
```bash
python vm_translator.py test_vm/BasicTest.vm
```
3. 輸出 `BasicTest.asm` 檔案

#### PointerTest.vm - 測試 pointer segment
1. 建立測試檔`PointerTest.vm`
2. 在終端機上輸入指令
```bash
python vm_translator.py test_vm/PointerTest.vm
```
3. 輸出 `PointerTest.asm` 檔案

#### StaticTest.vm - 測試 static segment
1. 建立測試檔`StaticTest.vm`
2. 在終端機上輸入指令
```bash
python vm_translator.py test_vm/StaticTest.vm
```
3. 輸出 `StaticTest.asm` 檔案

## 參考資源

*   [nand2tetris](https://drive.google.com/file/d/1CITliwTJzq19ibBF5EeuNBZ3MJ01dKoI/view)
*   [deepseek對話網址](https://chat.deepseek.com/share/y1apljhkrd0y2h7g2t)