import PySimpleGUI as s
import file as fi

list = []
done = []
list = fi.readFile()
done = fi.readCompleted()

layout = [[s.Text("TODO LIST ")],[s.Text("New Data : "),s.InputText("",key = "data")],
          [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True), s.Listbox(values=completed,key = "complete",size=(40,6), enable_events=True)],
          [s.CalendarButton("Choose Date", key='date'),s.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Button("completed"),s.Exit()],
          [s.Text("", auto_size_text=False, key="tell")]]

window = sg.Window('ToDo App', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event == "add":
        if(date == ''):
            window.FindElement('error').Update('choose date')
        x = entries["entry"] + " " + entries["dateDisp"] + " " + str(int(entries["priority"]))
        list.append(x)
        window.FindElement("list").Update(list)
        window.Element("tell").Update("item added")
        file.writeToFile(list)

    elif event == "delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
    elif event == None:
        break

window.Close()
