# WMM_TFG

WWM (World Magnetic Model) code for statistical analysis for TFG **Assessing the use of True North for aeronautical navigation**

## Code organization


* **Functions:** This folder contains all the functions that are called in the **Main.py**
    * **Database.py:** This file includes the function that calls and cleans the *SQLite* database and loads all the data into an Excel spreadsheet to treat later and visualize all the data
    * **File_creation.py:** This file includes the function that creates the file that will be entered into the *WMM* software which provides for a date, elevation, and coordinates of each airport
    * **wmm_file_creation.py:** This file includes the function that makes the call to the *WMM* software and passes it to the input file
    * **output_analysis.py:** This file includes the function that created a joined Excel spreadsheet with the airport data and the *WMM* software results for a better analysis adding the magnetic area column based on the airport's coordinates
    * **Computations.py:** This file includes the function that plots all of the figures contained in the Results folder

* **Necessary files:** This folder contains all the necessary files for the code to be executed (Databases, output files, input files, and spreadsheets)

* **Results:** This folder contains all the plots resulting from the code as *.png* files

* **WMM2020_Windows:** This folder contains the software distributed by WMM valid from 2020 to 2025



