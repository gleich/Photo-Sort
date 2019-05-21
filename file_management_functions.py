import os
import time
import json
import photo_functions as PF


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


def get_date_info(exif_array):
    """
    Will get all the infermation for the folder names (dates)
    :param exif_array: The list of dictonraries that contains the exif data for each photos
    :return: array of information
    """
    years = []
    date_info = {}
    for photo in exif_array:
        creation_info = photo["Creation Date"]
        year = creation_info[2]
        if year not in years:
            years.append(year)
    for year in years:
        date_info[year] = {}
    for photo in exif_array:
        creation_info = photo["Creation Date"]
        month = creation_info[1]
        year = creation_info[2]
        if month not in date_info[year].keys():
            current_layer = date_info[year]
            current_layer[month] = []
    for photo in exif_array:
        creation_info = photo["Creation Date"]
        day = creation_info[0]
        month = creation_info[1]
        year = creation_info[2]
        set_year = date_info[year]
        set_month = set_year[month]
        if day not in set_month:
            set_month.append(day)
    return date_info

# Testing
print(PF.photo_exif_data(PF.list_image_paths(pre_import_file_types())))
