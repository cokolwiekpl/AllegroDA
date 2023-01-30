import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def prepare_df():
    df = pd.read_csv('resources/ecommerce_data.csv')
    df['Order ID'] = df['Order ID'].astype(str)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Aging'] = df['Aging'].astype(str).astype(float)
    df['Ship Mode'] = df['Ship Mode'].astype(str)
    df['Product Category'] = df['Product Category'].astype(str)
    df['Product'] = df['Product'].astype(str)
    df['Sales'] = df['Sales'].replace(['0.xf'], '123')
    df['Sales'] = df['Sales'].astype(str).replace('[\$,]', '', regex=True).astype(float)
    df['Quantity'] = df['Quantity'].replace(['abc'], '12')
    df['Quantity'] = df['Quantity'].astype(str).replace('[\$,]', '', regex=True).astype(float)
    df['Profit'] = df['Profit'].astype(str).replace('[\$,]', '', regex=True).astype(float)
    df['Shipping Cost'] = df['Shipping Cost'].replace(['test'], '24.9')
    df['Shipping Cost'] = df['Shipping Cost'].astype(str).replace('[\$,]', '', regex=True).astype(float)
    df['Order Priority'] = df['Order Priority'].astype(str)
    df['Customer ID'] = df['Customer ID'].astype(str)
    df['Segment'] = df['Segment'].astype(str)
    df['City'] = df['City'].astype(str)
    df['State'] = df['State'].astype(str)
    df['Country'] = df['Country'].astype(str)
    df['Region'] = df['Region'].astype(str)
    df['Months'] = df['Months'].astype(str)

    df.drop(['Customer Name'], axis=1)
    df.dropna()

    df['Order year'] = df['Order Date']
    df['Order year'] = pd.to_datetime(df['Order year'])
    df['Order year'] = df['Order year'].dt.strftime('%Y')
    df['Quarter'] = df['Order Date'].dt.to_period('Q')

    df.sort_values(by='Order Date', inplace=True)

    return df

def create_image(df, plot_title, xlabel, ylabel, plot_file_name):
    df.groupby(df['Quarter'])['Order ID'].count().plot(kind="bar", title=plot_title)
    plt.xticks(rotation=30, horizontalalignment="center")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(plot_file_name)

def generate_plots():
    pass