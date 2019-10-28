import os
import os.path
import datetime
from excel_process import data


def txt_file_creation(to_whom, message):
    timestamp = datetime.datetime.now()  # only temporary, need to take date of the actual event.
    naming = to_whom + " " + " report.txt"
    filename = timestamp.strftime("%Y-%m-%d " + naming)
    filename_with_path = os.path.join(data['REPORT_OUTPUT_DIRECTORY'], filename)
    with open(filename_with_path, "w") as myfileresult:
        myfileresult.write(message)


def template_text_file_read(file_path, event_dict):
    with open(file_path, 'r') as file_buffer:
        filedata = file_buffer.read()
    for key in event_dict:
        filedata = filedata.replace(key, str(event_dict[key]))
    return filedata


def report_creation(event_dict):
    for filename in os.listdir(data['TEMPLATE_DIRECTORY']):
        txt_file_creation(f'{filename}'[:-4], template_text_file_read(f'{data["TEMPLATE_DIRECTORY"]}{filename}', event_dict))
