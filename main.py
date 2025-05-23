import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Import data
def import_data():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    return df

# Clean data
def clean_data(df):
    # Calculate quantiles
    bottom_quantile = df['value'].quantile(0.025)
    top_quantile = df['value'].quantile(0.975)
    
    # Filter out outliers
    df_clean = df[(df['value'] >= bottom_quantile) & (df['value'] <= top_quantile)]
    return df_clean

# Draw line plot
def draw_line_plot():
    df = import_data()
    df_clean = clean_data(df)
    
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df_clean.index, df_clean['value'], color='r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.savefig('line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    df = import_data()
    df_clean = clean_data(df)
    
    # Prepare data for bar plot
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Order months correctly
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)
    
    # Group and calculate mean
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    fig.savefig('bar_plot.png')
    return fig

# Draw box plot
def draw_box_plot():
    df = import_data()
    df_clean = clean_data(df)
    
    # Prepare data for box plots
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    
    # Order months correctly
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    fig.savefig('box_plot.png')
    return fig
