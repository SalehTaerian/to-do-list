import toDoList
class toDoList:
    def __init__(self):
        self.task_list = list()
    def add_work(self , new_work):
        self.task_list.append(new_work)
    def delete_work(self ,name):
        for task in self.task_list:
            if(task.name == name):
                self.task_list.remove(task)   
    def show_works(self):
        pass
    def save_load(self):
        pass