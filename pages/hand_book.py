import streamlit as st

with st.expander("Class1課程筆記"):
    st.write(
        '''


# 🐍 Python 程式設計入門筆記

### 🔤 什麼是註解？

註解就像是程式裡的小筆記，不會被電腦執行，可以讓人看得懂程式在做什麼。

- `#`：單行註解（只註解一行）
- `""" 內容 """`：多行註解（可以寫好幾行）

### 🖨️ 顯示文字的方法

```python
print("hello world")
```

用 `print()` 指令可以把文字或數字顯示在畫面上。

---

## 🔢 Python 的基本資料種類（型態）

| 種類             | 範例            | 說明               |
| ---------------- | --------------- | ------------------ |
| 整數 (`int`)     | `1`, `0`, `-5`  | 沒有小數點的數字   |
| 浮點數 (`float`) | `1.0`, `3.14`   | 有小數點的數字     |
| 字串 (`str`)     | `"apple"`       | 用引號包住的文字   |
| 布林值 (`bool`)  | `True`, `False` | 代表「對」或「錯」 |

---

## 📦 變數是什麼？

變數就像是一個可以放東西的小盒子，我們可以幫它取名字！

```python
a = 10       # 把數字10放進a
print(a)     # 顯示a裡面的東西（結果是10）

a = "apple"  # 把文字"apple"放進a，蓋掉原本的10
print(a)     # 顯示a裡的東西（結果是apple）
```

---

## ➕ 運算子（也就是算數符號）

| 符號 | 用法     | 說明                    |
| ---- | -------- | ----------------------- |
| `+`  | `1 + 1`  | 加法                    |
| `-`  | `2 - 1`  | 減法                    |
| `*`  | `2 * 3`  | 乘法                    |
| `/`  | `4 / 2`  | 除法（有小數）          |
| `//` | `5 // 2` | 整除（只取整數部分）    |
| `%`  | `5 % 2`  | 餘數                    |
| `**` | `2 ** 3` | 次方（2 的 3 次方 = 8） |

🔢 運算優先順序（誰先算）：

1. `()` 括號先算
2. `**` 次方
3. `*`, `/`, `//`, `%` 接著算
4. `+`, `-` 最後算

---

## 🧪 小練習

```python
a = "hello"
b = "world"
print(a + " " + b)  # 把兩個字串合起來，中間加空格
```

---

## ✨ 字串的玩法（文字的用法）

```python
s = "apple"
s1 = "apple" + "banana"   # 合併兩個字串 → applebanana
s2 = "apple" * 3          # 重複字串 → appleappleapple
s3 = "apple"[0]           # 取出字串的第一個字母 → a
```

---

## 🧩 字串格式化（變數放進字串中）

```python
name = "apple"
age = 10
print(f"Hello, my name is {name}, my age is {age} years old.")
```

這樣就可以把變數 `name` 和 `age` 放進句子裡，超方便！

'''
    )


with st.expander("Class2課程筆記"):
    st.write(
        '''
# 🐍 Python 初學筆記（給小學生看的版本）

## 1️⃣ 字串的長度 - `len()`

`len()` 可以用來算出文字有幾個字：

```python
print(len("hello world"))  # 有 11 個字
print(len("."))  # 只有 1 個字
```

---

## 2️⃣ 看變數是什麼種類 - `type()`

我們可以用 `type()` 來看東西是「數字」、「文字」，還是「對或錯」的布林值：

```python
print(type(1))       # 整數 int
print(type(1.0))     # 小數 float
print(type("hello")) # 字串 str
print(type(True))    # 布林值 bool（True 或 False）
```

---

## 3️⃣ 資料型態轉換

有時候我們需要把一種型態的資料換成另一種：

```python
print(int(1.0))       # 小數 變 整數
print(float(1))       # 整數 變 小數
print(str(1))         # 整數 變 字串
print(bool(1))        # 整數 變 True 或 False
print(int("1234"))    # 字串 變 整數
print(float("1.234")) # 字串 變 小數
print(str(1.234))     # 小數 變 字串
print(bool("1.234"))  # 字串 變 True
```

⚠️ 如果字串裡面不是數字，像是 `"hello"`，就不能轉換成數字，會出錯！

---

## 4️⃣ 使用者輸入 - `input()`

`input()` 可以請使用者輸入東西：

```python
a = input("請輸入一些文字：")
print(int(a) + 10)  # 輸入的內容會是字串，要記得轉成數字才能算數學
```

算圓面積的小練習：

```python
r = float(input("請輸入一個數字："))
pi = 3.14
area = pi * r * r
print(f"圓的面積是: {area}")
```

---

## 5️⃣ Streamlit 的使用（做出網頁）

用 Streamlit 我們可以做出網頁，把結果秀出來：

```python
import streamlit as st

st.title("這是標題")
st.write("這是可以顯示各種資料的區塊")
st.text("這裡只能顯示純文字")
```

### Markdown 顯示

Markdown 可以讓文字有特別的格式：

````python
st.markdown("""
* **粗體**
* *斜體*
* [連結](https://www.example.com)
* 程式碼：
```python
print("Hello, Streamlit!")
````

""")

````

### 顯示不同訊息：
```python
st.info("這是資訊訊息")
st.success("這是成功的訊息")
st.warning("這是警告")
st.error("這是錯誤")
````

---

## 6️⃣ 比較運算子（用來比大小）

```python
print(1 == 1)  # 一樣嗎？True
print(1 != 1)  # 不一樣嗎？False
print(1 > 1)   # 大於？False
print(1 < 1)   # 小於？False
print(1 >= 1)  # 大於或等於？True
print(1 <= 1)  # 小於或等於？True
```

---

## 7️⃣ 邏輯運算子（多個條件一起判斷）

### and（而且）

只要有一個是 False，結果就是 False：

```python
print(True and False)  # False
```

### or（或者）

只要有一個是 True，結果就是 True：

```python
print(True or False)  # True
```

### not（反過來）

把 True 變 False，False 變 True：

```python
print(not True)   # False
print(not False)  # True
```

---

## 8️⃣ 運算的優先順序（誰先算）

運算順序是：

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* / // %`
4. 加減 `+ -`
5. 比較 `== != > < >= <=`
6. not
7. and
8. or

---

## 9️⃣ 密碼門（if 判斷）

用 `if` 來判斷密碼，來決定要說什麼：

```python
password = input("請輸入密碼:")
if password == "12345":
    print("你好歡迎回家")
elif password == "1234":
    print("english or spanish")
elif password == "123":
    print("I am gay!")
else:
    print("You are gay!")
```

> ⚠️ 小提醒：寫程式時要用有禮貌的語句喔！

---

## 🔟 分數評分小工具（Streamlit + if 判斷）

```python
score = st.number_input(label="請輸入你的分數", step=1, min_value=0, max_value=100)

if score >= 90:
    st.write("A")
elif score >= 80:
    st.write("B")
elif score >= 70:
    st.write("C")
elif score >= 60:
    st.write("D")
else:
    st.write("F")
```

---

這樣的筆記希望你能看得懂、學得快！如果想要，我也可以幫你畫出圖示來記憶。要不要一起做一份圖像版筆記呢？🎨📘
'''
    )
