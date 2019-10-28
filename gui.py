from datetime import datetime, timedelta

import PySimpleGUI as sg
from dateutil import parser

from excel_process import excel_data_source, data, to_next_excel_entry
from history_process import last_event_data, check_and_update_database
from text_file_process import report_creation


def gui_window():
    today = datetime.today()
    today_list = [today.year, today.month, today.day, today.hour, today.minute]
    possible_events = ('Noon Sea', 'Noon River', 'Noon Port', 'Arrival', 'Departure', 'BOSP', 'EOSP', 'Drop Anchor',
                     'Anchor Aweigh', 'Bunkering')
    if last_event is None:
        voyage_no = location = time_zone = next_port = dest_tz = master = cargo_rob = ballast_rob = ''
    else:
        voyage_no = last_event[0]
        time_zone = round(float(last_event[2]), 1)
        next_port = last_event[8]
        dest_tz = round(float(last_event[10]), 1)
        master = last_event[11]
        cargo_rob = last_event[12]
        ballast_rob = last_event[17]
        location = last_event[18]

    last_eta_lt = check_datetime_data_present(last_event[9], dest_tz)
    c_ops_comm_lt = check_datetime_data_present(last_event[13], time_zone)
    c_ops_compl_lt = check_datetime_data_present(last_event[14], time_zone)
    etc = check_datetime_data_present(last_event[15], 0)
    etd = check_datetime_data_present(last_event[16], 0)

    general_info = [[sg.Text('Voyage:', size=(35, 1)), sg.InputText(voyage_no, size=(20, 1), key='voy')],  # 0
                [sg.Text('Event:', size=(35, 1)),
                 sg.Drop(values=possible_events, size=(20, 1), key='event')],

                [sg.Text('Location:', size=(35, 1)),
                 sg.InputText(location, size=(20, 1), key='location')],

                [sg.Text('Local Date/Time:', size=(35, 1))],
                time_read('local_time', today_list),

                [sg.Text('Time Zone: (HH,H - if W):', size=(35, 1)),
                 sg.InputText(time_zone, size=(20, 1), key='tz')],

                [sg.Text('Latitude:', size=(35, 1)),
                 sg.InputText(size=(5, 1), key='lat_deg'), sg.InputText(size=(5, 1), key='lat_min'),
                 sg.Drop(values=('', 'N', 'S'), size=(2, 1), key='lat_hemisphere')],

                [sg.Text('Longitude:', size=(35, 1)),
                 sg.InputText(size=(5, 1), key='long_deg'), sg.InputText(size=(5, 1), key='long_min'),
                 sg.Drop(values=('', 'E', 'W'), size=(2, 1), key='long_hemisphere')]]

    voy_info = [[sg.Text('Pressure:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='pressure')],

                [sg.Text('Temp:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='airtemp')],

                [sg.Text('Wind direction:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='wind_dir')],

                [sg.Text('Wind force in kts:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='wind_force')],

                [sg.Text('Sea height:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='sea_height')],

                [sg.Text('Sea direction:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='sea_dir')],

                [sg.Text('Swell height:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='swell')],

                [sg.Text('Course made good:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='cog')],

                [sg.Text('Log distance from last event:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='log')],

                [sg.Text('GPS distance from last event:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='gps_dist')],

                [sg.Text('Next port:', size=(35, 1)),
                 sg.InputText(next_port, size=(20, 1), key='next_port')],

                [sg.Text('ETA:', size=(35, 1))],
                time_read('eta_lt', last_eta_lt),

                [sg.Text("Destinantion's Time Zone: (HH,H - if W):", size=(35, 1)),
                 sg.InputText(dest_tz, size=(20, 1), key='dest_tz')],

                [sg.Text('Bilges:', size=(35, 1)),
                 sg.InputText(size=(20, 1), key='bilges')],

                [sg.Text('Master:', size=(35, 1)),
                 sg.InputText(master, size=(20, 1), key='master')],

                [sg.Text('Remarks:', size=(35, 1))],
                [sg.Multiline(size=(57, 5), key='remarks')],

                [sg.Button('Calculate')],

                # Voyage calculations to be made:

                [sg.Text('Time from last event:', size=(35, 1)),
                 sg.InputText(key='time_from_last', size=(20, 1))],

                [sg.Text('Average GPS speed from last event:', size=(35, 1)),
                 sg.InputText(key='avg_gps_spd', size=(20, 1))],

                [sg.Text('Average log speed from last event:', size=(35, 1)),
                 sg.InputText(key='avg_log_spd', size=(20, 1))],

                [sg.Text('Current:', size=(35, 1)),
                 sg.InputText(key='current', size=(20, 1))],

                [sg.Text('Wind force in Beaufort scale:', size=(35, 1)),
                 sg.InputText(key='wind_b', size=(20, 1))],

                [sg.Text('Total steaming time:', size=(35, 1)),
                 sg.InputText(key='voy_time', size=(20, 1))],

                [sg.Text('Total GPS distance:', size=(35, 1)),
                 sg.InputText('', key='voy_dist', size=(20, 1))],

                [sg.Text('Voyage average speed:', size=(35, 1)),
                 sg.InputText(key='voy_avg_spd', size=(20, 1))],

                [sg.Text('Total log distance:', size=(35, 1)),
                 sg.InputText(key='voy_log_dist', size=(20, 1))],

                [sg.Text('Remaining distance:', size=(35, 1)),
                 sg.InputText(key='rem_dist', size=(20, 1))],

                [sg.Text('ETA (destination ZT) with present speed:', size=(35, 1)),
                 sg.Text('', key='real_eta', size=(20, 1))],

                [sg.Text('Speed required for given ETA:', size=(35, 1)),
                 sg.Text('', key='speed_req', size=(20, 1))]
                ]

    er_info = [[sg.Text('HFO ROB:', size=(35, 1)), sg.InputText(er_excel['~HFOROB~'], size=(20, 1), key='HFOROB')],
               [sg.Text('MDO ROB:', size=(35, 1)), sg.InputText(er_excel['~MDOROB~'], size=(20, 1), key='MDOROB')],
               [sg.Text('Lube oil (cylinders) ROB:', size=(35, 1)),
                sg.InputText(er_excel['~LOCYLROB~'], size=(20, 1), key='LOCYLROB')],
               [sg.Text('Lube oil (Main Engine) ROB:', size=(35, 1)),
                sg.InputText(er_excel['~LOMEROB~'], size=(20, 1), key='LOMEROB')],
               [sg.Text('Lube oil (Aux engines) ROB:', size=(35, 1)),
                sg.InputText(er_excel['~LOAUXROB~'], size=(20, 1), key='LOAUXROB')],
               [sg.Text('Lube oil (Total) ROB:', size=(35, 1)),
                sg.InputText(er_excel['~LOTOTALROB~'], size=(20, 1), key='LOTOTALROB')],
               [sg.Text('ME HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~MEHFOCONS~'], size=(20, 1), key='MEHFOCONS')],
               [sg.Text('ME MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~MEMDOCONS~'], size=(20, 1), key='MEMDOCONS')],
               [sg.Text('Aux engines HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~AUXHFOCONS~'], size=(20, 1), key='AUXHFOCONS')],
               [sg.Text('Aux engines MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~AUXMDOCONS~'], size=(20, 1), key='AUXMDOCONS')],
               [sg.Text('Boiler HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~BOILERHFOCONS~'], size=(20, 1), key='BOILERHFOCONS')],
               [sg.Text('Boiler MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~BOILERMDOCONS~'], size=(20, 1), key='BOILERMDOCONS')],
               [sg.Text('Total HFO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALHFOCONS~'], size=(20, 1), key='TOTALHFOCONS')],
               [sg.Text('Total MDO consumption:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALMDOCONS~'], size=(20, 1), key='TOTALMDOCONS')],
               [sg.Text('Lube oil consumption (cylinders):', size=(35, 1)),
                sg.InputText(er_excel['~LOCYLCONS~'], size=(20, 1), key='LOCYLCONS')],
               [sg.Text('Lube oil consumption (ME):', size=(35, 1)),
                sg.InputText(er_excel['~LOMECONS~'], size=(20, 1), key='LOMECONS')],
               [sg.Text('Lube oil consumption (aux engines):', size=(35, 1)),
                sg.InputText(er_excel['~LOAUXCONS~'], size=(20, 1), key='LOAUXCONS')],
               [sg.Text('Lube oil total consumption:', size=(35, 1)),
                sg.InputText(er_excel['~TOTALLOCONS~'], size=(20, 1), key='TOTALLOCONS')],
               [sg.Text('Average RPM:', size=(35, 1)), sg.InputText(er_excel['~RPM~'], size=(20, 1), key='RPM')],
               [sg.Text('ME distance:', size=(35, 1)), sg.InputText(er_excel['~MEDIST~'], size=(20, 1), key='MEDIST')],
               [sg.Text('ME speed:', size=(35, 1)), sg.InputText(er_excel['~MESPD~'], size=(20, 1), key='MESPD')],
               [sg.Text('Slip:', size=(35, 1)), sg.InputText(er_excel['~SLIP~'], size=(20, 1), key='SLIP')],
               [sg.Text('ME average kW:', size=(35, 1)), sg.InputText(er_excel['~MEKW~'], size=(20, 1), key='MEKW')],
               [sg.Text('ME total kWh:', size=(35, 1)), sg.InputText(er_excel['~MEKWH~'], size=(20, 1), key='MEKWH')],
               [sg.Text('ME load:', size=(35, 1)), sg.InputText(er_excel['~MELOAD~'], size=(20, 1), key='MELOAD')],
               [sg.Text('ME governor setting:', size=(35, 1)),
                sg.InputText(er_excel['~MEGOV~'], size=(20, 1), key='MEGOV')],
               [sg.Text('Aux engines total time:', size=(35, 1)),
                sg.InputText(er_excel['~AUXTIME~'], size=(20, 1), key='AUXTIME')],
               [sg.Text('Aux engines average kW:', size=(35, 1)),
                sg.InputText(er_excel['~AUXKW~'], size=(20, 1), key='AUXKW')],
               [sg.Text('Aux engines total kWh:', size=(35, 1)),
                sg.InputText(er_excel['~AUXKWH~'], size=(20, 1), key='AUXKWH')],
               [sg.Text('Fresh water ROB:', size=(35, 1)),
                sg.InputText(er_excel['~FWROB~'], size=(20, 1), key='FWROB')],
               [sg.Text('Fresh water produced:', size=(35, 1)),
                sg.InputText(er_excel['~FWPROD~'], size=(20, 1), key='FWPROD')],
               [sg.Text('Fresh water consumed:', size=(35, 1)),
                sg.InputText(er_excel['~FWCONS~'], size=(20, 1), key='FWCONS')],
               [sg.Text('Sludge tank content:', size=(35, 1)),
                sg.InputText(er_excel['~SLUDGETK~'], size=(20, 1), key='SLUDGETK')],
               [sg.Text('Oily bilge tank content:', size=(35, 1)),
                sg.InputText(er_excel['~OILYBILGETK~'], size=(20, 1), key='OILYBILGETK')],
               [sg.Text('Incinerator settling tank content:', size=(35, 1)),
                sg.InputText(er_excel['~INCINERATORSETTLINGTK~'], size=(20, 1), key='INCINERATORSETTLINGTK')],
               [sg.Text('Incinerator service tank content:', size=(35, 1)),
                sg.InputText(er_excel['~INCINERATORSERVICETK~'], size=(20, 1), key='INCINERATORSERVICETK')],
               [sg.Text('Bilge water tank content:', size=(35, 1)),
                sg.InputText(er_excel['~BILGEWATERTK~'], size=(20, 1), key='BILGEWATERTK')],
               [sg.Text('Sludge total:', size=(35, 1)),
                sg.InputText(er_excel['~SLUDGETOTAL~'], size=(20, 1), key='SLUDGETOTAL')]
               ]

    cargo_info = [
        [sg.Text('Cargo ops in progress:', size=(35, 1)), sg.Drop(key='if_cargo', values=('No', 'Yes'), size=(20, 1))],
        [sg.Text('Cargo ops commenced (LT):', size=(35, 1))],
         time_read('c_ops_comm', c_ops_comm_lt),

        [sg.Text('Cargo ops completed (LT):', size=(35, 1))],
         time_read('c_ops_compl', c_ops_compl_lt),

        [sg.Text('Cargo ROB:', size=(35, 1)), sg.InputText(cargo_rob, key='cargo_rob', size=(20, 1))],
        [sg.Text('Cargo loaded/discharged from last event:', size=(35, 1)),
         sg.InputText(key='cargo_daily', size=(20, 1))],
        [sg.Text('Cargo to go:', size=(35, 1)), sg.InputText(key='cargo_to_go', size=(20, 1))],
        [sg.Text('Ballast water ROB:', size=(35, 1)), sg.InputText(ballast_rob, key='ballast_rob', size=(20, 1))],
        [sg.Text('Ballast water change from last event:', size=(35, 1)),
         sg.InputText(key='ballast_daily', size=(20, 1))],
        [sg.Text('Number of shore cranes:', size=(35, 1)),
         sg.InputText(key='shore_cranes_no', size=(20, 1))],
        [sg.Text('Number of ship cranes:', size=(35, 1)),
         sg.InputText(key='ship_cranes_no', size=(20, 1))],
        [sg.Text('Estimated time completion (LT):', size=(35, 1))],
        time_read('etc', etc),
        [sg.Text('Estimated time departure (LT):', size=(35, 1))],
         time_read('etd', etd)
    ]

    noon_rep = [[sg.Text('Here will go noon report values which will sum values from last 24hrs', size=(57, 5))]]

    column = [sg.TabGroup([[sg.Tab('Nav info', voy_info),
               sg.Tab('Engine info', er_info),
               sg.Tab('Cargo Info', cargo_info),
               sg.Tab('Noon report', noon_rep)]])],

    sg.ChangeLookAndFeel('SystemDefault')
    # Create the Window
    layout = [[sg.Frame('Mandatory Data', general_info)],
              [sg.Button('Submit'),
               sg.Button('Create reports'),
               sg.Button('Quit')],
              [sg.Column(column, scrollable=True, vertical_scroll_only=True)]]



    window = sg.Window('report_creator', resizable=True).Layout(layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Quit'):  # if user closes window or clicks quit
            break
        if event == 'Calculate':
            time_local = datetime(int(values['local_time_year']), int(values['local_time_month']), int(values['local_time_day']),
                                  int(values['local_time_hour']), int(values['local_time_minute']))
            time_utc = time_local - timedelta(hours=float(values['tz']))
            eta_lt = datetime(int(values['eta_lt_year']), int(values['eta_lt_month']), int(values['eta_lt_day']),
                              int(values['eta_lt_hour']), int(values['eta_lt_minute']))
            eta_utc = eta_lt - timedelta(hours=float(values['dest_tz']))
            if last_event is None:
                time_from_last_seconds = hour_notation_to_seconds(values['time_from_last'])
                voy_time_seconds = time_from_last_seconds
                voy_dist = float(values['gps_dist'])
                voy_log_dist = float(values['log'])
                rem_dist = float(values['rem_dist']) if values['rem_dist'] != '' else 0
                avg_gps_spd = voy_dist / (time_from_last_seconds / 3600)
                avg_log_spd = voy_log_dist / (time_from_last_seconds / 3600)
            else:
                time_from_last_seconds = (time_utc - parser.parse(last_event[3])).total_seconds()
                last_voy_time = hour_notation_to_seconds(last_event[5])
                voy_time_seconds = time_from_last_seconds + last_voy_time

                voy_dist = check_float_value_present(values['gps_dist']) + float(last_event[6]) if values['gps_dist'] != '' else float(last_event[6])

                voy_log_dist = check_float_value_present(values['log']) + float(last_event[7]) if values['log'] != '' else float(last_event[7])

                rem_dist = round(float(last_event[4]) - check_float_value_present(values['gps_dist']))

                avg_gps_spd = round(check_float_value_present(values['gps_dist']) / (time_from_last_seconds / 3600), 2)
                avg_log_spd = round(check_float_value_present(values['log']) / (time_from_last_seconds / 3600), 2)

            voy_avg_spd = round(voy_dist / (voy_time_seconds / 3600), 2)

            time_from_last_display = seconds_to_hour_notation(time_from_last_seconds)

            voy_time_display = seconds_to_hour_notation(voy_time_seconds)

            current = round((avg_gps_spd - avg_log_spd), 2)

            wind_kts = check_int_value_present(values['wind_force'])
            if wind_kts < 1:
                wind_b = 0
            elif 1 <= wind_kts <= 3:
                wind_b = 1
            elif 4 <= wind_kts <= 6:
                wind_b = 2
            elif 7 <= wind_kts <= 10:
                wind_b = 3
            elif 11 <= wind_kts <= 16:
                wind_b = 4
            elif 17 <= wind_kts <= 21:
                wind_b = 5
            elif 22 <= wind_kts <= 27:
                wind_b = 6
            elif 28 <= wind_kts <= 33:
                wind_b = 7
            elif 34 <= wind_kts <= 40:
                wind_b = 8
            elif 41 <= wind_kts <= 47:
                wind_b = 9
            elif 48 <= wind_kts <= 55:
                wind_b = 10
            elif 56 <= wind_kts <= 63:
                wind_b = 11
            elif wind_kts <= 64:
                wind_b = 12
            else:
                wind_b = 0

            time_rem_hrs = rem_dist / avg_gps_spd if avg_gps_spd != 0 else 0
            real_eta = time_utc + timedelta(hours=(time_rem_hrs + float(values['dest_tz'])))
            time_to_eta = eta_utc - time_utc
            speed_req = rem_dist / (time_to_eta.total_seconds() / 3600)



            hfo_rob = check_float_value_present(values['HFOROB'])
            mdo_rob = check_float_value_present(values['MDOROB'])
            me_hfo_cons = check_float_value_present(values['MEHFOCONS'])
            me_mdo_cons = check_float_value_present(values['MEMDOCONS'])
            aux_hfo_cons = check_float_value_present(values['AUXHFOCONS'])
            aux_mdo_cons = check_float_value_present(values['AUXMDOCONS'])
            boiler_hfo_cons = check_float_value_present(values['BOILERHFOCONS'])
            boiler_mdo_cons = check_float_value_present(values['BOILERMDOCONS'])
            total_hfo_cons = check_float_value_present(values['TOTALHFOCONS'])
            total_mdo_cons = check_float_value_present(values['TOTALMDOCONS'])
            lo_cyl_cons = check_int_value_present(values['LOCYLCONS'])
            lo_me_cons = check_int_value_present(values['LOMECONS'])
            lo_aux_cons = check_int_value_present(values['LOAUXCONS'])
            lo_total_cons = check_int_value_present(values['TOTALLOCONS'])
            rpm = check_float_value_present(values['RPM'])
            me_dist = check_float_value_present(values['MEDIST'])
            me_spd = check_float_value_present(values['MESPD'])
            me_kw = check_float_value_present(values['MEKW'])
            me_kwh = check_float_value_present(values['MEKWH'])
            aux_kw = check_float_value_present(values['AUXKW'])
            aux_kwh = check_float_value_present(values['AUXKWH'])

            slip = percentage(values['SLIP'])

            me_load = percentage(values['MELOAD'])

            me_gov = percentage(values['MEGOV'])

            window.Element('time_from_last').Update(time_from_last_display)
            window.Element('avg_gps_spd').Update(avg_gps_spd)
            window.Element('avg_log_spd').Update(avg_log_spd)
            window.Element('current').Update(current)
            window.Element('voy_time').Update(voy_time_display)
            window.Element('voy_dist').Update(voy_dist)
            window.Element('voy_avg_spd').Update(voy_avg_spd)
            window.Element('voy_log_dist').Update(voy_log_dist)
            window.Element('rem_dist').Update(rem_dist)
            window.Element('real_eta').Update(real_eta.strftime('%Y-%m-%d %H:%M'))
            window.Element('wind_b').Update(wind_b)
            window.Element('speed_req').Update(round(speed_req, 2))
        if event == 'Submit':
            user_dict = {
                '~VOY~': values['voy'],
                '~EVENT~': values['event'],
                '~LOCATION~': values['location'],
                '~TIMELOCAL~': time_local.strftime('%Y-%m-%d %H:%M'),
                '~TZ~': values['tz'],
                '~TIMEUTC~': time_utc.strftime('%Y-%m-%d %H:%M'),
                '~LAT~': f'{values["lat_deg"]}-{values["lat_min"]}{values["lat_hemisphere"]}',
                '~LON~': f'{values["long_deg"]}-{values["long_min"]}{values["long_hemisphere"]}',
                '~COURSE~': values['cog'],
                '~GPSDIST~': values['gps_dist'],
                '~TIMEFROMLAST~': time_from_last_display,
                '~GPSAVGSPD~': avg_gps_spd,
                '~REMAININGDIST~': rem_dist,
                '~LOGFROMLAST~': values['log'],
                '~LOGSPDLAST~': avg_log_spd,
                '~CURRENTSPD~': current,
                '~NEXTPORT~': values['next_port'],
                '~ETATIMELOCAL~': eta_lt.strftime('%Y-%m-%d %H:%M'),
                '~ETATZ~': values['dest_tz'],
                '~ETATIMEUTC~': eta_utc.strftime('%Y-%m-%d %H:%M'),
                '~WINDDIR~': values['wind_dir'],
                '~WINDFORCEKTS~': wind_kts,
                '~WINDFORCEB~': wind_b,
                '~SEAHEIGHT~': values['sea_height'],
                '~SEADIR~': values['sea_dir'],
                '~SWELL~': values['swell'],
                '~AIRTEMP~': values['airtemp'],
                '~PRESSURE~': values['pressure'],
                '~BILGES~': values['bilges'],
                '~REMARKS~': values['remarks'],
                '~MASTER~': values['master'],
                '~VOYDIST~': voy_dist,
                '~VOYTIME~': voy_time_display,
                '~VOYGPSAVGSPD~': voy_avg_spd,
                '~VOYLOGDIST~': voy_log_dist,
                '~HFOROB~': hfo_rob,
                '~MDOROB~': mdo_rob,
                '~LOCYLROB~': int(float(values['LOCYLROB'])),
                '~LOMEROB~': int(float(values['LOMEROB'])),
                '~LOAUXROB~': int(float(values['LOAUXROB'])),
                '~LOTOTALROB~': int(float(values['LOTOTALROB'])),
                '~FWROB~': values['FWROB'],
                '~FWPROD~': values['FWPROD'],
                '~FWCONS~': values['FWCONS'],
                '~MEHFOCONS~': me_hfo_cons,
                '~MEMDOCONS~': me_mdo_cons,
                '~AUXHFOCONS~': aux_hfo_cons,
                '~AUXMDOCONS~': aux_mdo_cons,
                '~BOILERHFOCONS~': boiler_hfo_cons,
                '~BOILERMDOCONS~': boiler_mdo_cons,
                '~TOTALHFOCONS~': total_hfo_cons,
                '~TOTALMDOCONS~': total_mdo_cons,
                '~LOCYLCONS~': lo_cyl_cons,
                '~LOMECONS~': lo_me_cons,
                '~LOAUXCONS~': lo_aux_cons,
                '~TOTALLOCONS~': lo_total_cons,
                '~RPM~': rpm,
                '~MEDIST~': me_dist,
                '~MESPD~': me_spd,
                '~SLIP~': slip,
                '~MEKW~': me_kw,
                '~MEKWH~': me_kwh,
                '~MELOAD~': me_load,
                '~MEGOV~': me_gov,
                '~AUXTIME~': values['AUXTIME'],
                '~AUXKW~': aux_kw,
                '~AUXKWH~': aux_kwh,
                '~SLUDGETK~': values['SLUDGETK'],
                '~OILYBILGETK~': values['OILYBILGETK'],
                '~INCINERATORSETTLINGTK~': values['INCINERATORSETTLINGTK'],
                '~INCINERATORSERVICETK~': values['INCINERATORSERVICETK'],
                '~BILGEWATERTK~': values['BILGEWATERTK'],
                '~SLUDGETOTAL~': values['SLUDGETOTAL'],
                '~IFCARGO~': values['if_cargo'],
                '~COMMENCECARGOUTC~': f'{values["c_ops_comm_year"]}-{values["c_ops_comm_month"]}-{values["c_ops_comm_day"]} {values["c_ops_comm_hour"]}:{values["c_ops_comm_minute"]}',
                '~COMPLETEDCARGOUTC~': f'{values["c_ops_compl_year"]}-{values["c_ops_compl_month"]}-{values["c_ops_compl_day"]} {values["c_ops_compl_hour"]}:{values["c_ops_compl_minute"]}',
                '~CARGOROB~': values['cargo_rob'],
                '~CARGODAILY~': values['cargo_daily'],
                '~CARGOTOGO~': values['cargo_to_go'],
                '~BALLASTROB~': values['ballast_rob'],
                '~BALLASTDAILY~': values['ballast_daily'],
                '~SHORECRANESNO~': values['shore_cranes_no'],
                '~SHIPCRANESNO~': values['ship_cranes_no'],               
                '~ETCLOCAL~': f'{values["etc_year"]}-{values["etc_month"]}-{values["etc_day"]} {values["etc_hour"]}:{values["etc_minute"]}',
                '~ETDLOCAL~': f'{values["etd_year"]}-{values["etd_month"]}-{values["etd_day"]} {values["etd_hour"]}:{values["etd_minute"]}',

            }
            update = sg.PopupYesNo('Data ready for reports/database update. Do you want to update database?',
                                   title='Update database?')
            check_and_update_database(user_dict)
            sg.PopupOK(to_next_excel_entry(update))

        if event == 'Create reports':
            report_creation(user_dict)
    window.close()


def percentage(entry):
    if entry != '' and entry is not None:
        num_entry = float(entry)
        percent = num_entry * 100 if num_entry in range(-1, 1) else num_entry
        return round(percent)
    else:
        return 0


def check_float_value_present(value):
    if value != 0 and value != '' and value is not None:
        return round(float(value), 2)
    else:
        return 0


def check_int_value_present(value):
    if value != 0 and value != '' and value is not None:
        return round(float(value))
    else:
        return 0


def hour_notation_to_seconds(hour_string):
    hour_minutes_list = hour_string.split(':')
    return timedelta(
        hours=float(hour_minutes_list[0]) + (float(hour_minutes_list[1]) / 60)).total_seconds()


def seconds_to_hour_notation(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    return f'{int(hour)}:{str(int(minutes)).zfill(2)}'


def check_datetime_data_present(datetime_string, tz=None):
    if datetime_string != 0 and datetime_string != '' and datetime_string is not None:
        date_format = parser.parse(datetime_string)
        tz_timedelta = timedelta(hours=tz)
        date_format += tz_timedelta
        return [date_format.year, date_format.month, date_format.day, date_format.hour, date_format.minute]
    else:
        return ['', '', '', '', '']


def to_datetime(datetime_list):
    return datetime(year=int(datetime_list[0]), month=int(datetime_list[1]), day=int(datetime_list[2]),
                    hour=int(datetime_list[3]), minute=int(datetime_list[4]))


def time_read(key, time_list=None):
    time_form = [sg.Text('YYYY:', size=(6, 1)),
                 sg.InputText(time_list[0], size=(4, 1), key=f'{key}_year'),
                 sg.Text('MM:', size=(3, 1)),
                 sg.InputText(time_list[1], size=(3, 1), key=f'{key}_month'),
                 sg.Text('DD:', size=(3, 1)),
                 sg.InputText(time_list[2], size=(3, 1), key=f'{key}_day'),
                 sg.Text('HH:', size=(3, 1)),
                 sg.InputText(time_list[3], size=(3, 1), key=f'{key}_hour'),
                 sg.Text('mm:', size=(4, 1)),
                 sg.InputText(time_list[4], size=(3, 1), key=f'{key}_minute')]
    return time_form


er_excel = excel_data_source(data['FIRST_DATA'] - 1)
last_event = last_event_data()
gui_window()
