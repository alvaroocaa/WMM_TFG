import pandas as pd
import matplotlib.pyplot as plt
import numpy as np     
import cartopy.crs as ccrs
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

def plots(Excel_file):
    
    values = pd.read_excel(Excel_file, engine='openpyxl')
    
    #---------------------------------------------------------------------------------------- PER CONTINENTS
    
    continents = values['continent'].tolist()
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
    
    #Create bar plot
    plt.figure(figsize=(10, 6))
    plt.rc('font', family='Times New Roman', size=14)
    plt.bar(continents, averages, color='skyblue', edgecolor='black')
    plt.title('Average Magnetic Variation (º) per Year by continent', fontsize=18, fontweight='bold')
    plt.xlabel('Continent', fontsize=16)
    plt.ylabel('Average Magnetic Variation (º)', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('average_continent_variation.png', dpi=300, bbox_inches='tight')
    
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
    plt.rc('font', family='Times New Roman', size=14)
    plt.bar(magzones, averages, colormap='skyblue', edgecolor='black')
    plt.title('Average Magnetic Variation (º) per Year by Magnetic Zone', fontsize=18, fontweight='bold')
    plt.xlabel('Magnetic Zone', fontsize=16)
    plt.ylabel('Average Magnetic Variation (º)', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('average_magzone_variation.png', dpi=300, bbox_inches='tight')

    #------------------------------------------------------------------------------------- PLOT MAP WITH GRADIENT OF ANNUAL RATE (º/year)
   
    latitudes = values['Latitude'].tolist()
    longitudes = values['Longitude'].tolist()
    magvars = [value / 60 for value in values['dD_min'].tolist()]

    fig = plt.figure(figsize=(100, 75))  # Increase figure size
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Adjust marker size
    marker_size = 50

    sc = ax.scatter(longitudes, latitudes, s=marker_size, c=magvars, cmap='Paired',
                    transform=ccrs.PlateCarree(), edgecolors='k')

    cbar = plt.colorbar(sc)
    cbar.set_label('Magnetic Variation (deg)')

    ax.coastlines()

    plt.title('Magnetic Variation')

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('MagVar.png', dpi=300, bbox_inches='tight')
    
    #------------------------------------------------------------------------------------- PLOT MAP WITH CHANGE + / -

    fig2 = plt.figure(figsize=(15, 10))  # Reduced figure size for better fitting in a thesis
    ax2 = fig2.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    colors = ['red' if var < 0 else 'blue' for var in magvars]

 
    ax2.scatter(longitudes, latitudes, s=marker_size, c=colors,
                transform=ccrs.PlateCarree(), edgecolors='k')

 
    legend_handles = [
        mpatches.Patch(color='red', label='Negative'),
        mpatches.Patch(color='blue', label='Positive')
    ]


    plt.legend(handles=legend_handles, fontsize=14, loc='upper right')

    plt.title('Magnetic Variation: Positive and Negative', fontsize=18, fontweight='bold')
    plt.xlabel('Longitude', fontsize=16)
    plt.ylabel('Latitude', fontsize=16)

    ax2.coastlines()
    ax2.set_xticks([])
    ax2.set_yticks([])
    plt.savefig('magvar_sign_thesis.png', dpi=300, bbox_inches='tight')

    plt.show()
