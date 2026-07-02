tasks = []

count = int(input("请输入今天几个任务："))

for i in range(1, count + 1):
    task = input(f"请输入第 {i} 个任务：")
    tasks.append(task)

for i in range(1, len(tasks) + 1):
    print(f"{i}.{tasks[i-1]}")