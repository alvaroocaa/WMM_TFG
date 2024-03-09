import subprocess
import os

def wmm_file_call(input_file, output_file, directory):

    command = "wmm_file.exe f " + input_file + " " + output_file

    os.chdir(directory)

    process = subprocess.run(command)

