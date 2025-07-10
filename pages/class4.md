## 🐍 今天的 Python 學習筆記

### 🖥️ 用 Streamlit 做畫面設計

#### 1️⃣ 建立標題

```python
st.title("我是標題")
```

👆 這會在畫面上顯示一個大標題。

---

#### 2️⃣ 做出左右兩邊的欄位（像分左右兩格）

```python
col1, col2 = st.columns(2)
```

👈 `col1` 是左邊，`col2` 是右邊。我們可以在兩邊放不同的東西，例如按鈕：

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

---

#### 3️⃣ 可以用比例決定欄位寬度

```python
col1, col2 = st.columns([1, 2])
```

意思是：左邊寬度 1，右邊寬度是 2。

---

#### 4️⃣ 也可以用 `with col1:` 的方式寫

這樣寫可以讓程式更整齊：

```python
with col1:
    st.button("我是按鈕")
```

---

#### 5️⃣ 做出很多欄位（像 4 格並排）

```python
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

---

#### 6️⃣ 做出很多列，每列兩格

```python
for i in range(3):  # 做3列
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}")
    with col2:
        st.write(f"這是第{i+1}列的右邊")
```

---

### 📝 文字輸入

```python
text = st.text_input("請輸入名字", value="這是預設文字")
st.write(f"你輸入的是:{text}")
```

🔤 這可以讓使用者輸入文字！

---

### 🔁 記住變數的值（session_state）

🔸 普通變數不能記得按鈕按幾次，但 `session_state` 可以！

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("按一下+1"):
    st.session_state.ans += 1

st.write(f"目前的數字是: {st.session_state.ans}")
```

🔁 `st.rerun()` 可以用來重新整理畫面。

---

### 🍔 做一個簡單的點餐機！

```python
if "order" not in st.session_state:
    st.session_state.order = []

food = st.text_input("輸入餐點名稱")
if st.button("加入"):
    st.session_state.order.append(food)
```

🔄 顯示購物車＋刪除功能：

```python
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("刪除", key=i):
            st.session_state.order.pop(i)
            st.rerun()
```

---

## ➕ 算數運算子（讓變數自己加自己）

| 寫法      | 意思                  |
| --------- | --------------------- |
| `a += 1`  | a = a + 1             |
| `a -= 1`  | a = a - 1             |
| `a *= 2`  | a = a × 2             |
| `a /= 2`  | a = a ÷ 2             |
| `a %= 2`  | a = a 除以 2 後的餘數 |
| `a **= 2` | a 的平方              |

---

## 🔢 計算的順序（誰先做？）

1. `()` 先算括號
2. `**` 次方
3. `* / // %` 乘除
4. `+ -` 加減
5. 比大小 `== > < >= <=`
6. `not`
7. `and`
8. `or`
9. 最後是指定像 `= += *=`

---

## 🔁 while 迴圈（重複做事情）

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

🔸 如果你想要中斷：

```python
if 某個條件:
    break  # 跳出迴圈
```

---

## 🎲 隨機 random 模組

```python
import random
```

### ✅ 抽一個隨機數

```python
random.randint(1, 6)  # 1到6
```

---

### 🔢 猜數字遊戲範例

```python
ans = random.randint(1, 100)
while True:
    num = int(input("猜一個 1 到 100 的數字: "))
    if num > ans:
        print("太大了")
    elif num < ans:
        print("太小了")
    else:
        print("猜對了！")
        break
```

---

## 📕 字典 Dictionary（像資料寶箱）

### ✅ 建立字典

```python
d = {"蘋果": 20, "香蕉": 30}
```

### ✅ 取出資料

```python
print(d["蘋果"])  # 顯示 20
```

### ✅ 加入或修改資料

```python
d["蘋果"] = 15  # 修改
d["西瓜"] = 40  # 新增
```

### ✅ 刪除資料

```python
d.pop("蘋果")
```

### ✅ 走訪字典

```python
for k, v in d.items():
    print(f"{k}:{v}")
```
