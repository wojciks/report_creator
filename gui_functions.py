import PySimpleGUI as sg
from datetime import datetime, timedelta
from dateutil import parser


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
        return int(round(float(value)))
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


def time_read(key, time_list):
    if time_list is None:
        time_list = [''] * 5
    return [sg.Text('YYYY:', size=(6, 1)),
            sg.InputText(time_list[0], size=(4, 1), key=f'{key}_year'),
            sg.Text('MM:', size=(3, 1)),
            sg.InputText(time_list[1], size=(3, 1), key=f'{key}_month'),
            sg.Text('DD:', size=(3, 1)),
            sg.InputText(time_list[2], size=(3, 1), key=f'{key}_day'),
            sg.Text('HH:', size=(3, 1)),
            sg.InputText(time_list[3], size=(3, 1), key=f'{key}_hour'),
            sg.Text('mm:', size=(4, 1)),
            sg.InputText(time_list[4], size=(3, 1), key=f'{key}_minute')]


def form_to_datetime(year, month, day, hour, minute):
    if year and month and day and hour and minute != '':
        return datetime(check_int_value_present(year),
                        check_int_value_present(month),
                        check_int_value_present(day),
                        check_int_value_present(hour),
                        check_int_value_present(minute))
    else:
        return ''


def if_date_present(value):
    if type(value) != datetime:
        return ''
    else:
        return value.strftime('%Y-%m-%d %H:%M')


def geoposition_split(geoposition):
    split_position = str(geoposition).split('-')
    return {'degrees': split_position[0], 'minutes': split_position[1][:-1], 'hemisphere': split_position[1][-1]}
