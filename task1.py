todos = []

while True:
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
            print(todos)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
