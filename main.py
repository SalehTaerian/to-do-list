from toDoList import ToDoList
from Task_Class import Task
myPlan = ToDoList()
print('*'*7 , "welcome" , '*'*7)
choice =1
while(choice):
    choice = int(input('''what do you want to do?
                   1-add task
                   2-delete task
                   3-show task
                   4 exit\n'''
                   ))
    if(choice==1):
        task_name = input('enter your taskname:')
        exp = input('enter explanation:')
        priority = input('enter priority:')
        tempTask = Task(task_name , exp , priority)
        myPlan.add_work(tempTask)
    elif(choice==2):
        name = input('enter taskname that you wanna delete:')
        myPlan.delete_work(name)
    elif(choice==3):
        myPlan.show_works()
    else:
        break
myPlan.save()
