import PySimpleGUI as sg


def gui_window():
    layout = [[sg.Text('Voyage:', size=(35, 1)), sg.InputText('326', size=(20, 1))],
              [sg.Text('Event:', size=(35, 1)), sg.Drop(values=('Noon Sea','Noon River', 'Noon Port', 'Arrival', 'Departure'), size=(20, 1))],
              [sg.Text('Local Date/Time (YYYY-MM-DD HHmm):', size=(35, 1)), sg.InputText('2019-08-15 2205', size=(20, 1))],
              [sg.Text('Time Zone: (HHmm , - if W):', size=(35, 1)), sg.InputText('0100', size=(20, 1))],
              [sg.Text('Pressure:', size=(35, 1)), sg.InputText('1030', size=(20, 1))],
              [sg.Text('Temp:', size=(35, 1)), sg.InputText('25', size=(20, 1))],
              [sg.Text('Wind direction:', size=(35, 1)), sg.InputText('SSW', size=(20, 1))],
              [sg.Text('Wind force in kts:', size=(35, 1)), sg.InputText('3', size=(20, 1))],
              [sg.Text('Sea scale:', size=(35, 1)), sg.InputText('2', size=(20, 1))],
              [sg.Text('Sea direction:', size=(35, 1)), sg.InputText('SW', size=(20, 1))],
              [sg.Text('Swell height:', size=(35, 1)), sg.InputText('0', size=(20, 1))],
              [sg.Text('Course made good:', size=(35, 1)), sg.InputText('092', size=(20, 1))],
              [sg.Text('Log distance from last event:', size=(35, 1)), sg.InputText('230', size=(20, 1))],
              [sg.Text('GPS distance from last event:', size=(35, 1)), sg.InputText('225', size=(20, 1))],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('report_creator', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
        print('You entered ', values[1])
        print('You entered ', values[2])
        print('You entered ', values[3])
        print('You entered ', values[4])
        print('You entered ', values[5])
        print('You entered ', values[6])
        print('You entered ', values[7])
        print('You entered ', values[8])
        print('You entered ', values[9])
        print('You entered ', values[10])
        print('You entered ', values[11])
        print('You entered ', values[12])
        print('You entered ', values[13])

    window.close()

gui_window()