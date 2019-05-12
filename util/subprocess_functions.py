import subprocess


def get_subprocess_output(shell_command):
    """
    Will get the output of a subprocess command that has been ran.
    :param shell_command: the command that was recorded.
    :return: the command's output
    """

    return complete_output


# Testing:
command = str((subprocess.run(['ls'], capture_output=True)))
print(command)
print(get_subprocess_output(command))
