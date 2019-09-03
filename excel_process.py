import xlrd
from appconf import DATA_GOING_DOWN, FIRST_DATA, EXCEL_PATH, EXCEL_SHEET, EVENT_LOCATION_DICT


def excel_data_source(where_first_data):
    file = EXCEL_PATH  # need to fix the global var here...
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(EXCEL_SHEET)
    excel_data = {
        '~HFOROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['HFOROB']), worksheet)),
        '~MDOROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MDOROB']), worksheet)),
        '~LOCYLROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOCYLROB']), worksheet)),
        '~LOMEROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOMEROB']), worksheet)),
        '~LOAUXROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOAUXROB']), worksheet)),
        '~LOTOTALROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOTOTALROB']), worksheet)),
        '~FWROB~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['FWROB']), worksheet)),
        # '~FWPROD~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['FWPROD']), worksheet)),
        # '~FWCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['FWCONS']), worksheet)),
        '~MEHFOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEHFOCONS']), worksheet)),
        '~MEMDOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEMDOCONS']), worksheet)),
        '~AUXHFOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['AUXHFOCONS']), worksheet)),
        '~AUXMDOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['AUXMDOCONS']), worksheet)),
        '~BOILERHFOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['BOILERHFOCONS']), worksheet)),
        '~BOILERMDOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['BOILERMDOCONS']), worksheet)),
        '~TOTALHFOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['TOTALHFOCONS']), worksheet)),
        '~TOTALMDOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['TOTALMDOCONS']), worksheet)),
        '~LOCYLCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOCYLCONS']), worksheet)),
        '~LOMECONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOMECONS']), worksheet)),
        '~LOAUXCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['LOAUXCONS']), worksheet)),
        # '~TOTALLOCONS~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['TOTALLOCONS']), worksheet)),
        '~RPM~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['RPM']), worksheet)),
        '~MEDIST~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEDIST']), worksheet)),
        '~MESPD~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MESPD']), worksheet)),
        '~SLIP~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['SLIP']), worksheet)),
        '~MEKW~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEKW']), worksheet)),
        '~MEKWH~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEKWH']), worksheet)),
        '~MELOAD~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MELOAD']), worksheet)),
        '~MEGOV~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['MEGOV']), worksheet)),
        '~AUXTIME~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['AUXTIME']), worksheet)),
        '~AUXKW~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['AUXKW']), worksheet)),
        '~AUXKWH~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['AUXKWH']), worksheet)),
        '~SLUDGETK~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['SLUDGETK']), worksheet)),
        '~OILYBILGETK~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['OILYBILGETK']), worksheet)),
        '~INCINERATORSETTLINGTK~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['INCINERATORSETTLINGTK']), worksheet)),
        '~INCINERATORSERVICETK~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['INCINERATORSERVICETK']), worksheet)),
        '~BILGEWATERTK~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['BILGEWATERTK']), worksheet)),
        '~SLUDGETOTAL~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT['SLUDGETOTAL']), worksheet)),
    }
    return excel_data


def single_cell_data_read(data_loc, worksheet):
    if DATA_GOING_DOWN:  # need to fix the global var here...
        return worksheet.cell(data_loc[0], data_loc[1]).value
    else:
        return worksheet.cell(data_loc[1], data_loc[0]).value

