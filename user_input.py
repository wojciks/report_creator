from datetime import datetime, timedelta
from dateutil import parser
from gui import data_from_gui
from history_process import voyage_distance_time_avg_speed, last_event_data
import sqlite3


def nav_data():
    last_event = last_event_data()
    voy_data = voyage_distance_time_avg_speed(sqlite3.connect('data_history.db'), data_from_gui[0])
    time_local = datetime(data_from_gui[2], data_from_gui[3], data_from_gui[4], data_from_gui[5], data_from_gui[6])
    time_utc = time_local - timedelta(hours=float(data_from_gui[7]))
    eta_time_local = datetime(data_from_gui[25], data_from_gui[26], data_from_gui[27], data_from_gui[28], data_from_gui[29])
    time_from_last = (time_utc - parser.parse(last_event[3])).total_seconds()
    latitude = f'{data_from_gui[18]}-{data_from_gui[19]}{data_from_gui[20]}'
    longitude = f'{data_from_gui[21]}-{data_from_gui[22]}{data_from_gui[23]}'
    remaining = last_event[4] - data_from_gui[17]

    user_dict = {
    '~VOY~': data_from_gui[0],
    '~EVENT~': data_from_gui[1],
    '~LOCATION~': 'AT SEA',
    '~TIMELOCAL~': time_local,
    '~TZ~': data_from_gui[7],
    '~TIMEUTC~': time_utc,
    '~LAT~': latitude,
    '~LON~': longitude,
    '~GPSDIST~': data_from_gui[17],
    '~TIMEFROMLAST~': time_from_last,
    '~REMAININGDIST~': remaining,
    '~LOGFROMLAST~': data_from_gui[16],
    '~POBTIMELOCAL~': '2019-09-06 08:24',
    '~POFFTIMELOCAL~': '2019-09-06 10:24',
    '~NEXTPORT~': data_from_gui[24],
    '~ETATIMELOCAL~': eta_time_local,
    '~ETATZ~': data_from_gui[30],
    '~WINDDIR~': data_from_gui[10],
    '~WINDFORCEKTS~': data_from_gui[11],
    '~SEAHEIGHT~': data_from_gui[12],
    '~SEADIR~': data_from_gui[13],
    '~SWELL~': data_from_gui[14],
    '~BILGES~': data_from_gui[31],
    '~REMARKS~': data_from_gui[33],
    '~MASTER~': data_from_gui[32]}

    user_dict['~GPSAVGSPD~'] = float(user_dict['~GPSDIST~']) / float(user_dict['~TIMEFROMLAST~'])

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

    return user_dict
