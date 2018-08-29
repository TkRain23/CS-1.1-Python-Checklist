import sys
import os
from termcolor import colored, cprint

checklist = list()  # initialize a list called checklist to store items


def create(item):  # this function creates an item within your list
    checklist.append(item)


def read(index):  # this function prints an item based on on it's index value
    try:
        item = checklist[int(index)]
        return item
    except ValueError:
        cprint('List Indices must be integers, not strings', 'white', 'on_red')
    except IndexError:
        cprint('Index out of Bounds', 'white', 'on_red')


def update(index, item):  # this function updates an item at a specific index
    try:
        checklist[int(index)] = item
    except ValueError:
        cprint('List Indices must be integers, not strings', 'white', 'on_red')
    except IndexError:
        cprint('Index out of Bounds', 'white', 'on_red')


def destroy(index):  # this function destroys an item at a specific index
    try:
        checklist.pop(int(index))
    except ValueError:
        cprint('List Indices must be integers, not strings', 'white', 'on_red')
    except IndexError:
        cprint('Index out of Bounds', 'white', 'on_red')


def list_all_items():  # this function lists all items
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    try:
        update(int(index), "{}{}".format("√", checklist[int(index)]))
    except ValueError:
        cprint('List Indices must be integers, not strings', 'white', 'on_red')
    except IndexError:
        cprint('Index out of Bounds', 'white', 'on_red')


def mark_incompleted(index):
    # removes the first character from the string fo this list
    try:
        update(index, checklist[int(index)][1:])
    except ValueError:
        cprint('List Indices must be integers, not strings', 'white', 'on_red')
    except IndexError:
        cprint('Index out of Bounds', 'white', 'on_red')


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select(function_code):

    if function_code == "A" or function_code == "a":
        input_item = user_input("Input Item:")
        create(input_item)
        os.system("clear")

    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number?")
        os.system("clear")
        destroy(item_index)

    elif function_code == "U" or function_code == "u":
        item_index = user_input("Index Number?")
        input_item = user_input("Input Item:")
        os.system("clear")
        update(item_index, input_item)

    elif function_code == "C" or function_code == "c":
        item_index = user_input("Index Number?")
        os.system("clear")
        mark_completed(item_index)

    elif function_code == "I" or function_code == "i":
        item_index = user_input("Index Number?")
        os.system("clear")
        mark_incompleted(item_index)

    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "Q" or function_code == "q":
        return False

    else:
        cprint('Unknown Option', 'cyan', 'on_white')

    return True


running = True
while running:
    selection = user_input(
        "Press A to Add to list, R to Remove, U to Update item, C to mark as" +
        " Completed, I to mark as mark_incompleted, and P to show list." +
        "\nPress Q to Exit. ")
    running = select(selection)
