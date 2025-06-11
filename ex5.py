def greet():
    return "Greetings from mylib!"
# 导入自定义模块
import mylib

print(mylib.greet())

# 导入第三方模块
import requests

resp = requests.get("https://api.github.com")
print(f"状态码: {resp.status_code}")

# 包结构导入示例
from mypackage import mylib
