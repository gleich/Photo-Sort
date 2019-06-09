import photo_functions as PF
import file_management_functions as FMF
import utility_functions as UF
from termcolor import colored


def main():
    """
    Runs main
    """
    file_types = FMF.pre_import_file_types()
    print()
    UF.clear_output(50)
    question_items = ["Where is the folder you wanna sort?", "1. External Drive", "2. Folder", "3. Folder on External Drive\n---------------------------------\n"]
    UF.clear_output(50)
    question = "\n".join(question_items)
    while True:
        drive_or_folder = input(question)
        if "folder" in drive_or_folder.lower() and "drive" in drive_or_folder.lower():
            FMF.cd_into_drive()
            FMF.cd_into_folder(False)
            break
        elif "folder" in drive_or_folder.lower():
            FMF.cd_into_folder(True)
            break
        elif "drive" in drive_or_folder.lower():
            FMF.cd_into_drive()
            break
        else:
            UF.print_colored("Please pick a valid option!", "red")
            continue
    image_paths = PF.list_image_paths(file_types)
    UF.clear_output(50)
    for image in image_paths:
        print("Found:", image)
    UF.print_colored("Found " + str(len(image_paths)) + " image paths", 'green')
    UF.clear_output(10)
    exif_data = PF.photo_exif_data(image_paths)
    for file in exif_data:
        file_name = file["File Name"]
        print("Got the exif data for:", file_name)
    UF.print_colored("Found exif data for " + str(len(exif_data)) + " photos", "green")
    UF.clear_output(10)
    created_folders = FMF.init_folders(exif_data)
    for folder in created_folders:
        print("Created the folder:", folder)
    UF.print_colored("Created " + str(len(created_folders)) + " folders", "green")
    UF.clear_output(10)
    question_parts = ["Are you sure that you wanna move all the photos into the folders?", colored("WARNING:", "red", attrs=['bold', 'blink']), "1. If you quit the program now, you will need to run the program again by running python main.py in terminal.", "2. The folders were already created, so you will need to run the command to just put the photos in folders.", "Answer with y or n\n"]
    UF.clear_output(50)
    UF.print_colored("Created " + str(len(created_folders)) + " folders", "green")
    UF.print_colored("Found exif data for " + str(len(exif_data)) + " photos", "green")
    UF.print_colored("Found " + str(len(image_paths)) + " image paths", 'green')
    print("")
    continue_question = input("\n".join(question_parts))
    if "y" in continue_question.lower():
        duplicate_amount = FMF.put_photos_in_folders(exif_data)
        UF.print_colored("Found " + str(duplicate_amount) + " Duplicates", "green")
        UF.print_colored("All the photos were moved into their folders", 'green')
    elif "n" in continue_question.lower():
        UF.clear_output(10)
        print(colored("The photos were not put in the folders.", 'yellow', attrs=['bold', 'blink']))


main()
