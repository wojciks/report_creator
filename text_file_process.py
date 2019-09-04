import os
import os.path
import datetime
from excel_process import excel_data_source
from appconf import FIRST_DATA, TEMPLATE_DIRECTORY, REPORT_OUTPUT_DIRECTORY
from user_input import nav_data


def txt_file_creation(to_whom, which_event, message):
    timestamp = datetime.datetime.now()  # only temporary, need to take date od the actual event.
    naming = to_whom + " " + which_event + " report "
    filename = timestamp.strftime(naming + "%Y-%m-%d.txt")
    filename_with_path = os.path.join(REPORT_OUTPUT_DIRECTORY, filename)
    with open(filename_with_path, "w") as myfileresult:
        myfileresult.write(message)
    myfileresult.close()


def template_text_file_read(file_path):
    with open(file_path, 'r') as file_buffer:
        filedata = file_buffer.read()
    for key in DICTIONARY:
        filedata = filedata.replace(key, str(DICTIONARY[key]))
    return filedata


def merge_two_dicts(dict1, dict2):
    z = dict1.copy()
    z.update(dict2)
    return z


DICTIONARY = merge_two_dicts(excel_data_source(FIRST_DATA), nav_data())

for filename in os.listdir(TEMPLATE_DIRECTORY):
    txt_file_creation(f'{filename}'[:-4], DICTIONARY['~EVENT~'],template_text_file_read(f'{TEMPLATE_DIRECTORY}{filename}'))

