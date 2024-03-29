from Functions.Database import call_database
from Functions.wmm_file_function import wmm_file_call
from Functions.File_creation import input_file
from Functions.output_analysis import wmm_file_analysis
from Functions.Computations import mag_angle_var
    
directory_wmm = "C:/Users/Alvaro/Documents/Uni/8e quadri/TFG/Codi/WMM_TFG"

Data_excel = "airports from SQL.xlsx"

call_database()
input_file(Data_excel)
wmm_file_call("input_file.txt", "output_file.txt", directory_wmm)
wmm_file_analysis("output_file.txt", "analysis file.xlsx", Data_excel)
mag_angle_var("analysis file.xlsx")


