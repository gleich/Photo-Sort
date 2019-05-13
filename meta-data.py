import subprocess
import json


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
    command = shell_command.split(" ")
    command_ran = subprocess.run(command, capture_output=get_output)
    return command_ran


# Testing:
# print(run_command("find . -type f", True))
# Testing with get_subprocess_output:
# print(get_subprocess_output(run_command("find . -type f", True)))


def list_image_paths():
    """
    Will list all the photos in the current directory and in all subdirectories.
    :return: array of the photo paths
    """
    files = []
    with open("supported_file_types.json") as supported_file_types:
        file_types = json.load(supported_file_types)
        print(file_types)
        for extenstion in file_types:
            command_to_run = "find . -iname '*." + extenstion + "'"
            ran_command = run_command(command_to_run, True)
            command_output = get_subprocess_output(ran_command)
            file_paths = command_output.split("\n")
            for file in file_paths:
                files.append(file)


# Testing
list_image_paths()
