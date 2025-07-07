"""
這是多行註解
這邊可以放很多的文字
"""

# 這是單行註解
print("hello world")  # print是在終端機顯示文字的指令
# ctr1+?可以快速註解或取消註解

# 基本型態
print(1)  # int這是整數,-1,0,2,3,4,5,6,7,8,9
print(1.0)  # float這是浮
print(1.2340)  # float這是浮點數
print("apple")  # str這是字串"saddasd123125557
print(True)  # bool 這是布林值 True或false
print(False)  # bool 這是布林值 True或false

# 變數
a = 10  # 新增一儲存存空間並取名為a,"="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為"apple"
print(a)  # 在終端機顯示a所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取整除法
print(1 % 1)  # 取餘數
print(1**1)  # 次方
# 優先順序
# 1.()括號
# 2.**次方
# 3.*/ // %  乘 除 取商 取榆數
# 4.+ - 加 減

# 練習
a = "hello"
b = "world"
print(a + "" + b)


# 字串
s = "apple"  # 字串
s1 = "apple" + "banana"  # 字串連接
s2 = "apple" * 3  # 字串重複
s3 = "apple"[0]  # 字串的第一個字

# 字串格式化
name = "apple"
age = 10
print(f"Hello,my name is {name},  my age is {age} years old ")
