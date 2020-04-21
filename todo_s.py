# name: "TO DO" app (simplified TXT version)
# version: 0.1 (beta)
# author: Valeriy B.

# Usage:
# The app works from keyboard inputs:
    # 1. Type a task you want to add to the 'TO DO' app list;
    # 2. Type '!print' command to print the tasks from the app list;
    # 3. Type '!remove' command to remove a task from the list;
    # 4. Type '!finish' to stop the app.

# NOTE: All the inputs are case sensitive in this app version: 'Call' and 'call' are not the same words

import os
import time
import fileinput


# create a 'txt' file
def create_file_txt():
    with open("tasks.txt", "w") as txt_file:
        txt_file.write("TASKS FROM TO DO LIST\n\n")


# verifying today's date
def today_date():
    today_date_elem = time.asctime(time.localtime())
    return today_date_elem


# append tasks to 'txt' file
def create_tasks_txt(input_task):
    if os.path.exists("tasks.txt") == False:
        create_file_txt()

    with open("tasks.txt", "a") as append_task_txt:
        input_task_all = input_task + "\n"
        append_task_txt.writelines(input_task_all)


# remove the tasks from the app
def remove_tasks():
    task_delete = input("Type the task you want to remove: ")
    for line in fileinput.input("tasks.txt", inplace=True):
        if task_delete in line:
            continue
        print(line, end='')


# read the tasks file
def print_tasks():
    with open("tasks.txt", "r") as file:
        print(file.read())


# running the app
def app_run(run_commands):

    # add today's day at the top of the 'txt' file
    with open("tasks.txt", "a") as txt_file_date:
        txt_file_date.writelines("\n" + today_date()[4:10] + ", " + today_date()[-4:] + " (" + today_date()[11:16] + ")" + "\n\n")

    print("You can type a task to add it to the app or commands: '!print' for printing the tasks; '!remove' to remove a task from the app")

    # start looping
    count = 1
    while run_commands != "!finish":
        run_commands = input("Type a task or a command: ")
        add_task = str(count) + ". " + run_commands
        if run_commands == "!remove":
            print_tasks()
            remove_tasks()
        elif run_commands == "!print":
            print_tasks()
        else:
            create_tasks_txt(add_task)  # append tasks to 'txt' file
        count += 1

    # remove '!finish' as a task input
    finish_input = "!finish"
    for line in fileinput.input("tasks.txt", inplace=True):
        if finish_input in line:
            continue
        print(line, end='')

    print("Thank you! All changes made to 'tasks.txt' file")


app_run("")



