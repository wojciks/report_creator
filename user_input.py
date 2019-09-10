from datetime import datetime, timedelta


def nav_data():

    user_dict = {  # {f'~{key}~': input(f'Insert data for {key}: ') for key in USER_DATA_ENTRY_FIELDS}
    '~VOY~': '325',
    '~EVENT~': 'NOONS',
    '~LOCATION~': 'AT SEA',
    '~TIMELOCAL~': datetime(2019, 9, 6, 10, 24),
    '~TZ~': '2',
    '~LAT~': '50-04.9N',
    '~LON~': '019-55.2E',
    '~GPSDIST~': '250',
    '~TIMEFROMLAST~': '24',
    '~REMAININGDIST~': '3300',
    '~LOGFROMLAST~': '230',
    '~POBTIMELOCAL~': '2019-09-06 08:24',
    '~POFFTIMELOCAL~': '2019-09-06 10:24',
    '~NEXTPORT~': 'SG  SIN',
    '~ETATIMELOCAL~': '2019-09-30 10:00',
    '~ETATZ~': '8',
    '~WINDDIR~': 'SSW',
    '~WINDFORCEKTS~': '15',
    '~SEAHEIGHT~': '0.5',
    '~SEADIR~': 'SSW',
    '~SWELL~': '0.5',
    '~BILGES~': 'DRY',
    '~REMARKS~': 'No remarks',
    '~MASTER~': 'Jan Kowalski'}

    user_dict['~GPSAVGSPD~'] = float(user_dict['~GPSDIST~']) / float(user_dict['~TIMEFROMLAST~'])

    user_dict['~TIMEUTC~'] = user_dict['~TIMELOCAL~'] - timedelta(hours=int(user_dict['~TZ~']))
    user_dict['~TIMEUTC~'] = user_dict['~TIMEUTC~'].strftime("%Y-%m-%d %H:%M")
    user_dict['~TIMELOCAL~'] = user_dict['~TIMELOCAL~'].strftime("%Y-%m-%d %H:%M")

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
