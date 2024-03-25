import pandas as pd
import pycountry_convert as pc

'''
Output_file format: (+ description of each element)

** The vertical direction is perpendicular to the WGS 84 ellipsoid model of the Earth, the 
horizontal plane is perpendicular to the vertical direction, and the rotational directions clockwise and 
counter-clockwise are determined by a view from above

Date -> date computed in decimal (between 2020.0 and 2025.0)
MSL - Ellipsoid -> indication of altitude, Mean Sea Level or Ellipsoid (WGS84)
Depth(m) ->  depth of the ocean below the survey vessel
Latitude -> latitude (days and minutes)
Longitude -> longitude (days and minutes)
D_deg -> declination angle (degrees) (also called the magnetic variation and measured clockwise from true north to the horizontal component of the field vector)
D_min -> declination angle (minutes) (also called the magnetic variation and measured clockwise from true north to the horizontal component of the field vector)
I_deg -> inclination angle (degrees) (also called the dip angle and measured from the horizontal plane to the field vector, positive downwards)
I_min -> inclination angle (minutes) (also called the dip angle and measured from the horizontal plane to the field vector, positive downwards)
H_nT -> horizontal intensity (nano Teslas)
X_nT -> northerly intensity (nano Teslas)
Y_nT -> easterly intensity (nano Teslas
Z_nT -> vertical intensity (nano Teslas) (positive downwards)
F_nT -> TOTAL intensity (nano Teslas)

-- Variations / year
dD_min -> variation declination angle (minutes / year) (also called the magnetic variation and measured clockwise from true north to the horizontal component of the field vector)
dI_min -> variation inclination angle (minutes / year) (also called the dip angle and measured from the horizontal plane to the field vector, positive downwards)
dX_nT ->horizontal intensity (nano Teslas / year)
dX_nT -> northerly intensity (nano Teslas / year)
dY_nT -> easterly intensity (nano Teslas / year)
dZ_nT -> vertical intensity (nano Teslas / year) (positive downwards)
dF_nT -> TOTAL intensity (nano Teslas / year)

---------------- Additionally to have uncertainty values appended to the output file add the "e" flag or "Errors"
δD_min ->
δI_min ->
δH_nT ->
δX_nT ->
δY_nT ->
δZ_nT ->
δF_nT ->

-----------------------------------------

Filtrar aeroports

Dividir en continents -> Buscar llibreria que a partir dels paisos per poder separar en continents
Regions aeronautiques -> FIRs, intentar buscar base de dades també per tenir classificació + aeronautica


'''



def wmm_file_analysis(file_path, output_path, Data_excel_path):
    
    #Format output as excel
    
    analysis_excel = pd.read_csv(file_path, delim_whitespace=True)
    
    Data_excel = pd.read_excel(Data_excel_path, index_col=None, na_values=['NA'], usecols="B:F")
    
    analysis_excel = pd.concat([analysis_excel, Data_excel], axis=1)                               
                               
    analysis_excel.to_excel(output_path, index = False)
    
    #Create a new column to filter by contintent
    
    Countries = pd.read_excel(output_path, index_col=None, na_values=['NA'], usecols="Z").values.flatten()
    
    #Control error for bad written countries:
    
    countries = switch_country(Countries)
    
    Continents = country_to_continent(countries)
    
    analysis_excel['Continent'] = Continents
    
    analysis_excel.to_excel(output_path, index = False)


#Function to get the continent given a country name to add a column to the excel with the continent name to filter the analysis
def country_to_continent(country_name_vector):
    
    continent_vector = []
    
    for country in country_name_vector:
        
        try:
            
            country_alpha2 = pc.country_name_to_country_alpha2(country, cn_name_format="upper")
            country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
            country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
            continent_vector.append(country_continent_name)
            
        except Exception as e:
            continent_vector.append("")
            
            
    return continent_vector

def switch_country(argument_list):
    switcher = {
        "UK": "Great Britain",
        "ENGLAND": "Great Britain",
        "NORTH IRELAND": "IRELAND",
        "WALES": "Great Britain",
        "GUERNSEY ISLD.": "Great Britain",
        "SCOTLAND": "Great Britain",
        "CANARY ISLANDS": "SPAIN",
        "ACORES": "Portugal",
        "CENTRAL AFRICAN REP.": "SUDAN",
        "DIEGO GARCIA ISLAND": "SUDAN",
        "COMOROS ISLANDS": "SUDAN",
        "MAYOTTE ISLAND": "SUDAN",
        "REUNION ISLAND": "SUDAN",
        "SAO TOME & PRINCIPE": "SUDAN",
        "ZAIRE": "SUDAN",
        "SPANISH NORTH AFRICA": "MOROCCO",
        "GUINEA BISSAU": "SUDAN",
        "CAPE VERDE ISLANDS": "SUDAN",
        "CORSE ISL.": "ITALY",
        "ST. PIERRE & MIQUELON": "CANADA",
        "MADEIRA": "PORTUGAL",
        "BOSNIA-HERCEGOVINA": "SUDAN",
        "FORMER MACEDONIA": "GREECE",
        "YUGOSLAVIA": "Serbia",
        "TURKS & CAICOS I.": "DOMINICAN REPUBLIC",
        "TUVALU I.": "AUSTRALIA",
        "TUVALU ISLAND": "AUSTRALIA",
        "WALLIS & FUTUNA": "AUSTRALIA",
        "TUAMOTU ISLANDS": "AUSTRALIA",
        "PHOENIX ISL.": "AUSTRALIA",
        "MARIANA ISLANDS": "PHILIPPINES",
        "JOHNSTON ATOLL": "MEXICO",
        "MIDWAY ISLAND": "USA",
        "PALAU ISLAND": "INDONESIA",
        "KOREA": "SOUTH KOREA",
        "ANTARCTICA": "USA",
        "GALAPAGOS I. (ECUADOR": "ECUADOR",
        "SURINAM": "BRAZIL",
        "ANTILLES": "DOMINICAN REPUBLIC",
        "VIRGIN ISL.": "PUERTO RICO",
        "ST. KITTS & NEVIS": "PUERTO RICO",
        "ANGUILLA ISL.": "PUERTO RICO",
        "MONTSERRAT ISLAND": "PUERTO RICO",
        "TRINIDAD & TOBAGO": "VENEZUELA",
        "ST.VINCENT/GRENADINES": "VENEZUELA",
        "EAST TIMOR": "INDONESIA",
        "WEST TIMOR": "INDONESIA",
        "ENGALND": "GREAT BRITAIN",
        "FAROE ISL.": "NORWAY",
        "LUXEMBURG": "LUXEMBOURG",
        "BOPHUTHATSWANA": "BOTSWANA", 
        "FRENCH GUYANA": "BRAZIL",
        "LEEWARD ISLANDS": "BRAZIL",
        "ST. LUCIA ISLAND": "DOMINICAN REPUBLIC" 
    }
    return [switcher.get(country, country) for country in argument_list]


