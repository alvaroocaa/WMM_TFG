import pandas as pd
import matplotlib.pyplot as plt

def mag_angle_var(Excel_file):
    
    values = pd.read_excel(Excel_file)
    
    continents = values['Continent'].tolist()
    magentic_variation_minutesxyear = values['dD_min'].tolist()
    
    sum_per_continent = {continent: 0 for continent in set(continents)}
    count_per_continent = {continent: 0 for continent in set(continents)}
    
    # Iterate through each value and accumulate the sum and count per continent
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
    plt.title('Average Magnetic Variation Minutes per Year by Continent')
    plt.xlabel('Continent')
    plt.ylabel('Average Magnetic Variation Minutes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    