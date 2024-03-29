import pandas as pd
import matplotlib.pyplot as plt
import numpy as np     
import cartopy.crs as ccrs

def mag_angle_var(Excel_file):
    
    values = pd.read_excel(Excel_file)
    
    #---------------------------------------------------------------------------------------- PER CONTINENTS
    
    continents = values['Continent'].tolist()
    magentic_variation_minutesxyear = values['dD_min'].tolist()
    
    sum_per_continent = {continent: 0 for continent in set(continents)}
    count_per_continent = {continent: 0 for continent in set(continents)}
    
    # Iterate through each value and accumulate the sum and count (of dD/year) per continent
    for continent, minutes in zip(continents, magentic_variation_minutesxyear):
        sum_per_continent[continent] += minutes
        count_per_continent[continent] += 1
        
    # Calculate the average for each continent
    average_per_continent = {continent: (sum_per_continent[continent]/60)/ count_per_continent[continent] for continent in set(continents)}

    print(average_per_continent)
    
    continents = list(average_per_continent.keys())
    averages = list(average_per_continent.values()) 
    
    # Create bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(continents, averages, color='skyblue')
    plt.title('Average Magnetic Variation (º) per year by continent')
    plt.xlabel('Continent')
    plt.ylabel('Average Magnetic Variation (º)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    #---------------------------------------------------------------------------------------- PER MAGZONES
    
    magzones = values['MagZones'].tolist()
        
    sum_per_magzone = {magzone: 0 for magzone in set(magzones)}
    count_per_magzone = {magzone: 0 for magzone in set(magzones)}
        
    # Iterate through each value and accumulate the sum and count (of dD/year) per magzone
    for magzone, minutes in zip(magzones, magentic_variation_minutesxyear):
        sum_per_magzone[magzone] += minutes
        count_per_magzone[magzone] += 1
        
    # Calculate the average for each magzone
    average_per_magzone = {magzone: (sum_per_magzone[magzone]/60)/ count_per_magzone[magzone] for magzone in set(magzones)}
    
    print(average_per_magzone)
    
    magzones = list(average_per_magzone.keys())
    averages = list(average_per_magzone.values()) 
    
    # Create bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(magzones, averages, color='skyblue')
    plt.title('Average Magnetic Variation (º) per year by magnetic zone')
    plt.xlabel('Magnetic Zone')
    plt.ylabel('Average Magnetic Variation (º)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    #---------------------------------------------------------------------------------------- PLOT MAP WITH GRADIENT
    
    IATA_codes = values['iata_code'].tolist()
    latitudes = values['Latitude'].tolist()
    longitudes = values['Longitude'].tolist()
    magvars = [value / 60 for value in values['dD_min'].tolist()]
    
    places = []

    # Iterate over the lists simultaneously and construct the matrix
    for iata, lat, lon, magvar in zip(IATA_codes, latitudes, longitudes, magvars):  
        row = [iata, lat, lon, magvar]
        places.append(row)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())
    
    sc = ax.scatter(longitudes, latitudes, c=magvars, cmap='magma', transform=ccrs.PlateCarree(), edgecolors='k')
    cbar = plt.colorbar(sc)
    cbar.set_label('Magnetic Variation (deg)')
              
    ax.coastlines()
    
    ax.gridlines()
    plt.title('Magnetic Variation')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    
    plt.show()
    