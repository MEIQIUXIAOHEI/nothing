# 写入文本文件
with open("output.txt", "w") as file:
    file.write("Hello, Python!\n")

# 读取文本文件
with open("output.txt", "r") as file:
    data = file.read()
    print(data)

# CSV 文件操作
import csv

with open("people.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Alice", 20])
