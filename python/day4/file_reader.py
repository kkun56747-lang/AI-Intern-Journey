with open("python/day4/test.txt", "r", encoding="utf-8") as file:
 content = file.read()

print("文件共有：")
print(len(content), "个字符")
print("========")
print(content)
print("========")
print(content.upper())