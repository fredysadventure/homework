import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Import the data
df = pd.read_csv('medical_examination.csv')

# Task 2: Add overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)

# Task 3: Normalize data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Task 4: Draw Categorical Plot
def draw_cat_plot():
    # Task 5: Create DataFrame for cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Task 6: Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat.rename(columns={'size': 'total'}, inplace=True)
    
    # Task 7: Draw the catplot
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )
    
    # Task 8: Get the figure
    fig = g.fig
    
    # Task 9: Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Task 10: Draw Heat Map
def draw_heat_map():
    # Task 11: Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Task 12: Calculate the correlation matrix
    corr = df_heat.corr()

    # Task 13: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Task 14: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Task 15: Plot the correlation matrix
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={'shrink': 0.5}
    )

    # Task 16: Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
