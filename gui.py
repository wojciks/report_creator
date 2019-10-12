import PySimpleGUI as sg


def gui_window():
    voy_info = [[sg.Text('Voyage:', size=(35, 1)), sg.InputText('326', size=(20, 1))],
              [sg.Text('Event:', size=(35, 1)),
               sg.Drop(values=('Noon Sea','Noon River', 'Noon Port', 'Arrival', 'Departure'), size=(20, 1))],

              [sg.Text('Local Date/Time (YYYY-MM-DD HHmm):', size=(35, 1)),
               sg.InputText('2019-08-15 2205', size=(20, 1))],

              [sg.Text('Time Zone: (HHmm , - if W):', size=(35, 1)),
               sg.InputText('0100', size=(20, 1))],

              [sg.Text('Pressure:', size=(35, 1)),
               sg.InputText('1030', size=(20, 1))],

              [sg.Text('Temp:', size=(35, 1)),
               sg.InputText('25', size=(20, 1))],

              [sg.Text('Wind direction:', size=(35, 1)),
               sg.InputText('SSW', size=(20, 1))],

              [sg.Text('Wind force in kts:', size=(35, 1)),
               sg.InputText('3', size=(20, 1))],

              [sg.Text('Sea scale:', size=(35, 1)),
               sg.InputText('2', size=(20, 1))],

              [sg.Text('Sea direction:', size=(35, 1)),
               sg.InputText('SW', size=(20, 1))],

              [sg.Text('Swell height:', size=(35, 1)),
               sg.InputText('0', size=(20, 1))],

              [sg.Text('Course made good:', size=(35, 1)),
               sg.InputText('092', size=(20, 1))],

              [sg.Text('Log distance from last event:', size=(35, 1)),
               sg.InputText('230', size=(20, 1))],

              [sg.Text('GPS distance from last event:', size=(35, 1)),
               sg.InputText('225', size=(20, 1))]]


    er_info = [[sg.Text('HFO ROB:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('MDO ROB:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil (cylinders) ROB:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil (Main Engine) ROB:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil (Aux engines):', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil (Total):', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME HFO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME MDO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Aux engines HFO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Aux engines MDO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Boiler HFO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Boiler MDO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Total HFO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Total MDO consumption:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil consumpton (cylinders):', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil consumpton (ME):', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil consumpton (aux engines):', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Lube oil total consumpton:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Average RPM:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME distance:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME speed:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Slip:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME average kW:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME total kWh:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME load:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('ME governor setting:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Aux engines total time:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Aux engines average kW:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Aux engines total kWh:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Fresh water ROB:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Fresh water produced:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Fresh water consumed:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Sludge tank content:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Oily bilge tank content:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Incinerator settling tank content:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Incinerator service tank content:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Bilge water tank content:', size=(35, 1)), sg.InputText('700', size=(20, 1))],
               [sg.Text('Sludge total:', size=(35, 1)), sg.InputText('700', size=(20, 1))]
               ]

    # Create the Window
    layout = [
        [sg.TabGroup([[sg.Tab('Nav info', voy_info),
                       sg.Tab('Engine info', er_info)]])],

        [sg.Button('Ok'),
         sg.Button('Cancel')]]

    window = sg.Window('report_creator').Layout([[sg.Column(layout, scrollable=True, vertical_scroll_only=True)]])
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break

        for i in range(0, 51):
            print('You entered ', values[i])

    window.close()
gui_window()