# 算術指定運算子
a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
a %= 2  # a = a % 2
print(a)  # 0
a %= 2  # a = a % 2
print(a)  # 0.0
a **= 2  # a = a ** 2
print(a)  # 0.0

# 優先順序
# 1.()括號
# 2.**次方
# 3.*/ // %  乘 除 取商 取榆數
# 4.+ - 加 減
# 5. == !=> < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **=算術指定運算子

# while 迴圈
# while 會搭配一個條件是來使用
# 條件式為 True 時會一直執行迴圈
# 條件式為 False時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成 False
i = 0
while i < 5:
    print(i)
    i += 1  # i = i + 1

    # break 可以強制跳出迴圈
    # 先判斷break屬於哪個迴圈,然後跳出迴圈
    i = 0
    while i < 5:
        print(i)
        for j in range(5):
            print(j)
        if j == 3:
            break  # 跳出迴圈, 屬於while迴圈
        i += 1

for i in range(5):
    print(i)
    if i == 3:
        break  # 跳出迴圈
import random  # 匯入random模主

# random.randrange()設定抽籤範圍的方式跟range()一樣
print(random.randrange(7))  # 0到6
print(random.randrange(1, 2))  # 1到6
print(random.randrange(1, 7, 2))  # 1到6, 隔間2

# random.choice()設定抽籤範圍的放是一定要設地開始與結束
且結束的數字會包含在內
print(random.randint(1, 6))  # 1到6


ans = random.randint(1, 100)  # 隨機產生 1 到 100 的整數
while True:  # 無窮迴圈
    num = int(input(f"請輸入1 到 100 的整數:"))

    if num < 0 or num > 100:  # 如果輸入超出範圍
        print("請輸入1到100的整數")
    elif num > ans:  # 如果輸入的數字大於答案
        print("太大了！")
    elif num < ans:  # 如果輸入的數字小於答案
        print("太小了！")
    else:  # 如果輸入的數字等於答案
        print("答對了！")
        break  # 跳出迴圈


# 字典(Dictionary) : 用來除純 [key-value] 配對的資料結構
# 字典很適合用來表示有對應關係的資料, 像是商品和價格的對應

# 建立字典:使用大括號{} ,key 和 value 之間用冒號 : 分隔
d = {"蘋果": 20, "香蕉": 30, "葡萄": 25}
print(d)

# 從中取得特定 key 對應的 value
# 如果 key 不存在會產生 KeyError 錯誤
d = {"蘋果": 20, "香蕉": 30, "葡萄": 25}
print(d["蘋果"])
# print(d["梨子"])  # 這行會產生 KeyError: '梨子'錯誤

# 遍歷字典:有多種方式可以走訪字典中的資料
d = {"蘋果": 20, "香蕉": 30, "葡萄": 25}

# 方式一:直接遍歷字典,會取得所有的 key
for k in d:
    print(k)  # 印出 key 名稱
    print(d[k])  # 印出 key 來取得對應的 value

# 方式二:明確使用 keys() 方法來取得所有 value
for k in d.keys():
    print(k)  # 印出 key 名稱
    print(d[k])  # 用 key 來取得對應的 value

# 方式三:使用 values() 方法來取得對應得 value
for v in d.values():
    print(v)  # 直接印出 value, 但不知道對應得 key 是甚麼

# 方式四:使用 items() 方法同時取得 key 和 value 的配對關係
# 這是最常用的方式, 因為可以同時存取 key 和 value
for k, v in d.items():
    print(f"{k}:{v}")  # 同時印出 key 和 value 的配對關係

# 新增/修改字典的內容
# 直接指定 key 對應的 value,如果 key 已存在就是修改,如果 key 不存在就是新增
d = {"蘋果": 20, "香蕉": 30, "葡萄": 25}
d["蘋果"] = 10
print(d)
d["蓮霧"] = 15
print(d)

# 刪除字典的內容
d = {"蘋果": 20, "香蕉": 30, "葡萄": 25}
d.pop("蘋果")
# 如果要刪掉的key不存在,會出現KeyError
# 這時候可以加上第二個參數,當key不存在時部會有任何變化
popitem = d.pop("蓮霧", "不存在這比資料")
print(d)
print(popitem)
