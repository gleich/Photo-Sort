import os
import time
import json
import utility_functions as UF


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


# Testing
# print(pre_import_file_types())


def new_file_path(photo_date):
    """
    Get the new file path for the photo. An example would be 2019/January/31st
    :param photo_date: The list for the date that is supplied from the exif data
    :return: Array of all the new file paths
    """
    if len(photo_date) == 3:
        month = photo_date[0]
        day = int(photo_date[1])
        year = int(photo_date[2])
        if day in (1, 21, 31):
            new_day = str(day) + "st"
        elif day in (2, 22):
            new_day = str(day) + "nd"
        elif day == 23:
            new_day = str(day) + "rd"
        else:
            new_day = str(day) + "th"
        final_string = "./" + str(year) + "/" + str(month) + "/" + str(month) + "-" + str(new_day)
        return final_string


# Testing
# print(new_file_path(["August",  22, 2019]))


def init_folders(raw_exif_data):
    """
    Will create all the folders in the current directory
    :param raw_exif_data: the raw exif data for all the photos.
    """
    folders = []
    for photo in raw_exif_data:
        photo_folder = photo["New Path"]
        if photo_folder not in folders:
            folders.append(photo_folder)
    for folder_path in folders:
        UF.run_command(["mkdir", "-p", folder_path], False)

