import PySimpleGUI as s
import file


list = []
done = []
list = file.readFile()
done = file.readCompleted()
layout = [[s.Text("TODO LIST ")],[s.Text("New Event : "),s.InputText("",key = "data")],
          [s.CalendarButton("Choose Date", target="dispDate", key='date'),s.InputText("",key = "dispDate", disabled=True ,do_not_clear=False)],
          [s.Text("LIST : "), s.Listbox(values=list,key = "list",size=(40,6), enable_events=True), s.Text("FINISHED : "), s.Listbox(values=done,key = "complete",size=(40,6), enable_events=True)],
          [s.Slider(range=(10,1,-1),default_value=1,orientation="horizontal",key="priority")],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Button("finished")],
          [s.Text("", auto_size_text=False, key="tell")]]

window = s.Window("my first GUI ", layout)

while True:
    event, value = window.Read()
    if (event == "add"):
        if(value["dispDate"] == ""):
            window.Element("error").Update("Please input a date")
            continue
        if (value["data"] == ""):
            window.Element("error").Update("Please enter a value")
            continue

        x = value["data"]+" "+value["dispDate"]+" "+str(int(value["priority"]))
        list.append(x)
        window.FindElement("list").Update(list)
        window.Element("tell").Update("entry added")
        file.writeFile(list) #working

    elif( event == "delete"):
        list.remove(''.join(value["list"]))
        window.FindElement("list").Update(list)
        window.Element("tell").Update("entry deleted")
        file.writeFile(list) #working

    elif( event == "prioritize"):
        for i in range(len(list)):
            min = i
            for j in range(i+1, len(list)):
                if(list[min][-1] > list[j][-1]):
                    min = j
            list[i],list[min] = list[min],list[i]
        window.FindElement("list").Update(list)
        window.Element("tell").Update("prioritized")
        file.writeFile(list) #working

    elif( event == "finished"):
        list.remove(''.join(value["list"]))
        done.append(''.join(value["list"]))
        window.FindElement("list").Update(list)
        window.FindElement("complete").Update(done)
        window.Element("tell").Update("item completed")
        file.writeCompleted(done) #working


window.Close()
