from Functions.Database import call_database
from Functions.wmm_file_function import wmm_file_call
from Functions.File_creation import input_file
from Functions.output_analysis import wmm_file_analysis

directory_wmm = "C:/Users/Alvaro/Documents/Uni/8e quadri/TFG/Codi/WMM_TFG"

#call_database()
input_file("airports from SQL.xlsx")
wmm_file_call("input_file.txt", "output_file.txt", directory_wmm)
average_magvar_degreesxyear = wmm_file_analysis("output_file.txt", "analysis file.xlsx")

print(average_magvar_degreesxyear)