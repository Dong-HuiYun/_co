# 期末作業（第6-12章習題）

## 著作狀態聲明

**原創與參考來源說明：**

- 第6-11章習題：全部由AI生成（DeepSeek/Gemini/Claude）
- 第12章習題：參考 GitHub 專案以及老師的版本進行理解
- AI 輔助使用：
[gemini對話網址](https://gemini.google.com/share/2ed098a7f9fc)

## 各章節內容報告

### 第6章：Assembler (組譯器)

**作業連結：**[第六章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/6)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 知道這個專案是要開發一個組譯器，Hack組合語言（符號式機器語言）翻譯成Hack二進位碼。程式能夠讀取 .asm 檔案並在終端機輸入指令：

```bash

# python assembler.py [檔名.asm]
python assembler.py Add.asm

```

輸出對應 .hack 檔案。

2. 知道如何驗證程式碼是否正確：使用 CPU Emulator 執行產生的二進位碼，測試Add（加法）、Max（求最大值）、Rect（繪製矩形）以及 Pong（桌球遊戲）的輸出與正確答案是否相同。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/xllgp004g7q23k98zc)


### 第7章：VM Translator (Part 1)

**作業連結：**[第七章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/7)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 知道這個專案是要開發一個 虛擬機翻譯器（VM Translator） 的基礎版本，將 VM 代碼翻譯成 Hack 組合語言，因爲只是基礎版本，因此僅需實作 VM 語言中的算術邏輯指令（如 add, sub, eq 等）以及 push/pop 指令。翻譯器讀取 VM 指令（例如 push constant 7），並產生對應的 Hack 組合語言序列，以便在 Hack 電腦的 RAM 上執行堆疊操作。

2. 知道如何驗證程式碼是否正確：使用範例的.vm檔，並在終端機上輸入指令（例如：python vm_translator.py test_vm/SimpleAdd.vm），生成.asm檔，比對是否和範例的輸出相同。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/y1apljhkrd0y2h7g2t)

### 第8章：VM Translator (Part 2)

**作業連結：**[第八章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/8)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 第八章將第七章的基礎虛擬機翻譯器進行完善，使其能處理 程式流程控制（Branching） 與 函式呼叫（Function commands） 指令。并且能將包含多個 .vm 檔案的資料夾翻譯成單一 .asm 組語檔案

2. 流程分爲兩階段：處理分支指令、處理函式與多檔案

- 第一階段：處理分支指令 

    BasicLoop：測試基本循環邏輯 。

    FibonacciSeries：測試分支指令的綜合運用 。


- 第二階段：處理函式與多檔案 

    SimpleFunction：測試基礎的 function 與 return 操作 。

    FibonacciElement：測試遞迴函式呼叫、多檔案整合以及引導代碼（Bootstrap code）的生成 。

    StaticsTest：專門測試在多檔案環境下，不同類別（檔案）間靜態變數（static variables）的處理 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)

### 第9章：Jack 程式設計

**作業連結：**[第九章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/9)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 檔案結構
    Main.jack - 遊戲入口點
    SnakeGame.jack - 遊戲主邏輯（遊戲迴圈、碰撞檢測、計分）
    Snake.jack - 蛇的類別（移動、生長、碰撞檢測）
    Food.jack - 食物類別（隨機生成位置）
    
2. 遊戲功能

    按空白鍵 開始遊戲
    方向鍵控制蛇的移動（上下左右）
    吃食物後蛇會變長並加分
    碰到牆壁或自己會遊戲結束
    計分系統（每個食物 +10 分）
    隨著分數增加遊戲速度加快
    開始畫面和遊戲結束畫面
    按 P 鍵：暫停遊戲
    再按一次 P 鍵：繼續遊戲
    按 Q 鍵：退出遊戲

**AI對話網址：**

- [claude對話網址](https://claude.ai/share/9da17a61-2a0d-4aee-831f-409c9c56de1e)

### 第10章：語法分析器

**作業連結：**[第十章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/10)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 建立一個能解析 Jack 程式語法結構的工具，並將其輸出為 XML 格式，以便驗證解析的正確性

2. 語法分析器的組成

- JackTokenizer (標記解析器)：

    負責將原始碼（.jack 檔案）拆解成一個個獨立的「標記」(Tokens) 。
    過濾掉所有的註解與空白字元 。
    標記類型包括：關鍵字 (keyword)、符號 (symbol)、識別碼 (identifier)、整數常數 (integerConstant) 與字串常數 (stringConstant) 。

- CompilationEngine (編譯引擎)：

    從標記流中讀取內容，並根據 Jack 語法規則進行遞迴解析 。
    輸出反映程式結構的階層式 XML 標籤 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/3lz0950zcjfrmywdnx)

- [claude對話網址](https://claude.ai/share/8d86d7d1-b8f0-444a-a45a-d65876d7c466)

### 第11章：代碼產生器

**作業連結：**[第十一章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/11)

**習題完成狀態：** 老師提供的程式碼

**理解程度：** 少部分理解

1. 原本語法分析器產生的 passive XML 輸出，將被替換為可執行的 VM 指令序列 。

2. 測試

- 編譯程序

```bash

cd 11/py/
python Compiler.py ../jack/Seven/

```
為文件夾中的每個 `.jack` 文件生成對應的 `.vm` 文件。

- 檢查生成的 VM 代碼

```bash

cat ../jack/Seven/Main.vm

```
- 準備 Jack OS 庫文件

將 Jack 操作系統的 `.vm` 文件複製到測試文件夾：

```bash

cp [nand2tetris_path]/tools/OS/*.vm jack/Seven/

```

**參考網址：**

- [老師提供的程式碼網址](https://github.com/ccc114a/cpu2os/tree/master/_nand2tetris/11)


### 第12章：作業系統

**作業連結：**[第十二章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E6%9C%AB%E4%BD%9C%E6%A5%AD/12)

**學習狀態：** 僅閱讀理解老師的範例

**理解程度：** 少部分理解

- 使用 Jack 語言實作 8 個核心類別（Class），每個類別負責不同的系統服務 ：

    1. Math.jack：處理數學運算（如乘除法、平方根等） 。

    2. String.jack：處理字串處理與轉換 。

    3. Array.jack：管理陣列的建立 。

    4. Memory.jack：負責記憶體管理（分配與釋放，如 alloc 和 deAlloc） 。

    5. Screen.jack：負責繪圖功能（如繪製直線、矩形、圓形） 。

    6. Output.jack：處理文字輸出與螢幕字元顯示 。

    7. Keyboard.jack：處理鍵盤輸入與讀取按鍵訊息 。

    8. Sys.jack：系統服務（如程式初始化 init、暫停執行 wait 以及終止程式 halt） 。

**參考網址：**

- [老師提供的程式碼網址](https://github.com/ccc114a/cpu2os/tree/master/_nand2tetris/12)
