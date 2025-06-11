# 函数定义示例
def say_hello(person, msg="Hello"):
    return f"{msg}, {person}!"

print(say_hello("Alice"))         # Hello, Alice!
print(say_hello("Bob", "Hi"))     # Hi, Bob!

# 可变参数示例
def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1, 2, 3, 4))    # 10

# 匿名函数示例
multiply_by_two = lambda n: n * 2
print(multiply_by_two(5))         # 10

# 高阶函数示例
def execute(func, data):
    return func(data)

print(execute(lambda v: v ** 2, 4))   # 16
