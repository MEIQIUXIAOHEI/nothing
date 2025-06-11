# 变量类型示例
username = "Alice"         # str
user_age = 20              # int
score_list = [90, 85, 88]  # list
profile = {"name": username, "age": user_age}  # dict

# 类型转换示例
age_text = str(user_age)
num_value = int("123")

# 作用域示例
count = 10  # 全局变量

def update_count():
    local_value = 5  # 局部变量
    global count
    count += 1
    print(f"函数内部: count={count}, local_value={local_value}")

update_count()
print(f"函数外部: count={count}")
