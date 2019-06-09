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
        raise "Can't "

    current_time = datetime.datetime.now()
    dict_to_load = {"Operating System": current_os,
                    "Ran Before:": False,
                    "Run Times:": 0,
                    "Last run:": current_time
                    }
    with open("settings.json", "w") as settings_json:
        json.dump(dict_to_load, settings_json)


def update_settings():
    """
    Will update the user's settings
    :return: none
    """

