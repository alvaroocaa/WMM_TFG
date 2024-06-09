import pandas as pd

def input_file(excel_file_path):

    excel_database = pd.read_excel(excel_file_path, sheet_name="Sheet1")
    
    input_file_txt = open("input_file.txt", "w")
    
    for index, row in excel_database.iterrows():
                
        input_file_txt.write(
            "2024.0 " + # Date: xxxx.xxx for decimal  (2023.7)
            "M " + # Altitude: M - Above mean sea level: E above WGS84 Ellipsoid
            "M" + str(row['elevation_ft']) + " " + # Altitude: Kxxxxxx.xxx for kilometers  (K1000.13), Mxxxxxx.xxx for meters  (m1389.24), Fxxxxxx.xxx for feet  (F192133.73)
            str(row['latitude_deg']) + " " + str(row['longitude_deg']) # Lat/Lon: xxx.xxx in decimal  (-76.53) (Lat and Lon must be specified in the same format.)
            + "\n"
        )
    
    input_file_txt.close()
    
def input_file_multi(excel_file_path):

    excel_database = pd.read_excel(excel_file_path, sheet_name="Sheet1")
    
    years = ['2020.0', '2021.0', '2022.0', '2023.0', '2024.0']
    
    input_file_txt = open("input_file_multi.txt", "w")
    
    for x in years:
        
        for index, row in excel_database.iterrows():
                
            input_file_txt.write(
                x + " " + # Date: xxxx.xxx for decimal  (2023.7)
                "M " + # Altitude: M - Above mean sea level: E above WGS84 Ellipsoid
                "M" + str(row['elevation_ft']) + " " + # Altitude: Kxxxxxx.xxx for kilometers  (K1000.13), Mxxxxxx.xxx for meters  (m1389.24), Fxxxxxx.xxx for feet  (F192133.73)
                str(row['latitude_deg']) + " " + str(row['longitude_deg']) # Lat/Lon: xxx.xxx in decimal  (-76.53) (Lat and Lon must be specified in the same format.)
                + "\n"
            )

    input_file_txt.close()