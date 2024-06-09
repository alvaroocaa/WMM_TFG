import pandas as pd
import pycountry_convert as pc
import xlsxwriter
from pyexcelerate import Workbook

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
    
def wmm_file_analysis_multi(file_path, output_path, Data_excel_path):
    
    #Format output as excel
    
    analysis_excel = pd.read_csv(file_path, delim_whitespace=True)
    
    Data_excel = pd.read_excel(Data_excel_path, index_col=None, usecols="A:K", engine='openpyxl')
    data_excel_repeated = pd.concat([Data_excel]*4, ignore_index=True)
    
    analysis_excel = pd.concat([analysis_excel, data_excel_repeated], axis=1)  

    
    analysis_excel = analysis_excel.sort_values(by=['Date', 'Id'])
    #analysis_excel['VAR_min'] = analysis_excel.groupby('Id')['dD_min'].transform(lambda x: x.diff())       
    #analysis_excel['VAR_min'] = analysis_excel.groupby('Id')['dD_min'].diff()         

    data = [analysis_excel.columns.tolist()] + analysis_excel.values.tolist()
    wb = Workbook()
    wb.new_sheet('Sheet1', data=data)
    wb.save(output_path)
                               
    #analysis_excel.to_excel(output_path, index = False, engine='xlsxwriter')
    
    #Latitudes = pd.read_excel(output_path, index_col=None, usecols="E", engine='openpyxl').values.flatten()
    
    MagZones = country_to_magzone(analysis_excel['latitude_deg'])
    
    analysis_excel['MagZones'] = MagZones
    
    analysis_excel.to_excel(output_path, index = False, engine='xlsxwriter')



#Function to organize by coordinates: North Magnetic Pole, South Magnetic Pole and Magnetic Equator
def country_to_magzone(latitude_vector):
    
    magzone_vector = []
    
    for latitude in latitude_vector:
            
        if latitude < -64:
            magzone = "South Magnetic Pole"
            
        elif latitude > 67:
            magzone = "North Magentic Pole"
            
        else:
            magzone = "Magnetic Equator"
    
        magzone_vector.append(magzone)
        
    return magzone_vector

