# 🐍 貪食蛇遊戲 (Snake Game)

**Nand2Tetris Project 9 - Jack 語言實作**

這是一個使用 Jack 語言開發的經典貪食蛇遊戲，包含完整的遊戲機制、計分系統、暫停功能和無限重玩功能。

---

## 📁 專案結構

```
SnakeGame/
├── Main.jack           # 程式入口點
├── SnakeGame.jack      # 遊戲主邏輯與遊戲迴圈
├── Snake.jack          # 蛇的類別（移動、碰撞、生長）
├── Food.jack           # 食物類別（隨機生成）
└── README.md           # 本文件
```

---

## 🎮 遊戲功能

### 核心功能
- ✅ 流暢的蛇移動控制
- ✅ 食物隨機生成
- ✅ 碰撞檢測（牆壁、自身）
- ✅ 計分系統（每個食物 +10 分）
- ✅ 動態難度（分數越高速度越快）
- ✅ 暫停/繼續功能
- ✅ 無限重玩（遊戲結束後可重新開始）

### 遊戲畫面
- 邊框包圍的遊戲區域
- 實時顯示分數
- 清晰的開始畫面說明
- Game Over 提示畫面

---

## 🎯 遊戲操作

### 開始遊戲
1. 執行程式後會看到開始畫面
2. 按 **空白鍵 (Space)** 開始遊戲

### 遊戲中控制
| 按鍵 | 功能 |
|------|------|
| ⬆️ 上箭頭 | 向上移動 |
| ⬇️ 下箭頭 | 向下移動 |
| ⬅️ 左箭頭 | 向左移動 |
| ➡️ 右箭頭 | 向右移動 |
| **P** | 暫停/繼續遊戲 |

### 遊戲結束後
- 按 **R 鍵** 返回開始畫面
- 再按 **空白鍵** 重新開始

### 遊戲規則
- 🍎 吃到食物：蛇變長 +1，得分 +10
- 💥 碰到牆壁：遊戲結束
- 💥 咬到自己：遊戲結束
- ⚡ 分數 > 50：遊戲加速
- ⚡ 分數 > 100：遊戲更快

---

## 📚 程式碼說明

### 1. Main.jack - 程式入口點

```jack
class Main {
    function void main() {
        var SnakeGame game;
        let game = SnakeGame.new();
        do game.run();
        do game.dispose();
        return;
    }
}
```

**功能**：
- 建立遊戲實例
- 啟動遊戲主迴圈
- 程式結束時釋放記憶體

**說明**：這是整個程式的起點，類似 Java 的 `main()` 方法。

---

### 2. SnakeGame.jack - 遊戲主邏輯

#### 主要成員變數
```jack
field Snake snake;      // 蛇物件
field Food food;        // 食物物件
field int score;        // 分數
field boolean gameOver; // 遊戲是否結束
field int delay;        // 遊戲速度（毫秒）
```

#### 核心方法

**`constructor new()`**
- 初始化遊戲物件
- 設定初始分數和速度
- 建立蛇和食物實例

**`method run()`** - 遊戲主迴圈
```
無限迴圈 {
    顯示開始畫面
    ↓
    等待空白鍵
    ↓
    遊戲進行迴圈 {
        處理鍵盤輸入
        移動蛇
        檢測碰撞
        更新畫面
    }
    ↓
    顯示 Game Over
    ↓
    等待 R 鍵重新開始
}
```

**重要機制**：
- **碰撞檢測**：每次移動後檢查是否撞牆或撞自己
- **食物檢測**：判斷蛇頭是否與食物重疊
- **暫停功能**：使用 `paused` 變數控制遊戲暫停
- **動態速度**：根據分數調整 `delay` 值

**輔助方法**：
- `drawBorder()`：繪製遊戲邊界
- `displayScore()`：顯示分數資訊
- `showInstructions()`：顯示開始畫面說明
- `showGameOver()`：顯示遊戲結束畫面
- `showPaused()`：顯示暫停提示
- `resetGame()`：重置遊戲狀態

---

### 3. Snake.jack - 蛇的類別

#### 資料結構
```jack
field Array bodyX, bodyY;  // 蛇身體各節的座標陣列
field int length;          // 當前蛇的長度
field int direction;       // 移動方向 (1=上, 2=下, 3=左, 4=右)
field int size;           // 每節身體的大小（像素）
field boolean growing;    // 是否正在生長
```

#### 核心方法

**`constructor new()`**
- 初始化蛇在螢幕中央
- 設定初始長度為 3 節
- 預設向右移動

**`method move()`** - 移動邏輯
```
計算新的頭部位置
↓
如果不在生長 {
    把每節身體往前移一格（陣列位移）
}
如果正在生長 {
    增加 length
    把每節身體往前移一格
    重置 growing 標記
}
↓
設定新頭部座標
```

**`method setDirection(newDir)`**
- 防止 180 度轉向（避免蛇直接咬到自己）
- 例如：向右移動時不能直接轉向左

**`method draw()`**
- 遍歷所有身體節點
- 使用 `Screen.drawRectangle()` 繪製每一節

**碰撞檢測方法**：
- `hitWall()`：檢查頭部是否超出邊界
- `hitSelf()`：檢查頭部是否與身體其他節重疊
- `eatFood(food)`：檢查頭部是否接觸到食物

**`method grow()`**
- 設定 `growing = true`
- 下次移動時會增加長度而不是移除尾巴

---

### 4. Food.jack - 食物類別

#### 資料結構
```jack
field int x, y;     // 食物座標
field int size;     // 食物大小
field int seed;     // 隨機數種子
```

#### 核心方法

**`method random(max)`** - 偽隨機數生成器
```jack
seed = (seed * 75) + 74;  // 線性同餘生成器
if (seed < 0) {
    seed = -seed;
}
return (seed - ((seed / max) * max));  // 取模運算
```

**說明**：Jack 語言沒有內建隨機函數，因此使用簡單的數學演算法生成偽隨機數。

**`method respawn()`** - 重新生成食物
```
生成隨機格子座標 (避開邊界)
↓
轉換為像素座標
↓
更新 seed 以增加隨機性
```

**`method draw()`** - 繪製食物
- 外層：繪製實心方塊
- 內層：繪製較小的空心，讓食物看起來像一個框

**座標轉換**：
- 使用格子系統（每格 8 像素）
- 轉換公式：`像素座標 = 格子座標 × 8`

---

## 🛠️ 編譯與執行

### 前置需求
1. 下載並安裝 [Nand2Tetris Software Suite](https://www.nand2tetris.org/software)
2. 確保已解壓縮並知道 `nand2tetris/tools` 資料夾的位置

### 編譯步驟

#### Windows (PowerShell)

```powershell
# 切換到 tools 目錄
cd C:\Users\dongh\Desktop\nand2tetris\nand2tetris\tools
.\JackCompiler.bat C:\Users\dongh\Desktop\大二上計算機結構\_co\homework\9\SnakeGame
```


### 執行步驟

1. **開啟 VM Emulator**
   
2. **載入程式**
   - 點擊 `File` → `Load Program`
   - 選擇 `SnakeGame` **資料夾**（不是單一檔案）
   - 確認資料夾中包含 4 個 `.vm` 檔案

3. **設定執行模式**
   - `Animate`: 選擇 `No Animation`
   - `View`: 選擇 `Screen`
   - 速度滑桿拉到 `Fast`

4. **執行遊戲**
   - 點擊 `Run` 按鈕（▶▶）
   - 或按 `F5` 快捷鍵

5. **使用內建 OS**
   - 首次執行會詢問是否使用內建 OS
   - **選擇「是(Y)」**

### 編譯成功確認
編譯成功後，`SnakeGame` 資料夾應包含：
```
SnakeGame/
├── Main.jack
├── Main.vm          ← 編譯產生
├── SnakeGame.jack
├── SnakeGame.vm     ← 編譯產生
├── Snake.jack
├── Snake.vm         ← 編譯產生
├── Food.jack
└── Food.vm          ← 編譯產生
```

---

## 🎨 程式設計重點

### 1. 物件導向設計
- **分離關注點**：每個類別負責單一職責
- **封裝性**：內部實作細節不外露
- **可維護性**：修改一個類別不影響其他類別

### 2. 遊戲迴圈架構
```
輸入處理 → 更新遊戲狀態 → 繪製畫面 → 延遲 → 重複
```

### 3. 碰撞檢測演算法
- **邊界檢測**：比較座標與邊界值
- **自身碰撞**：遍歷身體陣列比對座標
- **食物檢測**：使用距離判斷（允許誤差範圍）

### 4. 隨機數生成
使用線性同餘生成器（LCG）：
```
X(n+1) = (a × X(n) + c) mod m
```

### 5. 陣列操作
- **位移操作**：實現蛇的移動
- **動態長度**：支援蛇的生長

---

## 🐛 已知問題與限制

### 限制
1. **隨機性有限**：偽隨機數生成器可能產生規律
2. **最大長度**：蛇最長 200 節（受陣列大小限制）
3. **速度下限**：delay < 50ms 可能造成控制困難
4. **食物可能生成在蛇身上**：未實作避開蛇身的檢測

### 可能的改進
- 改進隨機數演算法
- 食物生成時檢測是否與蛇重疊
- 加入音效（需要 Jack OS 音效支援）
- 加入高分紀錄系統
- 多種難度選擇

## 參考資料

- [Nand2Tetris 官方網站](https://www.nand2tetris.org/)
- Jack 語言規格說明
- Project 9 規格文件
- [claude對話網址](https://claude.ai/share/9da17a61-2a0d-4aee-831f-409c9c56de1e)
