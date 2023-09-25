""""
Tasks list
Commands:
    list (to list task)
    undo (to undo task)
    redo (to redo task)
    clear (to clear terminal)
    stop (to stop program)
"""

import os

def do_list(tasks):
    print()
    if not tasks:
        print('No tasks to list...')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()

def undo(tasks, undo_tasks):
    print()
    if not tasks:
        print('No tasks to undo...')
        return

    task = tasks.pop()
    print(f'{task=} removed from to-do list.')
    undo_tasks.append(task)
    print()

def redo(tasks, redo_task):
    print()
    if not redo_task:
        print('No task to redo...')
        return

    task = redo_task.pop()
    print(f'{task=} added to task list.')
    tasks.append(task)
    print()

def add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You dont type anything...')
        return

    elif task != 'stop':

        print(f'{task=} added to task list.')
        tasks.append(task)
        print()

tasks = []
redo_task = []

while True:
    print('Commands: list, undo, redo, clear, stop')
    task = input('Enter a task or command: ')
    
    commands = {
        'list': lambda: do_list(tasks),
        'undo': lambda: undo(tasks, redo_task),
        'redo': lambda: redo(tasks, redo_task),
        'clear': lambda: os.system('cls'),
        'add': lambda: add(task, tasks),
    }
    command = commands.get(task) if commands.get(task) is not None else \
        commands['add']
    command()

    if task == 'stop':
        print('task closed.')
        break
