當然可以！以下是一份**適合國小學生閱讀的 Python 筆記**，用簡單易懂的語言整理了你今天學到的內容：

---

## 🐍 Python 小學堂筆記

### ✅ 1. `if`、`elif`、`else` 是什麼？

在寫程式時，我們常常需要做判斷，比如：「如果今天下雨，就帶傘」，這時候就會用到 `if`。

```python
if 天氣 == "下雨":
    print("帶傘")
```

- `if`: 如果是對的，就執行。
- `elif`: 如果前面的不對，試試這個。
- `else`: 其他情況都做這個。

```python
if 分數 >= 90:
    print("A")
elif 分數 >= 80:
    print("B")
else:
    print("加油！")
```

🔍 **小提醒：**

- 用很多個 `if`，每一個都會檢查，速度慢。
- 用 `if` + `elif` + `else`，會一個一個檢查，有符合就不繼續了，速度比較快！

---

### 🔁 2. `for` 迴圈：重複做事情！

想像你要連續說 5 次「Hello」，可以這樣寫：

```python
for i in range(5):
    print("Hello")
```

- `range(5)` 會產生數字 0, 1, 2, 3, 4。
- `i` 是次數的變數，可以改名字沒關係。

你也可以設定從哪開始到哪結束：

```python
for i in range(1, 5):
    print(i)
```

這樣會印出：1、2、3、4（不包含 5 喔）

---

### 🧊 3. Streamlit 小工具

這是做網頁的小幫手！你可以用按鈕、輸入框、畫圖等等～

```python
import streamlit as st
st.button("按我一下")
```

- 按下按鈕時可以做一些特別的事情，比如放氣球或下雪：

```python
if st.button("放氣球"):
    st.balloons()
if st.button("下雪"):
    st.snow()
```

還可以做金字塔遊戲：

```python
num = st.number_input("輸入一個數字", min_value=1, max_value=9)
for i in range(1, num + 1):
    st.write(f"{i}" * i)
```

---

### 🧺 4. List 列表：裝東西的箱子

```python
水果 = ["蘋果", "香蕉", "葡萄"]
```

- 每個東西的位置叫「索引（index）」，從 0 開始。

```python
print(水果[0])  # 蘋果
print(水果[1])  # 香蕉
```

- 可以一次取好幾個：

```python
print(水果[0:2])  # 取第0到第1（不包含2）
```

- 算裡面有幾個東西用 `len()`：

```python
print(len(水果))  # 3
```

---

### 🧲 5. List 的使用小技巧

#### 🆕 加東西 `append()`

```python
水果.append("鳳梨")
```

#### ❌ 移除東西

- 移除特定內容（第一個找到的）：

```python
水果.remove("香蕉")
```

- 移除特定位置：

```python
水果.pop(0)  # 移除第0個
水果.pop()   # 移除最後一個
```

#### 🔢 排序

```python
數字 = [3, 1, 5, 2]
數字.sort()  # 排好順序：1, 2, 3, 5
```

---

### 📂 6. 開啟檔案

用 `open()` 把檔案打開來讀內容：

```python
f = open("檔案路徑", "r", encoding="utf-8")
內容 = f.read()
print(內容)
f.close()
```

用 `with` 更方便，會自動幫你關檔案：

```python
with open("檔案路徑", "r", encoding="utf-8") as f:
    內容 = f.read()
    print(內容)
```

---

### 🧠 7. 變數是怎麼傳的？

#### ✉️ 複製數值（Call by value）

```python
a = 1
b = a
b = 2
print(a, b)  # a還是1
```

#### 🔗 傳參考（Call by reference）

```python
a = [1, 2, 3]
b = a
b[0] = 9
print(a, b)  # a也會被改到
```

如果不想改到原本的：

```python
b = a.copy()
```

---

### 🔤 8. 字串結尾檢查 `.endswith()`

用來檢查檔案是不是某個類型的：

```python
檔名 = "notes.txt"
print(檔名.endswith(".md"))  # False
```

---

如果你有圖畫、玩具或糖果要整理，就可以想像 Python 的這些功能就像是幫你分類、找東西和重複做事的好幫手～
學會這些，你也能寫出自己的小遊戲或小工具囉！🎮🎨

---

如果你想要這份筆記轉成 PDF 或更好看的版本，也可以跟我說喔 😊
