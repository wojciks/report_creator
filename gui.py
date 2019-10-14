import PySimpleGUI as sg
from excel_process import excel_data_source, data

er_excel = excel_data_source(data['FIRST_DATA'])


def gui_window():
    voy_info = [[sg.Text('Voyage:', size=(35, 1)), sg.InputText('326', size=(20, 1))],
                [sg.Text('Event:', size=(35, 1)),
                 sg.Drop(values=('Noon Sea', 'Noon River', 'Noon Port', 'Arrival', 'Departure', 'BOSP', 'EOSP'), size=(20, 1))],

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
                 sg.InputText('225', size=(20, 1))],

                [sg.Text('Latitude:', size=(35, 1)),
                 sg.InputText('225', size=(5, 1)), sg.InputText('225', size=(5, 1)), sg.Drop(values=('N', 'S'), size=(2, 1))],

                [sg.Text('Longitude:', size=(35, 1)),
                 sg.InputText('225', size=(5, 1)), sg.InputText('225', size=(5, 1)), sg.Drop(values=('E', 'W'), size=(2, 1))],

                [sg.Text('Master:', size=(35, 1)),
                 sg.InputText('225', size=(20, 1))],

                [sg.Text('Remarks:', size=(35, 1))],

                [sg.InputText('225', size=(57, 1))],

                [sg.Button('Calculate')],

                [sg.Text('Time from last event:', size=(35, 1)),
                 sg.Text('time_from_last', size=(20, 1))],

                [sg.Text('Average GPS speed from last event:', size=(35, 1)),
                 sg.Text('avg_gps_spd', size=(20, 1))],

                [sg.Text('Average log speed from last event:', size=(35, 1)),
                 sg.Text('avg_log_spd', size=(20, 1))],

                [sg.Text('Current:', size=(35, 1)),
                 sg.Text('current', size=(20, 1))],

                [sg.Text('Total steaming time:', size=(35, 1)),
                 sg.Text('voy_time', size=(20, 1))],

                [sg.Text('Total GPS distance:', size=(35, 1)),
                 sg.Text('voy_dist', size=(20, 1))],

                [sg.Text('Voyage average speed:', size=(35, 1)),
                 sg.Text('voy_avg_spd', size=(20, 1))],

                [sg.Text('Total log distance:', size=(35, 1)),
                 sg.Text('voy_log_spd', size=(20, 1))],

                [sg.Text('Remaining distance:', size=(35, 1)),
                 sg.Text('rem_dist', size=(20, 1))]
                ]

    er_info = [[sg.Text('HFO ROB:', size=(35, 1)), sg.InputText(er_excel['~HFOROB~'], size=(20, 1))],
               [sg.Text('MDO ROB:', size=(35, 1)), sg.InputText(er_excel['~MDOROB~'], size=(20, 1))],
               [sg.Text('Lube oil (cylinders) ROB:', size=(35, 1)), sg.InputText(er_excel['~LOCYLROB~'], size=(20, 1))],
               [sg.Text('Lube oil (Main Engine) ROB:', size=(35, 1)),
                sg.InputText(er_excel['~LOMEROB~'], size=(20, 1))],
               [sg.Text('Lube oil (Aux engines):', size=(35, 1)), sg.InputText(er_excel['~LOAUXROB~'], size=(20, 1))],
               [sg.Text('Lube oil (Total):', size=(35, 1)), sg.InputText(er_excel['~LOTOTALROB~'], size=(20, 1))],
               [sg.Text('ME HFO consumption:', size=(35, 1)), sg.InputText(er_excel['~MEHFOCONS~'], size=(20, 1))],
               [sg.Text('ME MDO consumption:', size=(35, 1)), sg.InputText(er_excel['~MEMDOCONS~'], size=(20, 1))],
               [sg.Text('Aux engines HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~AUXHFOCONS~'], size=(20, 1))],
               [sg.Text('Aux engines MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~AUXMDOCONS~'], size=(20, 1))],
               [sg.Text('Boiler HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~BOILERHFOCONS~'], size=(20, 1))],
               [sg.Text('Boiler MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~BOILERMDOCONS~'], size=(20, 1))],
               [sg.Text('Total HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALHFOCONS~'], size=(20, 1))],
               [sg.Text('Total MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALMDOCONS~'], size=(20, 1))],
               [sg.Text('Lube oil consumpton (cylinders):', size=(35, 1)),
                sg.InputText(er_excel['~LOCYLCONS~'], size=(20, 1))],
               [sg.Text('Lube oil consumpton (ME):', size=(35, 1)), sg.InputText(er_excel['~LOMECONS~'], size=(20, 1))],
               [sg.Text('Lube oil consumpton (aux engines):', size=(35, 1)),
                sg.InputText(er_excel['~LOAUXCONS~'], size=(20, 1))],
               [sg.Text('Lube oil total consumpton:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALLOCONS~'], size=(20, 1))],
               [sg.Text('Average RPM:', size=(35, 1)), sg.InputText(er_excel['~RPM~'], size=(20, 1))],
               [sg.Text('ME distance:', size=(35, 1)), sg.InputText(er_excel['~MEDIST~'], size=(20, 1))],
               [sg.Text('ME speed:', size=(35, 1)), sg.InputText(er_excel['~MESPD~'], size=(20, 1))],
               [sg.Text('Slip:', size=(35, 1)), sg.InputText(er_excel['~SLIP~'], size=(20, 1))],
               [sg.Text('ME average kW:', size=(35, 1)), sg.InputText(er_excel['~MEKW~'], size=(20, 1))],
               [sg.Text('ME total kWh:', size=(35, 1)), sg.InputText(er_excel['~MEKWH~'], size=(20, 1))],
               [sg.Text('ME load:', size=(35, 1)), sg.InputText(er_excel['~MELOAD~'], size=(20, 1))],
               [sg.Text('ME governor setting:', size=(35, 1)), sg.InputText(er_excel['~MEGOV~'], size=(20, 1))],
               [sg.Text('Aux engines total time:', size=(35, 1)), sg.InputText(er_excel['~AUXTIME~'], size=(20, 1))],
               [sg.Text('Aux engines average kW:', size=(35, 1)), sg.InputText(er_excel['~AUXKW~'], size=(20, 1))],
               [sg.Text('Aux engines total kWh:', size=(35, 1)), sg.InputText(er_excel['~AUXKWH~'], size=(20, 1))],
               [sg.Text('Fresh water ROB:', size=(35, 1)), sg.InputText(er_excel['~FWROB~'], size=(20, 1))],
               [sg.Text('Fresh water produced:', size=(35, 1)), sg.InputText(er_excel['~FWPROD~'], size=(20, 1))],
               [sg.Text('Fresh water consumed:', size=(35, 1)), sg.InputText(er_excel['~FWCONS~'], size=(20, 1))],
               [sg.Text('Sludge tank content:', size=(35, 1)), sg.InputText(er_excel['~SLUDGETK~'], size=(20, 1))],
               [sg.Text('Oily bilge tank content:', size=(35, 1)),
                sg.InputText(er_excel['~OILYBILGETK~'], size=(20, 1))],
               [sg.Text('Incinerator settling tank content:', size=(35, 1)),
                sg.InputText(er_excel['~INCINERATORSETTLINGTK~'], size=(20, 1))],
               [sg.Text('Incinerator service tank content:', size=(35, 1)),
                sg.InputText(er_excel['~INCINERATORSERVICETK~'], size=(20, 1))],
               [sg.Text('Bilge water tank content:', size=(35, 1)),
                sg.InputText(er_excel['~BILGEWATERTK~'], size=(20, 1))],
               [sg.Text('Sludge total:', size=(35, 1)), sg.InputText(er_excel['~SLUDGETOTAL~'], size=(20, 1))]
               ]

    cargo_info = [[sg.Text('Cargo ops in progress:', size=(35, 1)), sg.Drop(values=('Yes', 'No'), size=(20, 1))],
                  [sg.Text('Cargo ops commenced (LT):', size=(35, 1)), sg.InputText('comm_cargo_local', size=(20, 1))],
                  [sg.Text('Cargo ops completed (LT):', size=(35, 1)), sg.InputText('compl_cargo_local', size=(20, 1))],
                  [sg.Text('Cargo ROB:', size=(35, 1)), sg.InputText('cargo_rob', size=(20, 1))],
                  [sg.Text('Cargo loaded/discharged from last event:', size=(35, 1)), sg.InputText('cargo_daily', size=(20, 1))],
                  [sg.Text('Cargo to go:', size=(35, 1)), sg.InputText('cargo_to_go', size=(20, 1))],
                  [sg.Text('Ballast water ROB:', size=(35, 1)), sg.InputText('ballast_rob', size=(20, 1))],
                  [sg.Text('Ballast water change from last event:', size=(35, 1)), sg.InputText('ballast_daily', size=(20, 1))],
                  [sg.Text('Number of shore cranes:', size=(35, 1)),
                   sg.InputText('shore_cranes_no', size=(20, 1))],
                  [sg.Text('Number of ship cranes:', size=(35, 1)),
                   sg.InputText('ship_cranes_no', size=(20, 1))],
                  [sg.Text('Estimated time completion (LT):', size=(35, 1)),
                   sg.InputText('etc_local', size=(20, 1))],
                  [sg.Text('Estimated time departure (LT):', size=(35, 1)),
                   sg.InputText('etd_local', size=(20, 1))]]

    # Create the Window
    layout = [
        [sg.TabGroup([[sg.Tab('Nav info', voy_info),
                       sg.Tab('Engine info', er_info),
                       sg.Tab('Cargo Info', cargo_info)]])],

        [sg.Button('Ok'),
         sg.Button('Cancel')]]

    window = sg.Window('report_creator').Layout([[sg.Column(layout, scrollable=True, vertical_scroll_only=True)]])
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break

        for i in range(0, 52):
            print('You entered ', values[i])

    window.close()


gui_window()
