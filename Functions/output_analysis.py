import pandas as pd
import pycountry_convert as pc
import xlsxwriter

def wmm_file_analysis(file_path, output_path, Data_excel_path):
    
    #Format output as excel
    
    analysis_excel = pd.read_csv(file_path, delim_whitespace=True)
    
    Data_excel = pd.read_excel(Data_excel_path, index_col=None, usecols="B:K", engine='openpyxl')
    
    analysis_excel = pd.concat([analysis_excel, Data_excel], axis=1)                               
                               
    analysis_excel.to_excel(output_path, index = False)
    
    Latitudes = pd.read_excel(output_path, index_col=None, usecols="E", engine='openpyxl').values.flatten()
    
    MagZones = country_to_magzone(Latitudes)
    
    analysis_excel['MagZones'] = MagZones
    
    analysis_excel.to_excel(output_path, index = False)


#Function to organize by coordinates: North Magnetic Pole, South Magnetic Pole and Magnetic Equator
def country_to_magzone(latitude_vector):
    
    magzone_vector = []
    
    for latitude in latitude_vector:
            
        if latitude < -64:
            magzone = "South Magnetic Pole"
            
        elif latitude > 67:
            magzone = "North Magnetic Pole"
            
        else:
            magzone = "Magnetic Equator"
    
        magzone_vector.append(magzone)
        
    return magzone_vector

