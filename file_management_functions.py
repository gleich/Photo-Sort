import os
import time
import json
import utility_functions as UF


def cd_into_drive():
    """
    Will change the current directory into the directory where the files that will be sorted are.
    """
    project_location = os.getcwd()
    directory_layers = len(project_location.split("/"))
    command_parts = ["../"]
    for i in range(directory_layers):
         command_parts.append("../")
    path = "".join(command_parts)
    os.chdir(path)
    if "Volumes" in os.listdir():
        os.chdir("Volumes")
        while True:
            UF.clear_output(50)
            print("-------------------------------------------------------")
            drive_numbers = 0
            for drive in os.listdir():
                drive_numbers += 1
                print("Drive {drive_nums}: {item}".format(drive_nums=drive_numbers, item=drive))
            print("")
            drive_name = input("What is the drive that you wanna use?\n")
            if drive_name in os.listdir():
                os.chdir(drive_name)
                UF.print_colored("The program is now set to this drive:" + str(os.getcwd()), "green")
                break
            else:
                UF.print_colored("That is not a valid drive. The program will restart in 5 seconds", "red")
                time.sleep(5)
                continue


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
    :return: folders that were created
    """
    folders = []
    for photo in raw_exif_data:
        photo_folder = photo["New Path"]
        if photo_folder not in folders:
            folders.append(photo_folder)
    for folder_path in folders:
        UF.run_command(["mkdir", "-p", folder_path], False)
    UF.run_command(["mkdir", "Duplicates"], False)
    return folders


def rename_file(file_path):
    """
    Will create the string to rename a file to ./currentname_copy.file extension
    :param file_path: the current file path
    :return: new path
    """
    characters = list(file_path)
    dot_index = ''.join(characters).rindex('.')
    last_slash_index = ''.join(characters).rindex('/')
    name_section = characters[last_slash_index:dot_index]
    current_name = "".join(name_section)
    new_name = current_name + "_COPY"
    before_name = "".join(characters[0:last_slash_index])
    after_name = "".join(characters[dot_index:len(characters)])
    new_path = before_name + new_name + after_name
    return new_path


# Testing:
# print(rename_file("/Users/matthewgleich/Documents/GitHub/Get_Tempature/.idea/Get_Tempature.iml"))


def put_photos_in_folders(raw_exif_data):
    """
    Will take all the photos and put them in their folders
    :param raw_exif_data: the raw exif data
    :return: number of duplicates in put in folder
    """
    move_files = {}
    duplicate_files = []  # list of their current paths
    for file in raw_exif_data:
        file_name = file["File Name"]
        current_path = file["Current Path"]
        new_path = file["New Path"]
        if file_name not in move_files.keys():
            move_files[file_name] = [current_path, new_path]
        elif file_name in move_files.keys():
            duplicate_files.append(current_path)
            duplicate_file_orig = move_files[file_name][0]
            duplicate_file_new_path = rename_file(duplicate_file_orig)
            UF.run_command(["mv", duplicate_file_orig, duplicate_file_new_path], False)
            move_files.pop(file_name)
            duplicate_files.append(duplicate_file_new_path)
    for name, paths in move_files.items():
        current_path = paths[0]
        new_path = paths[1]
        UF.run_command(["mv", current_path, new_path], False)
    if len(duplicate_files) >= 2:
        for path in duplicate_files:
            UF.run_command(["mv", path, "./Duplicates"], False)
    return duplicate_amount


def cd_into_folder(go_to_root):
    """
    Will list the folders in the current directory and cd into the one that user chooses.
    :param go_to_root: If the program should cd up to the root (boolean)
    :return: current directory
    """
    if go_to_root:
        current_pwd = os.getcwd()
        levels = current_pwd.split("/")
        levels.pop(0)  # Removes blank space that is right before users.
        number_of_levels = len(levels) - 2  # Minus 2 because we wanna be a user root not system root.
        for i in range(number_of_levels):
            os.chdir("..")
    while True:
        UF.clear_output(50)
        command_output = os.popen("echo */").read()  # Won't work with subprocess for some strange reason
        raw_directories = command_output.split("/")
        directories = []
        current_directory = os.getcwd()
        print("The current path is:", current_directory)
        for directory in raw_directories:
            cleaned_directory = directory.strip()
            directories.append(cleaned_directory)
        for directory in directories:
            print(directory)
        folder = input("Please choose one of the folders above. If the current folder is the folder that you wanna sort, the please type *\n")
        if folder in directories:
            os.chdir(folder)
            continue
        elif folder == "*":
            UF.print_colored("The folder the program will run in is now set to" + folder, "green")
            break
        else:
            print("That is not one of the folders shown above.")
            continue
    UF.clear_output(10)
    return os.getcwd()