# Project 12

## 專案概述

這個專案要求學生實作一個完整的作業系統（Jack OS），這是整個「從 NAND 到俄羅斯方塊」課程的頂點項目。

### 專案目標
- 實作在課程中講述的作業系統
- 使用 Jack 高階語言編寫 OS 核心功能
- 為前面專案建立的硬體和軟體堆疊提供系統服務

## 作業系統架構

Jack OS 由 8 個類別檔案組成，每個類別提供特定的系統服務：

### 8 個 OS 類別檔案
1. **Math.jack** - 數學運算庫
2. **String.jack** - 字串處理
3. **Array.jack** - 陣列操作
4. **Memory.jack** - 記憶體管理（分配/釋放）
5. **Screen.jack** - 螢幕繪圖
6. **Output.jack** - 文字輸出
7. **Keyboard.jack** - 鍵盤輸入
8. **Sys.jack** - 系統初始化與基本服務

## 測試策略

專案採用獨特的 **漸進式測試** 方法：

### VM 模擬器的內建 OS 功能
- VM 模擬器內建了完整 OS 的實現
- 當程式呼叫 OS 函數時：
  - 如果學生已實作該函數 → 使用學生的版本
  - 如果未實作 → 使用模擬器的內建版本
- 這讓學生可以 **單獨測試每個 OS 模組**，無需等待其他模組完成

### 單元測試資料夾結構
```
projects/12/
├── MathTest/          # Math.jack 的測試
├── MemoryTest/        # Memory.jack 的測試
├── StringTest/        # String.jack 的測試
├── ArrayTest/         # Array.jack 的測試
├── ScreenTest/        # Screen.jack 的測試
├── OutputTest/        # Output.jack 的測試
├── KeyboardTest/      # Keyboard.jack 的測試
└── SysTest/           # Sys.jack 的測試
```

## 測試流程

### 針對每個 OS 類別的測試步驟：
1. **檢查測試程式**：了解測試內容和方式
2. **放入實作檔案**：將你的 Xxx.jack 放入對應的 XxxTest 資料夾
3. **編譯整個資料夾**：使用 Jack 編譯器編譯所有 .jack 檔案
4. **載入到 VM 模擬器**：載入測試腳本或整個資料夾
5. **執行測試**：按照各類別的特定指南進行測試

## 各 OS 類別的測試重點

### Math、Array、Memory 類別
- 包含完整的測試腳本 (.tst) 和預期輸出 (.cmp)
- 使用 VM 模擬器的自動測試功能
- Memory.alloc/deAlloc 需要額外的除錯測試（觀察 RAM 內部狀態）

### String 類別
測試輸出應包含：
- 字串操作：appendChar、setInt、length 等
- 字元操作：charAt、setCharAt
- 數值轉換：intValue

### Screen 類別
- 測試螢幕繪圖功能
- 檢查圖形輸出是否正確

### Output 類別
- 測試文字輸出功能
- 驗證顯示內容的正確性

### Keyboard 類別
- **互動式測試**：要求使用者按下特定按鍵
- 測試功能：
  - keyPressed() - 檢查是否有按鍵按下
  - readChar() - 讀取單一字元
  - readLine() - 讀取一行文字
  - readInt() - 讀取整數
- 所有測試通過後顯示 "Test ended successfully"

### Sys 類別
- 測試 Sys.wait() 函數：驗證等待時間是否正確（約 2 秒）
- Sys.init() 間接測試：所有測試程式都依賴它進行初始化

## 整合測試：Pong 遊戲

### 最終測試
- 使用之前專案的 Pong 遊戲進行完整整合測試
- 步驟：
  1. 將 8 個 OS .jack 檔案放入 projects/11/Pong 資料夾
  2. 編譯整個資料夾
  3. 載入到 VM 模擬器執行
  4. 驗證遊戲正常運行

### 優雅降級機制
- 如果某些 OS 函數未實作，VM 模擬器會使用內建版本
- 允許學生逐步完成 OS，無需一次實作所有功能

## 教學意義

這個專案完整實現了 **計算機系統的軟體堆疊**：

```
應用程式層（第11專案：高階語言程式）
      ↓
作業系統層（第12專案：Jack OS）
      ↓
虛擬機器層（第7-8專案：VM 翻譯器）
      ↓
組合語言層（第4專案：機器語言）
      ↓
硬體層（第5專案：Hack 電腦）
      ↓
邏輯閘層（第1-3專案：基本元件）
```

## 關鍵概念

1. **系統抽象**：OS 作為硬體與軟體之間的橋樑
2. **服務模組化**：將系統功能分解為獨立但協作的模組
3. **漸進式開發**：利用內建 OS 實現進行測試驅動開發
4. **完整的堆疊**：從 NAND 閘到完整作業系統的完整實現

## 參考資料

- [Nand2Tetris](https://www.nand2tetris.org/course)
- [claude對話網址](https://chat.deepseek.com/share/zdwxl4pyhwyvq9kuyd)