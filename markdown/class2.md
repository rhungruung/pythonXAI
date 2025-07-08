# 🐍 Python 初學筆記

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
