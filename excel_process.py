import xlrd
from appconf import DATA_GOING_DOWN, FIRST_DATA, EXCEL_PATH, EXCEL_SHEET, EVENT_LOCATION_DICT


def excel_data_source(where_first_data):
    file = EXCEL_PATH  # need to fix the global var here...
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(EXCEL_SHEET)
    excel_data = {
        f'~{key}~': str(single_cell_data_read((where_first_data, EVENT_LOCATION_DICT[key]), worksheet)) for key in
        EVENT_LOCATION_DICT}
    return excel_data


def single_cell_data_read(data_loc, worksheet):
    if DATA_GOING_DOWN:  # need to fix the global var here...
        return worksheet.cell(data_loc[0], data_loc[1]).value
    else:
        return worksheet.cell(data_loc[1], data_loc[0]).value
