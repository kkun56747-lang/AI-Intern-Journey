tasks = []
while True:
    print("===========Todo List===========")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 退出")

    choice = input("请输入选择：")

    if choice == "1":
        input_task = input("请输入添加任务：")
        tasks.append(input_task)
        print("添加成功！")

        
    elif choice == "2":
        if len(tasks) == 0:
            print("当前没有任务")
        else:
            print("当前任务：")
            for i in range(1,len(tasks)+1):
             print(f"{i}.{tasks[i-1]}")
        

    elif choice == "3":
        if len(tasks) == 0:
            print("当前没有任务")
        else: 
            print("当前任务：")
            for i in range(1,len(tasks)+1):
              print(f"{i}.{tasks[i-1]}")
            delete = input("请输入删除编号：")
            tasks.pop(int(delete) - 1)
            print("删除成功！")

    elif choice == "4":
        print("程序结束")
        break

    print("============返回上级菜单============")