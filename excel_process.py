import xlrd
import json

with open('appconf.json') as json_data_file:
    data = json.load(json_data_file)


def excel_data_source(where_first_data):
    file = data['EXCEL_PATH']  # need to fix the global var here...
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(data['EXCEL_SHEET'])
    excel_data = {
        f'~{key}~': str(single_cell_data_read((where_first_data, data['EVENT_LOCATION_DICT'][key]), worksheet)) for key
        in data['EVENT_LOCATION_DICT']}
    return excel_data


def single_cell_data_read(data_loc, worksheet):
    if data['DATA_GOING_DOWN']:  # need to fix the global var here...
        return worksheet.cell(data_loc[0], data_loc[1]).value
    else:
        return worksheet.cell(data_loc[1], data_loc[0]).value
