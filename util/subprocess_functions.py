import subprocess


def get_subprocess_output(shell_command):
    """
    Will get the output of a subprocess command that has been ran.
    :param shell_command: the command that was recorded.
    :return: the command's output
    """
    string_command = str(shell_command)
    stdout_position = string_command.find("stdout")
    stderr_position = string_command.find("stderr")
    relative_string = string_command[stdout_position:stderr_position]
    final_string = relative_string[relative_string.find("'") + 1:-3]
    return final_string


# Testing:
# command = str((subprocess.run(['pwd'], capture_output=True)))
# print(command)
# print(get_subprocess_output(command))
