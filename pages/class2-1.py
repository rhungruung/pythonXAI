print(len("hello world"))  # len()函數,可以計算字串的長度
print(len("."))  # len()函數,可以計算字串的長度
# tybe() #可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))  # <calss 'bool'>

# 型態轉換
print(int(1.0))  # float型態轉換成int型態
print(float(1))  # int型態轉換成float型態
print(str(1))  # int型態轉換成str型態
print(bool(1))  # int型態轉換成bool型態
print(int("1234"))  # str型態轉換成int型態
print(float("1.234"))  # str型態轉換成float型態
print(str(1.234))  # float型態轉換成str型態
print(bool("1.234"))  # str型態轉換成bool型態
# print(int("hello"))  # 這行會抱錯，因為字串裡面如果有非數字的字元，無法轉換成數字

# input ()函式的使用
print("輸入開始")
# input()是一個函式，可以讓使用者輸入文字
# ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一些文字：")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都是字串

r = float(input("請輸入一個數字："))
pi = 3.14
area = pi * r * r
print(f"圓的面積是: {area}")
