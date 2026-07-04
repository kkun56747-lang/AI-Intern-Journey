tasks = []
def show_menu():
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 保存任务")
    print("5. 读取任务")
    print("6. 退出")
def show_tasks():
    if len(tasks) == 0:
        print("当前没有任务")
    else:
        print("当前任务：")
        for i in range(1, len(tasks) + 1):
            print(f"{i}.{tasks[i - 1]}")
while True:
 print("===========Todo List===========")
 show_menu()
 choice = input("请输入选择：")

 if choice == "1":
        input_task = input("请输入添加任务：")
        tasks.append(input_task)
        print("添加成功！")

        
 elif choice == "2":
        show_tasks()
        

 elif choice == "3":
        show_tasks()
        if len(tasks) == 0:
            try: 
              delete = int(input("请输入删除编号："))
              tasks.pop(delete - 1)
              print("删除成功！")
            except:
              print("输入错误！")

 elif choice == "4":
        with open("python/day10/tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        print("保存成功！")
        

 elif choice == "5":
        tasks.clear()
        with open("python/day10/tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())
        print("读取成功！")
        

 elif choice == "6":
        print("退出")
        break

print("============返回上级菜单============")
