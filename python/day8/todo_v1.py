tasks = []
while True:
    print("===========Todo List===========")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 退出")

    choice = input("请输入选择：")

    if choice == "1":
        input_task = input("请输入添加任务：")
        tasks.append(input_task)
        print("添加成功！")

    if choice == "2":
        print("当前任务：")
        for i in range(1, len(tasks) + 1):
            print(f"{i}.{tasks[i-1]}")
    if choice == "3":
        print("程序结束")
        break