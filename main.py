import photo_functions as PF
import file_management_functions as FMF
import utility_functions as UF
from termcolor import colored
from platform import platform


def main():
    """
    Runs main
    """
    UF.clear_output(50)
    UF.print_txt_content("information.txt")
    print("\nDo you understand the information above?")
    continue_question = input(colored("Answer with y or n\n", "yellow", attrs=['bold']))
    if "y" in continue_question.lower():
        current_platform = platform()
        if "windows" in current_platform.lower() or "linux" in current_platform.lower():
            raise Exception("This program doesn't support Linux or Windows. It will not be able to run.")
        UF.clear_output(50)
        commands = ["Sort folder and it's sub-folders", "Sort current folder only", "Move Keep content (Not super reliable)", "Delete Remove content"]
        print("Below is a list of all the commands. Please select one.\n")
        command_number = 0
        for command in commands:
            command_number += 1
            print("{one}. {two}".format(one=command_number, two=command))
        print("")
        command_to_use = input(colored("Which of the commands shown above would you like to use?\n", "yellow", attrs=['bold'])).lower()
        if "sort" in command_to_use and "folder" in command_to_use:
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
            if "sort folder" in command_to_use and "sub-folders" in command_to_use or "1" in command_to_use:
                image_paths = PF.list_image_paths(file_types, True)
            else:
                image_paths = PF.list_image_paths(file_types, False)
                print(image_paths)
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
            question_parts = ["Are you sure that you wanna move all the photos into the folders?", colored("WARNING:", "red", attrs=['bold', 'blink']), "1. If you quit the program now, you will need to run the program again by running python main.py in terminal.", "2. ", colored("Answer with y or n\n", "yellow", attrs=["bold"])]
            UF.clear_output(50)
            print("---------------------------------")
            UF.print_colored("Created " + str(len(created_folders)) + " folders", "green")
            UF.print_colored("Found exif data for " + str(len(exif_data)) + " photos", "green")
            UF.print_colored("Found " + str(len(image_paths)) + " image paths", 'green')
            print("")
            continue_question = input("\n".join(question_parts))
            if "y" in continue_question.lower():
                duplicate_amount = FMF.put_photos_in_folders(exif_data)
                print("")
                UF.print_colored("Found " + str(duplicate_amount) + " Duplicates", "green")
                if duplicate_amount != 0:
                    UF.print_colored("All the photos were moved into their folders", 'green')
                    FMF.setup_duplicates_folder()
            elif "n" in continue_question.lower():
                UF.clear_output(10)
                print(colored("The photos were not put in the folders.", 'yellow', attrs=['bold', 'blink']))
        elif "content" in command_to_use:
            UF.clear_output(50)
            question_items = ["Where is the that you already sorted? (Not the duplicates folder)", "1. External Drive", "2. Folder", "3. Folder on External Drive\n---------------------------------\n"]
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
            UF.clear_output(50)
            if "keep" in command_to_use:
                FMF.duplicates_folder_management(True)
            else:
                FMF.duplicates_folder_management(False)
    else:
        print("The program will not run. To restart it run python main.py")

if __name__ == "__main__":
    main()
