from appconf import USER_DATA_ENTRY_FIELDS


def nav_data():
    user_dict = {f'~{key}~': input(f'Insert data for {key}: ') for key in USER_DATA_ENTRY_FIELDS}
    return user_dict
