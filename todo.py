#empty task list
tasks = []
#show tasks 

def display():
    length = len(tasks)
    if len(tasks) <= 0:
        print("Empty tasks \n")

    else:
        for task in range(length):
            print(f"{task+1}: {tasks[task]}")


#add task and give it a numberS
def addTask():
    global tasks
    toAdd = input("Add Task: ")
    tasks.append(toAdd)


#complete task
def completetask():
    global tasks

    display()
    
    finished = int(input("Which task number is Complete: "))
    if finished - 1 <= len(tasks):
        tasks.pop(finished-1)
    
#main that show options 

def main():

    while True:
        print("Todo App")
        print(" 1:Show Tasks \n 2: Add Task \n 3: Complete tasks \n 4: Quit \n")
        try:
            action = int(input("Action: "))
            if action == 1:
                display()
            elif action == 2:
                
                addTask()
            elif action == 3:
                
                completetask()
            elif action == 4:
                
                break
            else:
                print("Invlaid Input")
        except:
            print("Invlaid")

main()
