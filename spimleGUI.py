import PySimpleGUI
import functions

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter to-do", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_list(),
                               key='todos',
                               enable_events=True, size=(45, 10))
remove_button = PySimpleGUI.Button("Remove")
edit_button = PySimpleGUI.Button("Edit")
print(functions.get_list())
window = PySimpleGUI.Window("My To- Do Application",
                            layout=[
                                [label],
                                [input_box, add_button],
                                [list_box, remove_button,
                                 edit_button],
                                    ],
                            font=("Helvetica", 25))

while True:
    event, values = window.read()
    match event:
        case"Add":
            with open("text.txt", "a") as f:
                f.write(values["todo"] + "\n")
            window['todos'].update(values=functions.get_list())
        case "Remove":
            list = functions.get_list()
            try:
                todos = values["todos"][0] +'\n'
                list.remove(todos)
            except:
                todo = values['todo']
                list.remove(todo)
            with open("text.txt", 'w') as f:
                for item in list:
                    f.write(item)
            window['todos'].update(values=functions.get_list())
        case "Edit":
            todo_list = functions.get_list()
            edit_todo = values["todos"][0]
            new_todo = values["todo"]
            index = todo_list.index(edit_todo)
            todo_list[index] = new_todo + "\n"
            with open("text.txt", 'w') as f:
                for item in todo_list:
                    f.write(item)
            window['todos'].update(values=functions.get_list())
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            exit()

