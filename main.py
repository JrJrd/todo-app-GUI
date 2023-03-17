# from functions import get_todos, write_todos
import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input(" type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            print('here is todos existing files', todos)
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Not a valid command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todos.pop(number - 1)

            functions.write_todos(todos)

        except IndexError:
            print("no item with that number")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("invalid input")

print("bye!")
