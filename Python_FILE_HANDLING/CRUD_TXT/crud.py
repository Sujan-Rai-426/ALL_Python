class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "Python_FILE_HANDLING/CRUD_TXT/crud.txt"
        self.load_tasks()
    
    # <== [ LOAD / READ ] === Existing Task
    def load_tasks(self):
        '''Load tasks from file'''
        try:
            with open(self.filename, 'r') as f:
                self.tasks = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.tasks = []
    
    # <== [ ADD / WRITE ] === NEW Task
    def save_new_task(self):
        '''Save tasks to file'''
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(task + "\n")
    
    
    # ADD function
    def add_task(self):
        '''Add a new task'''
        new_task = input("Enter task: ")
        self.tasks.append(new_task)
        self.save_new_task()
        print("✅ Task added!")
    
    
    # View function
    def view_tasks(self):
        '''View all tasks'''
        if not self.tasks:
            print("📭 No tasks!")
            return
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
    
    
    # Delete function
    def delete_task(self):
        '''Delete a task'''
        self.view_tasks()
        if self.tasks:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(self.tasks):
                    removed = self.tasks.pop(num-1)
                    self.save_tasks()
                    print(f"✅ Deleted: {removed}")
                else:
                    print("❌ Invalid number!")
            except ValueError:
                print("❌ Please enter a number!")

# Run the to-do list
todo = TodoList()
while True:
    print("\n✅ To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Choose option: ")
    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.delete_task()
    elif choice == "4":
        print("👋 Goodbye!")
        break