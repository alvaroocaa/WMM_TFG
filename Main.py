from Functions.Database import call_database
from Functions.File_creation import input_file
from Functions.wmm_file_function import wmm_file_call
from Functions.output_analysis import wmm_file_analysis
from Functions.Computations import plots
    
directory_wmm = "/Users/alvaro/Documents/Uni/TFG"

Data_excel = "airports from SQL.xlsx"

#call_database()
#input_file("airports from SQL.xlsx")
#wmm_file_call("input_file.txt", "output_file.txt", "/Users/Alvaro/Documents/Uni/8e quadri/TFG/Codi/WMM_TFG")
wmm_file_analysis("output_file.txt", "analysis file.xlsx", "airports from SQL.xlsx")
plots("analysis file.xlsx")