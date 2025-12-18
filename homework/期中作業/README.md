# 期中作業（第1-5章習題）

## 著作狀態聲明

**原創與參考來源說明：**

- 第1章習題：原創（多工器後面的部分有在網路上找它的圖片，看是由哪些邏輯閘所組成的）
- 第2：部分原創+部分ai（詢問ai該如何設計，程式部分自己嘗試）
- 第3-5章習題：由AI生成
- AI 輔助使用：
[gemini對話網址](https://gemini.google.com/share/8745a8f7bffc)

## 各章節內容報告

### 第1章：Elementary Logic Gates（基礎邏輯閘）

**作業連結：**[第一章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD/1)

**習題完成狀態：** 原創（多工器後面的部分有在網路上找它的圖片，看是由哪些邏輯閘所組成的）

**理解程度：** 大部分理解

- 使用到的邏輯閘

    基礎邏輯閘：Not, And, Or, Xor, Mux, DMux 。


    16 位元版本：Not16, And16, Or16, Mux16 。

    多路/多位元邏輯閘：Or8Way, Mux4Way16, Mux8Way16, DMux4Way, DMux8Way 。

- 測試

    在HardwareSimulator上進行測試


### 第2章：Boolean Arithmetic（布林運算）

**作業連結：**[第二章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD/2)

**習題完成狀態：** 部分原創+部分ai（詢問ai該如何設計，程式部分自己嘗試）

**理解程度：** 部分原創+部分ai（詢問ai該如何設計，程式部分自己嘗試）

- 使用到的邏輯閘

    HalfAdder（半加器）

    FullAdder（全加器）

    Add16（16 位元加法器）

    Inc16（16 位元增量器）

    ALU（算術邏輯單元）：CPU 的運算核心 。

- ALU 實作階段

    基礎階段：先實作計算 out 的功能，忽略 zr 和 ng 。

    最終階段：在基礎版本上加入 zr 和 ng 的邏輯 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)

### 第3章：Memory

**作業連結：**[第三章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD/3)

**習題完成狀態：** AI生成

**理解程度：** 部分理解

- 目標

    建構電腦的主記憶體（RAM），這是一個由可定址暫存器組成的序列，每個暫存器用來儲存 n 位元的值 。

- 基礎元件：

    DFF (Data Flip-Flop)：這是原始元件（Primitive），官方直接提供，不需要自行實作 。

    Bit：1 位元儲存單元 。

    Register：16 位元暫存器 。

- RAM ：

    包含 RAM8、RAM64、RAM512、RAM4K、RAM16K，規模逐漸擴大 。

- 控制元件：

    PC (Program Counter)：程式計數器，用於追蹤下一條指令的位址 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)

### 第4章：Machine Language（機器語言）

**作業連結：**[第四章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD/4)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

- 目標

    動手建構電腦硬體（Project 5）與組譯器（Project 6）之前，先熟悉 Hack 指令集與低階編程 。

- 工具

    組譯器 (Assembler)：將符號式的 .asm 原始碼轉換成電腦可執行的 .hack 二進位代碼 。

    CPU 模擬器 (CPU Emulator)：以軟體模擬方式執行二進位代碼，可即時查看暫存器、記憶體與程式計數器（PC）的狀態，並支援螢幕顯示與鍵盤輸入 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)

### 第5章：Computer

**作業連結：**[第五章](https://github.com/Dong-HuiYun/_co/tree/main/homework/%E6%9C%9F%E4%B8%AD%E4%BD%9C%E6%A5%AD/5)

**習題完成狀態：** AI生成

**理解程度：** 少部分理解

- 實作目標

    Memory（記憶體）：將 RAM16K、螢幕（Screen）和鍵盤（Keyboard）整合進一個 32K 的定址空間中 。

    CPU（中央處理單元）：使用 Project 2 的 ALU、Project 3 的暫存器與程式計數器（PC），以及 Project 1 的邏輯閘來構建 。


    Computer（電腦頂層晶片）：這是最高層級的晶片，由 CPU、Memory 和指令記憶體（ROM32K）組成 。

**AI對話網址：**

- [deepseek對話網址](https://chat.deepseek.com/share/m54iatez0yxczupw5q)

