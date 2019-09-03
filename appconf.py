# File for configuring excel read:

EXCEL_PATH = './excel/Daily report.xlsx'
EXCEL_SHEET = 'Sheet1'
DATA_GOING_DOWN = True  # State True if data is displayed in columns
FIRST_DATA = 565  # State no of first row/column of data (row if if data displayed in columns)
EVENT_LOCATION_DICT = {
    'HFOROB': 6,
    'MDOROB': 7,
    'LOCYLROB': 10,
    'LOMEROB': 11,
    'LOAUXROB': 12,
    'LOTOTALROB': 13,
    'FWROB': 14,
    #'FWPROD':  Will be taken from direct input
    #'FWCONS':  Will be taken from direct input
    'MEHFOCONS': 15,
    'MEMDOCONS': 16,
    'AUXHFOCONS': 17,
    'AUXMDOCONS':  18,
    'BOILERHFOCONS': 19,
    'BOILERMDOCONS': 20,
    'TOTALHFOCONS': 21,
    'TOTALMDOCONS': 22,
    'LOCYLCONS': 23,
    'LOMECONS': 24,
    'LOAUXCONS': 25,
    #'TOTALLOCONS': , will be validated with calculation
    'RPM': 26,
    'MEDIST': 27,
    'MESPD': 29,
    'SLIP': 31,
    'MEKW': 34,
    'MEKWH': 35,
    'MELOAD': 37,
    'MEGOV': 36,
    'AUXTIME': 46,
    'AUXKW': 48,
    'AUXKWH': 47,
    'SLUDGETK': 49,
    'OILYBILGETK': 50,
    'INCINERATORSETTLINGTK': 51,
    'INCINERATORSERVICETK': 52,
    'BILGEWATERTK': 53,
    'SLUDGETOTAL': 54
    
}
