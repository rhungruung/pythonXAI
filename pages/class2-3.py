# 比較運算子
print(1 == 1)  # Ture
print(1 != 1)  # Ture
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True

# 邏輯運算子
# # and 運算子 ,只要有一個條件為Fales，結果就是Fales
# print(True and True)#True
# print(True and False)#False
# print(False and True)#False
# print(False and False)#False
# # or 運算子 ,只要有一個條件為True，結果就是True

# or 運算子,只要有一個條件為True，結果就是True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1.()括號
# 2.**次方
# 3.*/ // %  乘 除 取商 取榆數
# 4.+ - 加 減
# 5.==!=><>=<=比較運算子
# 6.not
# 7.and
# 8.or

# 密碼門檢查
passsword = input("請輸入密碼:")
if passsword == "12345":
    print("你好歡迎回家")
elif passsword == "1234":
    print("english or spanish")
elif passsword == "123":
    print("I am gay!")
else:  # 沒有達成上面條件的其他情況就會執行以下容
    print("You are gay!")
