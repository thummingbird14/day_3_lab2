from ast import If


tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# def uncompleted(tasks_list):
#     uncompleted_tasks = []
#     for task in tasks_list:
#         if task["completed"] == False:
#             uncompleted_tasks.append(task)
    
#     return uncompleted_tasks

# print(uncompleted(tasks))


# def return_uncompleted(task_list_that_is_passed_as_an_argument):
#     list_of_uncompleted_that_we_want_to_return = []
#     for the_current_task_that_we_are_looping_over in task_list_that_is_passed_as_an_argument:
#         if the_current_task_that_we_are_looping_over["completed"] == False:
#             list_of_uncompleted_that_we_want_to_return.append(the_current_task_that_we_are_looping_over)
#     # We are now outside of the for loop 
#     return list_of_uncompleted_that_we_want_to_return

# def uncompleted(tasks_list):
#     uncompleted_tasks = []
#     for task in tasks_list:
#         if task["completed"] == True:
#             uncompleted_tasks.append(task)
    
#     return uncompleted_tasks

# print(uncompleted(tasks))

# def uncompleted(tasks_list):
#     uncompleted_tasks = []
#     for task in tasks_list:
#             uncompleted_tasks.append(task["description"])
    
#     return uncompleted_tasks

# print(uncompleted(tasks))

# 4. Print a list of tasks where time_taken is at least a given time

def long_task(tasks_list, time):
    uncompleted_tasks = []
    for task in tasks_list:
        if (time <= task["time_taken"]):
            uncompleted_tasks.append(task)
    
    return uncompleted_tasks

print(long_task(tasks, 30))
