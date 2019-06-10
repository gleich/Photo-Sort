import json
from platform import platform
import datetime

def init_settings():
    """
    Will initialize the setting for a user
    :return: none
    """
    current_os = platform()
    if "windows" in current_os.lower() or "linux" in current_os.lower():
        raise Exception("This program doesn't work on Linux or Windows")
    current_time = datetime.datetime.now()
    list_to_load = [
        "Operating System:",
        current_os,
        "Ran Before:",
        False,
        "Times Ran:",
        0,
        "Last Run:",
        current_time
    ]
    with open("settings.json", "w") as settings_json:
        json.dump(list_to_load, settings_json)


def update_settings():
    """
    Will update the user's settings
    :return: none
    """
    current_os = platform()
    if "windows" in current_os.lower() or "linux" in current_os.lower():
        raise Exception("This program doesn't work on Linux or Windows")
    current_time = datetime.datetime.now()
    with open("settings.json", "r") as settings_json:
        loaded_list = json.load(settings_json)
    list_copy = [
        "Operating System:",
         current_os,
        "Ran Before:",
        True,
        "Times Ran:",
        loaded_list[6] + 1,
        "Last Run:",
        current_time
    ]
    with open("settings.json", "w") as settings_json:
        json.dump(list_copy, settings_json)

