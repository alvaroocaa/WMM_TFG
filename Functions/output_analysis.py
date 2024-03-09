import pandas as pd
import openpyxl

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
'''



def wmm_file_analysis(file_path, output_path):
    
    df = pd.read_csv(file_path, delim_whitespace=True)
    df.to_excel(output_path, index = False)
    
    # Computation of interesting values
    
    magentic_variation_minutesxyear = df['dD_min'].tolist()
    magentic_variation_degreesxyear = [x / 60 for x in magentic_variation_minutesxyear]
    
    average_magvar_degreesxyear = sum(magentic_variation_degreesxyear) / len(magentic_variation_degreesxyear)
    
    return average_magvar_degreesxyear