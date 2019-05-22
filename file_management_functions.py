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


def get_new_file_path(photo_date):
    """
    Get the new file path for the photo. An example would be 2019/January/31st
    :param exif_data: The list for the date that is supplied from the exif data
    :return: Array of all the new file paths
    """
    day = photo_date[0]
    month = photo_date[1]
    year = photo_date[2]
    if month == 1:
        new_month = "January"
    elif month == 2:
        new_month = "February"
    elif month == 3:
        new_month = "March"
    elif month == 4:
        new_month = "April"
    elif month == 5:
        new_month = "May"
    elif month == 6:
        new_month = "June"
    elif month == 7:
        new_month = "July"
    elif month == 8:
        new_month = "August"
    elif month == 9:
        new_month = "September"
    elif month == 10:
        new_month = "October"
    elif month == 11:
        new_month = "November"
    elif month == 12:
        new_month = "December"
    if day == 1 or day == 21 or day == 31:
        new_day = str(day) + "st"
    elif day == 2 or day == 22 or day == 2:
        new_day = str(day) + "nd"
    elif day == 23:
        new_day = str(day) + "rd"
    else:
        new_day = str(day) + "th"
    final_string = "{y}/{m}/{d}".format(y=year,m=new_month,d=new_day)
    return day


# Testing
print(get_new_file_path([22,8,2019]))
