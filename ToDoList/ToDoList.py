def addTask(taskName):
    tasks.append(taskName)
    print(tasks)

def deleteTask(taskName):
    print(tasks)
    pos = int(input("Enter position: "))
    tasks.pop(pos-1)
    print(tasks)

def editTask(oldTask, newTask):
    pos = int(input("Enter position: "))
    tasks.pop(pos-1)
    tasks.insert(pos-1, newTask)
    print(newTask)


tasks = []

while(True):
    print("Enter the task: 1.Add 2.Delete 3.Edit")
    num = int(input())

    if(num == 1):
        inpt = input()
        addTask(inpt)

    elif(num == 2):
        deleteTask(inpt)

    elif(num == 3):
        print(tasks)
        new = input("new Task: ")
        editTask(inpt, new)

    else:
        break

print(tasks)

