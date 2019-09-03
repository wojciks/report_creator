import datetime
from excel_process import excel_data_source
from appconf import DATA_GOING_DOWN, FIRST_DATA, EXCEL_PATH, EXCEL_SHEET, EVENT_LOCATION_DICT


voy = 325
event = "NOON"
location = "At sea"
captain = "ION BUCUR"
to_whom = 'Charterer'

DICTIONARY = {
    '~VOY~': voy,
    '~EVENT~': event,
    '~LOCATION~': location,
    '~MASTER~': captain
}


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def txt_file_creation(to_whom, which_event, message):
    timestamp = datetime.datetime.now()  # only temporary, need to take date od the actual event.
    naming = to_whom + " " + which_event + " report "
    filename = timestamp.strftime(naming + "%Y-%m-%d.txt")
    with open(filename, "w") as myfileresult:
        myfileresult.write(message)
    myfileresult.close()


def template_text_file_read(file_path):
    with open(file_path, 'r') as file_buffer:
        filedata = file_buffer.read()
    for key in DICTIONARY:
        filedata = filedata.replace(key, str(DICTIONARY[key]))
    return filedata


DICTIONARY = merge_two_dicts(DICTIONARY, excel_data_source(FIRST_DATA))

txt_file_creation(to_whom, event,
                  template_text_file_read('./reps_example/CHARTERER_EXAMPLE.txt'))
