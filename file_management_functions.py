import os
import time
import json


def cd_into_drive():
    """
    Will change the current directory into the directory of the drive that will be used.
    """
    project_location = os.getcwd()
    directory_layers = len(project_location.split("/"))
    command_parts = ["../"]
    for i in range(directory_layers):
        command_parts.append("../")
    path = "".join(command_parts)
    os.chdir(path)
    if "Volumes" in os.listdir():
        while True:
            os.chdir("Volumes")
            print("-------------------------------------------------------")
            drive_numbers = 0
            for drive in os.listdir():
                drive_numbers += 1
                print("Drive {drive_nums}: {item}".format(drive_nums=drive_numbers, item=drive))
            print("")
            drive_name = input("What is the drive that you wanna use?\n")
            if drive_name in os.listdir():
                os.chdir(drive_name)
                print("The program is now set to this drive:", os.getcwd())
                break
            else:
                print("That is not a valid drive. The program will restart in 5 seconds")
                time.sleep(5)
                continue
    else:
        raise Exception("Can't locate any drives")


# Testing:
# cd_into_drive()


def pre_import_file_types():
    """
    Will get the file types from the supported_file_types.json file
    :return: array of file types.
    """
    with open("supported_file_types.json") as json_file:
        file_types = json.load(json_file)
    return file_types
