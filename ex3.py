# 条件语句示例
mark = 85
if mark >= 90:
    print("优秀")
elif mark >= 60:
    print("及格")
else:
    print("不及格")

# 循环语句示例
for num in range(5):
    if num == 3:
        continue
    print(f"当前数字: {num}")

# 异常处理示例
try:
    value = int(input("请输入一个数字："))
    result = 100 / value
    print(f"结果是: {result}")
except ZeroDivisionError:
    print("错误：除数不能为零！")
except ValueError:
    print("错误：请输入有效数字！")
finally:
    print("程序执行结束。")
