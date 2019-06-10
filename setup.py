from platform import platform
import datetime

def update_settings():
    """
    Will write the settings for a user
    :return: none
    """
    current_os = platform()
    current_time = datetime.datetime.now()
    if "windows" in current_os.lower() or "linux" in current_os.lower():
        raise Exception("This program is not supported for your Operating System.")
    with open("settings.txt", "w") as settings_file:
        settings_file.write("Operating system: " + current_os)
        settings_file.write("Ran before: " + str(True))
        settings_file.write("Last Run Time: " + str(current_time))


def setup_requirements():
    """
    Will install and setup decencies
    :return:
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




