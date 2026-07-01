study = input("今天学习了什么？")
problem = input("今天遇到了什么问题？") 
harvest = input("今天最大的收获？")

with open("python/day5/learning_log.txt", "w", encoding="utf-8") as file:
    file.write(f"""===============
AI 学习日志
===============

今天学习：
{study}

遇到的问题：
{problem}

今天最大的收获：
{harvest}
""")


print("文件写入成功！")