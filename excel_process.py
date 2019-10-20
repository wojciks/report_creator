import xlrd
import json

with open('appconf.json') as json_data_file:
    data = json.load(json_data_file)


def excel_data_source(where_first_data):
    file = data['EXCEL_PATH']
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(data['EXCEL_SHEET'])
    excel_data = {
        f'~{key}~': str(single_cell_data_read((where_first_data, data['EVENT_LOCATION_DICT'][key]), worksheet)) for key
        in data['EVENT_LOCATION_DICT']}
    return excel_data


def single_cell_data_read(data_loc, worksheet):
    if data['DATA_GOING_DOWN']:
        return worksheet.cell(data_loc[0], data_loc[1]).value
    else:
        return worksheet.cell(data_loc[1], data_loc[0]).value


def to_next_excel_entry(reports_ok):
    if reports_ok == 'Yes':
        data['FIRST_DATA'] += 1
        with open('appconf.json', 'w') as outfile:
            json.dump(data, outfile)
        return f'Database updated! Next excel entry is no {data["FIRST_DATA"]}!'
    else:
        return f'Database not updated! You are still at excel entry no {data["FIRST_DATA"]}!'