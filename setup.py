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
        settings_file.write("Operating system: " + current_os + "\n")
        settings_file.write("Ran before: " + str(True) + "\n")
        settings_file.write("Last Run Time: " + str(current_time) + "\n")



# Testing:
# update_settings()
