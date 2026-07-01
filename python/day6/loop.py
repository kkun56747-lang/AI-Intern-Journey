count = int(input("请输入今天要完成几个任务："))
for i in range(1, count + 1):
    task = input(f"请输入第 {i} 个任务：")
    print(f"你输入的是：{task} ")