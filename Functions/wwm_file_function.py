import subprocess
import os

def wwm_file_call(input_file, output_file, directory):

    command = "wmm_file.exe f e " + input_file + " " + output_file

    os.chdir(directory)

    process = subprocess.run(command)

