import subprocess


#######################
#Subprocess functions:#
#######################

def get_subprocess_output(subprocess_command):
    """
    Will get the output of a subprocess command that has been ran.
    :param subprocess_command: the command that was recorded.
    :return: the command's output
    """
    string_command = str(subprocess_command)
    stdout_position = string_command.find("stdout")
    stderr_position = string_command.find("stderr")
    relative_string = string_command[stdout_position:stderr_position]
    final_string = relative_string[relative_string.find("'") + 1:-3]
    return final_string


# Testing:
# command = str((subprocess.run(['pwd'], capture_output=True)))
# print(command)
# print(get_subprocess_output(command))


def run_command(shell_command, get_output):
    """
    Will run a shell command using the subprocess module
    :param shell_command: The command that is going to be ran
    :param get_output: Will capture the output of the command
    :return: the command output
    """
    command_ran = subprocess.run(shell_command, capture_output=get_output)
    return command_ran


# Testing:
# print(run_command("find . -type f", True))
# Testing with get_subprocess_output:
# print(get_subprocess_output(run_command("pwd", True)))


def get_file_creation_data(file_path):
    """
    Finds when the photo was created. This is needed because it is not something that we get when using the exiftool.
    :param file_path:  The path of the file that the date will be gotton for.
    :return: string that says what the date of creation is for the file using the ISO format.
    """
    ran_command = run_command(["stat", file_path], True)
    command_output = get_subprocess_output(ran_command)
    return command_output


# Testing:
print(get_file_creation_data('./photos/test_image.jpg'))


#########################
#General Purpose python:#
#########################


def list_to_dict(lst):
    """
    Takes a list an turns it into a list
    :param lst: the list that will be turned into a dict
    """
    if len(lst) % 2 != 1:
        odd_indexes = []
        even_indexes = []
        for i in range(len(lst)):
            if i % 2 == 0:
                odd_indexes.append(lst[i])
            elif i % 2 == 1 or i == 0:
                even_indexes.append(lst[i])
        final_dict = dict(zip(odd_indexes, even_indexes))
        return final_dict
    else:
        print("The list needs to have an even amount of")


# Testing
# print(list_to_dict(["a", "b", "c", "d"]))


# This files is not gonna be unittested, this is due to the fact that there is no returned items.
def print_list_index(iterable_items):
    """
    Will list the indexes of all the items in a list. This is for testing.
    :param iterable_item: list or string that will be iterated through
    :return: nothing, it really just prints the items to the terminal.
    """
    if str(type(iterable_items)) == "<class 'str>":
        characters = list(iterable_items)
        for i in range(len(characters)):
            print(characters[i], ":", i)
    if str(type(iterable_items)) == "<class 'list'>":
        for i in range(len(iterable_items)):
            print(iterable_items[i], ":", i)
