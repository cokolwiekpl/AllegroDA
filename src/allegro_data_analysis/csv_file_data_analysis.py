import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

MONTH_DICT = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


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


def create_plot(title: str, xlabel: str, ylabel: str, plot_file_name: str):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f"resources/plots/{plot_file_name}")
    plt.clf()


def create_plot_by_order_id(data_frame: pd.DataFrame, group_by, plot_title: str, xlabel: str, ylabel: str, plot_file_name: str):
    """
    Create a bar plot of count of order IDs grouped by a given column.

    Parameters:
    data_frame (DataFrame): The data frame containing the sales data.
    group_by (str): The column to group the data by.
    plot_title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    plot_file_name (str): The name of the file to save the plot to.
    """
    data_frame.groupby(data_frame[group_by])['Order ID'].count().plot(kind="bar", title=plot_title)
    plt.xticks(rotation=30, horizontalalignment="center")
    create_plot(plot_title, xlabel, ylabel, plot_file_name)


def create_plot_of_country_profits(data_frame: pd.DataFrame, top_or_bottom_countries: str, plot_title: str, plot_file_name: str):
    """
    Create a bar plot of the total profits of top or bottom 10 countries.
    Parameters:
    data_frame (pandas.DataFrame): DataFrame containing the sales data.
    top_or_bottom_countries (str): Indicator to show either top or bottom 10 countries.
    plot_title (str): The title for the plot.
    plot_file_name (str): The name of the file to save the plot.
    """
    if top_or_bottom_countries == "top":
        countries_list = (data_frame.groupby("Country")["Profit"].sum().reset_index()).nlargest(10, "Profit")["Country"].tolist()
    elif top_or_bottom_countries == "bottom":
        countries_list = (data_frame.groupby("Country")["Profit"].sum().reset_index()).nsmallest(10, "Profit")["Country"].tolist()

    countries_data = data_frame[data_frame["Country"].isin(countries_list)].copy()

    table = countries_data.pivot_table(index="Months", columns="Country", values="Profit", aggfunc=sum)
    plt.figure(figsize=(80, 50))

    table.plot(kind="bar", subplots=True, layout=(5, 2), title=plot_title)
    plt.xlabel("Miesiąc")
    plt.ylabel("Dochód")
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)
    plt.savefig(f"resources/plots/{plot_file_name}")
    plt.clf()


def create_plot_by_category(data_frame: pd.DataFrame, category: str, plot_file_name: str):
    """
    Create plot of profit for a given product category.

    Parameters:
    data_frame (pandas.DataFrame): The data frame containing the data.
    category (str): The category of the product to plot.
    plot_file_name (str): The name of the file to save the plot to.
    """
    df_cat = data_frame.loc[data_frame['Product Category'] == category]
    df_cat_grouped = df_cat[['Months', 'Profit']].groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: MONTH_DICT[x]))
    df_cat_grouped.reset_index(inplace=True)

    title = f"Dochód z sprzedaży produktów z kategorii '{category}'"
    sns.lineplot(x='Months', y='Profit', data=df_cat_grouped).set(title=title, xlabel="Miesiąc", ylabel="Dochód")
    plt.savefig(f"resources/plots/{plot_file_name}")
    plt.clf()


def create_correlation_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    corr = data_frame.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(data_frame.corr(), mask=mask, annot=True, center=0, linewidths=.5, square=True, vmin=-0.15, vmax=0.3, fmt='0.1f').set(title=plot_title)
    plt.savefig(f"resources/plots/{plot_file_name}")
    plt.clf()


def create_linear_regression_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    sns.regplot(x='Shipping Cost', y='Profit', data=data_frame).set(title=plot_title)
    plt.savefig(f"resources/plots/{plot_file_name}")
    plt.clf()


def create_sales_and_monthly_income_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    df_sales_profit = data_frame[['Months', 'Sales', 'Profit']]
    df_sales_profit.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: MONTH_DICT[x])).plot.bar()
    create_plot(plot_title, "Miesiąc", "Dochód w $", plot_file_name)


def create_revenue_customer_segment_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    df_segment = data_frame[['Segment', 'Profit']]
    df_segment.groupby(['Segment'])['Profit'].count().plot(kind="bar", title=plot_title)
    plt.xticks(horizontalalignment="center")
    create_plot(plot_title, "Segment", "Dochód w $", plot_file_name)


def create_average_waiting_time_in_month_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    sns.boxplot(x="Months", y="Aging", data=data_frame)
    create_plot(plot_title, "Miesiąc", "Ilość dni", plot_file_name)


def create_income_generated_by_segments_plot(data_frame: pd.DataFrame, plot_title: str, plot_file_name: str):
    df_segment = data_frame.sort_values('Months', key=lambda x: x.apply(lambda x: MONTH_DICT[x]))[['Months', 'Segment', 'Profit']]
    sns.histplot(data=df_segment, x="Months", hue="Segment", multiple="stack").set(title=plot_title, xlabel='Miesiąc', ylabel='Dochód')
    plt.savefig(f'resources/plots/{plot_file_name}')
    plt.clf()


def generate_plots():
    """
    This code generates plots based on data from a dataframe df which is prepared from a function prepare_df().
    The code creates several plots of various aspects of the data, such as total orders per quarter, total orders per month,
    total orders by product category, monthly profits by top and bottom countries, and monthly sales vs profits.
    It also creates plots based on different customer segments and order aging.
    The plots are saved in various image files using the savefig method.
    """

    df = prepare_df()

    create_plot_by_order_id(df, 'Quarter', "Ilość zamówień w danym kwartale", "Kwartał", "Zamówienia", 'ZamowieniaKwartal.png')
    create_plot_by_order_id(df, 'Months', "Ilość zamówień w danym miesiącu na skale globaln", "Miesiąc", "Zamówienia", 'zamowieniaMiesiac.png')
    create_plot_by_order_id(df, 'Product Category', "Ilość produktów z poszczególnej kategorii", "Kategoria produktu", "Ilość zamówień", 'zamowieniaKategorie.png')

    create_plot_of_country_profits(df, "top", "Miesięczny dochów w 2015 w 10 krajach o największym dochodzie", 'najwiekszyDochod.png')
    create_plot_of_country_profits(df, "bottom", "Miesięczny dochów w 2015 w 10 krajach o najmniejszym dochodzie", 'najmniejszyDochod.png')

    create_plot_by_category(df, "Auto & Accessories", 'dochodSamochod.png')
    create_plot_by_category(df, "Home & Furniture", 'dochodDom.png')
    create_plot_by_category(df, "Fashion", 'dochodMods.png')
    create_plot_by_category(df, "Electronic", 'dochodelektornika.png')

    create_correlation_plot(df, "Korelacja pomiędzy zmiennymi ilościowymi", "korelacja.png")
    create_linear_regression_plot(df, "Dopasowanie 'Profit' i 'Shipping Cost' do modelu regresji liniowej", "proftCostReg.png")
    create_sales_and_monthly_income_plot(df, "Sprzedaż i dochód miesięczny", "sprzedazDochod.png")
    create_revenue_customer_segment_plot(df, "Przychod dla danego semgmentu klientów", "dochodSegment.png")
    create_average_waiting_time_in_month_plot(df, "Średni czas oczekiwania zamówienia na wysyłkę w danym miesiącu", "sredniaAgign.png")
    create_income_generated_by_segments_plot(df, "Dochód generowany przez poszczególne segmnety", "segmentyHistohram.png")
