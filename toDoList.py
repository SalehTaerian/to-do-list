from Task_Class import Task
import csv


class ToDoList:
    def __init__(self):
        self.task_list = list()
        self.myCSV = open("Tasks.csv", "a+")
        self.myCSV.seek(0)
        data = csv.reader(self.myCSV)
        if data :
            pass
        else:
            writer = csv.writer(self.myCSV)
            writer.writerow(['name' ,'explanation' , 'priority'])
        self.load()
    def add_work(self, new_work):
        self.task_list.append(new_work)
    def delete_work(self, name):
        for task in self.task_list:
            if task.name == name:
                self.task_list.remove(task)

    def show_works(self):
        for work in self.task_list:
            print(work.name, "\n", work.explanation, "\n", work.priority)
            print("*" * 15)

    
