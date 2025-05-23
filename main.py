import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')
    
    # First line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = np.arange(1880, 2051)
    plt.plot(years_extended1, res1.intercept + res1.slope*years_extended1, 
             'r', label='Best Fit Line (1880-2013)')
    
    # Second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = np.arange(2000, 2051)
    plt.plot(years_extended2, res2.intercept + res2.slope*years_extended2, 
             'green', label='Best Fit Line (2000-2013)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
