# 第6-12章習題與學習報告

## 著作狀態聲明

**原創與參考來源說明：**

- 第6-11章習題：全部由AI生成（ChatGPT/DeepSeek/Gemini/Claude）
- 第12章學習：參考 GitHub 專案以及老師的版本進行理解
- AI 輔助使用：
[gemini對話網址]()

## 各章節內容報告

### 第6章：Assembler (組譯器)

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

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 知道這個專案是要開發一個 虛擬機翻譯器（VM Translator） 的基礎版本，將 VM 代碼翻譯成 Hack 組合語言，因爲只是基礎版本，因此僅需實作 VM 語言中的算術邏輯指令（如 add, sub, eq 等）以及 push/pop 指令。翻譯器讀取 VM 指令（例如 push constant 7），並產生對應的 Hack 組合語言序列，以便在 Hack 電腦的 RAM 上執行堆疊操作。

2. 知道如何驗證程式碼是否正確：使用範例的.vm檔，並在終端機上輸入指令（例如：python vm_translator.py test_vm/SimpleAdd.vm），生成.asm檔，比對是否和範例的輸出相同。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/y1apljhkrd0y2h7g2t)

### 第8章：VM Translator (Part 2)

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

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

1. 檔案結構
    Main.jack - 遊戲入口點
    SnakeGame.jack - 遊戲主邏輯（遊戲迴圈、碰撞檢測、計分）
    Snake.jack - 蛇的類別（移動、生長、碰撞檢測）
    Food.jack - 食物類別（隨機生成位置）
    
**AI對話網址：**

- [claude對話網址](https://claude.ai/share/9da17a61-2a0d-4aee-831f-409c9c56de1e)

### 第10章：搜尋演算法
**習題完成狀態：** AI生成
**AI 使用記錄：**
- 使用 ChatGPT 釐清「二元搜尋樹 vs 雜湊表」的應用場景
- 對話網址：`https://chat.openai.com/share/xxx`（附完整對話截圖）
- AI 建議經理解後改寫為自己的實作
**AI對話網址：**

- [deepseek對話網址]()

### 第11章：動態規劃
**習題完成狀態：** AI生成
**具體說明：**
- 11.1-11.5：原創
- 11.6題：修改自 GitHub 專案 `user/repo` 的解法
- 修改內容：將遞迴版本改為迭代版本，並優化空間複雜度
- 11.8題：看不懂，用 AI 也無法理解（放棄該題）

**AI對話網址：**

- [deepseek對話網址]()

### 第12章：進階主題
**學習狀態：** 僅閱讀理解，未實作習題
**參考來源：**
- 完全參考 GitHub 專案 `[專案名稱]` 的解答版本
- 閱讀並理解以下主題：
  1. 貪心演算法
  2. NP 完全問題概念
  3. 近似演算法
- **未實作原因：** 依照指示僅需看懂解答版本

## 各題詳細標註

### 第6章
- 6.1-6.10：原創

### 第7章
- 7.1-7.11：原創

### 第8章
- 8.1-8.11：原創
- 8.12：修改（來源：geeksforgeeks.org）

### 第9章
- 9.1-9.9：原創

### 第10章
- 10.1-10.6：原創
- 10.7：AI 輔助原創（經理解後改寫）

### 第11章
- 11.1-11.5：原創
- 11.6：修改（來源：GitHub 專案）
- 11.7：原創
- 11.8：未完成（看不懂）

### 第12章
- 全部題目：僅閱讀參考解答，未實作

## 整體學習心得
1. **掌握程度：** 第6-10章完全掌握，第11章部分理解
2. **困難點：** 動態規劃的狀態轉移方程式設計較難
3. **AI 輔助效果：** 有助於釐清概念，但無法直接給出作業答案
4. **原創比例：** 約 90% 為原創或經理解後改寫

## 附錄：AI 對話記錄
### ChatGPT 對話（10.7題輔助）