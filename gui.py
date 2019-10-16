import PySimpleGUI as sg
from excel_process import excel_data_source, data
from datetime import datetime, timedelta
from dateutil import parser
from history_process import last_event_data, check_and_update_database


def gui_window():
    today = datetime.today()
    last_eta = parser.parse(last_event[9])
    voy_info = [[sg.Text('Voyage:', size=(35, 1)), sg.InputText(last_event[0], size=(20, 1))],  #0
                [sg.Text('Event:', size=(35, 1)),
                 sg.Drop(values=(
                 'Noon Sea', 'Noon River', 'Noon Port', 'Arrival', 'Departure', 'BOSP', 'EOSP', 'Drop Anchor',
                 'Anchor Aweigh'), size=(20, 1))],  #1

                [sg.Text('Local Date/Time:', size=(35, 1))],

                [sg.Text('YYYY:', size=(6, 1)),
                 sg.InputText(today.year, size=(4, 1)),  #2
                 sg.Text('MM:', size=(3, 1)),
                 sg.InputText(today.month, size=(3, 1)),  #3
                 sg.Text('DD:', size=(3, 1)),
                 sg.InputText(today.day, size=(3, 1)),  #4
                 sg.Text('HH:', size=(3, 1)),
                 sg.InputText('10', size=(3, 1)),  #5
                 sg.Text('mm:', size=(4, 1)),
                 sg.InputText('24', size=(3, 1))],  #6

                [sg.Text('Time Zone: (HH,H - if W):', size=(35, 1)),
                 sg.InputText(last_event[2], size=(20, 1))],  #7

                [sg.Text('Pressure:', size=(35, 1)),
                 sg.InputText('1030', size=(20, 1))],  #8

                [sg.Text('Temp:', size=(35, 1)),
                 sg.InputText('25', size=(20, 1))],  #9

                [sg.Text('Wind direction:', size=(35, 1)),
                 sg.InputText('SSW', size=(20, 1))],  #10

                [sg.Text('Wind force in kts:', size=(35, 1)),
                 sg.InputText('3', size=(20, 1))],   #11

                [sg.Text('Sea height:', size=(35, 1)),
                 sg.InputText('2', size=(20, 1))],  #12

                [sg.Text('Sea direction:', size=(35, 1)),
                 sg.InputText('SW', size=(20, 1))],  #13

                [sg.Text('Swell height:', size=(35, 1)),
                 sg.InputText('0', size=(20, 1))],  #14

                [sg.Text('Course made good:', size=(35, 1)),
                 sg.InputText('092', size=(20, 1))],  #15

                [sg.Text('Log distance from last event:', size=(35, 1)),
                 sg.InputText('230.5', size=(20, 1))],  #16

                [sg.Text('GPS distance from last event:', size=(35, 1)),
                 sg.InputText('225.8', size=(20, 1))],  #17

                [sg.Text('Latitude:', size=(35, 1)),
                 sg.InputText('52', size=(5, 1)), sg.InputText('15.6', size=(5, 1)),
                 sg.Drop(values=('N', 'S'), size=(2, 1))],  #18, 19, 20

                [sg.Text('Longitude:', size=(35, 1)),
                 sg.InputText('000', size=(5, 1)), sg.InputText('22.7', size=(5, 1)),
                 sg.Drop(values=('E', 'W'), size=(2, 1))],  #21, 22, 23

                [sg.Text('Next port:', size=(35, 1)),
                 sg.InputText(last_event[8], size=(20, 1))], #24

                [sg.Text('ETA:', size=(35, 1))],
                [sg.Text('YYYY:', size=(6, 1)),
                 sg.InputText(last_eta.year, size=(4, 1)),  #25
                 sg.Text('MM:', size=(3, 1)),
                 sg.InputText(last_eta.month, size=(3, 1)),  #26
                 sg.Text('DD:', size=(3, 1)),
                 sg.InputText(last_eta.day, size=(3, 1)),  #27
                 sg.Text('HH:', size=(3, 1)),
                 sg.InputText(last_eta.hour, size=(3, 1)),  #28
                 sg.Text('mm:', size=(4, 1)),
                 sg.InputText(last_eta.minute, size=(3, 1))],  #29

                [sg.Text("Destinantion's Time Zone: (HH,H - if W):", size=(35, 1)),
                 sg.InputText(last_event[10], size=(20, 1))],  #30

                [sg.Text('Bilges:', size=(35, 1)),
                 sg.InputText('Dry', size=(20, 1))],  #31

                [sg.Text('Master:', size=(35, 1)),
                 sg.InputText(last_event[11], size=(20, 1))],  #32

                [sg.Text('Remarks:', size=(35, 1))],

                [sg.Multiline(last_event[12], size=(57, 5))],  #33

                [sg.Button('Calculate')],

                # Voyage calculations to be made:

                [sg.Text('Time from last event:', size=(35, 1)),
                 sg.Text('', key='time_from_last', size=(20, 1))],

                [sg.Text('Average GPS speed from last event:', size=(35, 1)),
                 sg.Text('', key='avg_gps_spd', size=(20, 1))],

                [sg.Text('Average log speed from last event:', size=(35, 1)),
                 sg.Text('', key='avg_log_spd', size=(20, 1))],

                [sg.Text('Current:', size=(35, 1)),
                 sg.InputText(key='current', size=(20, 1))],

                [sg.Text('Total steaming time:', size=(35, 1)),
                 sg.Text('', key='voy_time', size=(20, 1))],

                [sg.Text('Total GPS distance:', size=(35, 1)),
                 sg.InputText(key='voy_dist', size=(20, 1))],

                [sg.Text('Voyage average speed:', size=(35, 1)),
                 sg.Text('', key='voy_avg_spd', size=(20, 1))],

                [sg.Text('Total log distance:', size=(35, 1)),
                 sg.Text('', key='voy_log_dist', size=(20, 1))],

                [sg.Text('Remaining distance:', size=(35, 1)),
                 sg.InputText(key='rem_dist', size=(20, 1))],

                [sg.Text('ETA (destination ZT) with present speed:', size=(35, 1)),
                 sg.Text('', key='real_eta', size=(20, 1))]
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

    cargo_info = [[sg.Text('Cargo ops in progress:', size=(35, 1)), sg.Drop(values=('No', 'Yes'), size=(20, 1))],
                  [sg.Text('Cargo ops commenced (LT):', size=(35, 1)), sg.InputText('comm_cargo_local', size=(20, 1))],
                  [sg.Text('Cargo ops completed (LT):', size=(35, 1)), sg.InputText('compl_cargo_local', size=(20, 1))],
                  [sg.Text('Cargo ROB:', size=(35, 1)), sg.InputText('cargo_rob', size=(20, 1))],
                  [sg.Text('Cargo loaded/discharged from last event:', size=(35, 1)),
                   sg.InputText('cargo_daily', size=(20, 1))],
                  [sg.Text('Cargo to go:', size=(35, 1)), sg.InputText('cargo_to_go', size=(20, 1))],
                  [sg.Text('Ballast water ROB:', size=(35, 1)), sg.InputText('ballast_rob', size=(20, 1))],
                  [sg.Text('Ballast water change from last event:', size=(35, 1)),
                   sg.InputText('ballast_daily', size=(20, 1))],
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

        [sg.Button('Submit'),
         sg.Button('Create reports'),
         sg.Button('Quit')]]

    window = sg.Window('report_creator').Layout([[sg.Column(layout, scrollable=True, vertical_scroll_only=True)]])
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Quit'):  # if user closes window or clicks quit
            return None
        if event == 'Calculate':
            time_local = datetime(int(values[2]), int(values[3]), int(values[4]),
                                  int(values[5]), int(values[6]))
            time_utc = time_local - timedelta(hours=float(values[7]))
            if last_event[4] is None:
                time_from_last_display = time_from_last = 0
            else:
                time_from_last = (time_utc - parser.parse(last_event[3])).total_seconds()

                n = time_from_last % (24 * 3600)
                hour = n // 3600

                n %= 3600
                minutes = n // 60

                time_from_last_display = f'{int(hour)}:{int(minutes)}'

            avg_gps_spd = float(values[17]) / (time_from_last / 3600)
            avg_log_spd = float(values[16]) / (time_from_last / 3600)
            current = avg_gps_spd - avg_log_spd

            voy_time = time_from_last + last_event[5]
            days = voy_time / (24 * 3600)
            n1 = voy_time % (24 * 3600)
            hour1 = n1 // 3600
            n1 %= 3600
            minutes1 = n1 // 60
            voy_time_display = f'{int(days)} days, {int(hour1)}:{int(minutes1)}'

            voy_dist = float(values[17]) + last_event[6]

            voy_avg_spd = voy_dist / (voy_time / 3600)

            voy_log_dist = float(values[16]) + float(last_event[7])

            rem_dist = float(last_event[4]) - float(values[17])

            time_rem_hrs = rem_dist / avg_gps_spd
            real_eta = time_utc + timedelta(hours=(time_rem_hrs + float(values[30])))

            window.Element('time_from_last').Update(time_from_last_display)
            window.Element('avg_gps_spd').Update(avg_gps_spd)
            window.Element('avg_log_spd').Update(avg_log_spd)
            window.Element('current').Update(current)
            window.Element('voy_time').Update(voy_time_display)
            window.Element('voy_dist').Update(voy_dist)
            window.Element('voy_avg_spd').Update(voy_avg_spd)
            window.Element('voy_log_dist').Update(voy_log_dist)
            window.Element('rem_dist').Update(rem_dist)
            window.Element('real_eta').Update(real_eta.strftime('%Y-%m-%d %H%M'))
        if event == 'Submit':
            user_dict = {
                '~VOY~': values[0],
                '~EVENT~': values[1],
                '~LOCATION~': 'AT SEA',
                '~TIMELOCAL~': time_local,
                '~TZ~': values[7],
                '~TIMEUTC~': time_utc,
                '~LAT~': f'{values[18]}-{values[19]}{values[20]}',
                '~LON~': f'{values[21]}-{values[22]}{values[23]}',
                '~GPSDIST~': values[17],
                '~TIMEFROMLAST~': time_from_last,
                '~REMAININGDIST~': rem_dist,
                '~LOGFROMLAST~': values[16],
                '~NEXTPORT~': values[24],
                '~ETATIMELOCAL~': parser.parse(f'{values[25]}-{values[26]}-{values[27]} {values[28]}:{values[29]}'),
                '~ETATZ~': values[30],
                '~WINDDIR~': values[10],
                '~WINDFORCEKTS~': values[11],
                '~SEAHEIGHT~': values[12],
                '~SEADIR~': values[13],
                '~SWELL~': values[14],
                '~BILGES~': values[31],
                '~REMARKS~': values[33],
                '~MASTER~': values[32],
                '~VOYDIST~': voy_dist,
                '~VOYTIME~': voy_time,
                '~VOYGPSAVGSPD~': voy_avg_spd,
                '~VOYLOGDIST~': voy_log_dist}

            if int(user_dict['~WINDFORCEKTS~']) < 1:
                user_dict['~WINDFORCEB~'] = 0
            elif 1 <= int(user_dict['~WINDFORCEKTS~']) <= 3:
                user_dict['~WINDFORCEB~'] = 1
            elif 4 <= int(user_dict['~WINDFORCEKTS~']) <= 6:
                user_dict['~WINDFORCEB~'] = 2
            elif 7 <= int(user_dict['~WINDFORCEKTS~']) <= 10:
                user_dict['~WINDFORCEB~'] = 3
            elif 11 <= int(user_dict['~WINDFORCEKTS~']) <= 16:
                user_dict['~WINDFORCEB~'] = 4
            elif 17 <= int(user_dict['~WINDFORCEKTS~']) <= 21:
                user_dict['~WINDFORCEB~'] = 5
            elif 22 <= int(user_dict['~WINDFORCEKTS~']) <= 27:
                user_dict['~WINDFORCEB~'] = 6
            elif 28 <= int(user_dict['~WINDFORCEKTS~']) <= 33:
                user_dict['~WINDFORCEB~'] = 7
            elif 34 <= int(user_dict['~WINDFORCEKTS~']) <= 40:
                user_dict['~WINDFORCEB~'] = 8
            elif 41 <= int(user_dict['~WINDFORCEKTS~']) <= 47:
                user_dict['~WINDFORCEB~'] = 9
            elif 48 <= int(user_dict['~WINDFORCEKTS~']) <= 55:
                user_dict['~WINDFORCEB~'] = 10
            elif 56 <= int(user_dict['~WINDFORCEKTS~']) <= 63:
                user_dict['~WINDFORCEB~'] = 11
            elif int(user_dict['~WINDFORCEKTS~']) <= 64:
                user_dict['~WINDFORCEB~'] = 12
            else:
                user_dict['~WINDFORCEB~'] = 0
            break

    window.close()
    return user_dict


er_excel = excel_data_source(data['FIRST_DATA'])
last_event = last_event_data()
gui_data = gui_window()
print(gui_data)

