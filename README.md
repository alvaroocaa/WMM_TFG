
# WMM_TFG
WWM code for statistical analysis for TFC **Assessing the use of True North for aeronautical navigation**

## Use of the code

In Functons folder there are the following files: **TO BE UPDATED AS NEW FUNCTIONS ARE CREATED**
* **Database.py:** Calls SQL database of 9300 airports and creates an Excel file with it
* **File_cration.py:** Creates the input file for the *wmm_file.exe* executable with the information in the Excel file created with the Database
* **wmm_file_function.py:** Calls the *wmm_file.exe* with the specific files created for it

All these functions are called in the correct order in the **Main.py**, directory_wmm needs to be adjusted where the folder is saved for each user
