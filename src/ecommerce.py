# %% [markdown]
# Wczytanie pliku CSV
#

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytaj dane z pliku CSV
df = pd.read_csv('ecommerce.csv')
# print(df.columns)

# %% [markdown]
#
# Zmiana typów kolumn z objektów na Stringi i Floaty oraz zamiana przypadkowych pojedyńczych wartości na bardziej racjonalne

# %%
# df['Order ID'] = df['Order ID'].astype(str)
# df['Order Date'] = pd.to_datetime(df['Order Date'])
# df['Ship Date'] = pd.to_datetime(df['Ship Date'])
# df['Aging'] = df['Aging'].astype(str).astype(float)
# df['Ship Mode'] = df['Ship Mode'].astype(str)
# df['Product Category'] = df['Product Category'].astype(str)
# df['Product'] = df['Product'].astype(str)
# df['Sales'] = df['Sales'].replace(['0.xf'], '123')
# df['Sales'] = df['Sales'].astype(str).replace('[\$,]', '', regex=True).astype(float)
# df['Quantity'] = df['Quantity'].replace(['abc'], '12')
# df['Quantity'] = df['Quantity'].astype(str).replace('[\$,]', '', regex=True).astype(float)
# df['Profit'] = df['Profit'].astype(str).replace('[\$,]', '', regex=True).astype(float)
# df['Shipping Cost'] = df['Shipping Cost'].replace(['test'], '24.9')
# df['Shipping Cost'] = df['Shipping Cost'].astype(str).replace('[\$,]', '', regex=True).astype(float)
# df['Order Priority'] = df['Order Priority'].astype(str)
# df['Customer ID'] = df['Customer ID'].astype(str)
# df['Segment'] = df['Segment'].astype(str)
# df['City'] = df['City'].astype(str)
# df['State'] = df['State'].astype(str)
# df['Country'] = df['Country'].astype(str)
# df['Region'] = df['Region'].astype(str)
# df['Months'] = df['Months'].astype(str)

# %% [markdown]
# Usunięcie niepotrzebnych kolumn oraz wierszy z wartościami NAN

# %%
# df.drop(['Customer Name'], axis=1)
# df.dropna()

# %% [markdown]
# Dodanie kolumny z rokiem zamówienia i jego kwartałem

# %%
# df['Order year'] = df['Order Date']
# df['Order year'] = pd.to_datetime(df['Order year'])
# df['Order year'] = df['Order year'].dt.strftime('%Y')
# df['Quarter'] = df['Order Date'].dt.to_period('Q')

# %% [markdown]
# Posortowanie zgodnie z datą zamówieia
#

# %%
# df.sort_values(by='Order Date', inplace=True)

# %% [markdown]
# Ilość zamówień w zależności od kwartału

# %%
df.groupby(df['Quarter'])['Order ID'].count().plot(kind="bar", title="Ilość zamówień w danym kwartale")
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Kwartał")
plt.ylabel("Zamówienia")
plt.savefig('ZamowieniaKwartal.png')

# %% [markdown]
# Ilość zamówień w danym miesiącu na skale globalną

# %%
df.groupby(df['Months'])['Order ID'].count().plot(kind="bar", title="Ilość zamówień w danym miesiącu na skale globaln")
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Miesiąc")
plt.ylabel("Zamówienia")
plt.savefig('zamowieniaMiesiac.png')

# %% [markdown]
# 10 krajów o największym przychodzie w 2015. Są to kraje które przyniosły największy dochód

# %%

# Tworzymy tabelę z profitami i krajami
countires = pd.DataFrame(df.groupby(['Country'])['Profit'].sum())

# Wybieramy 10 krajów o największym rocznym popycie, zamieniamy typ z datFrame na Serie, aby łątwiej było nam wyciągnąć listę państw
countries_with_largest_profit = countires.nlargest(10, 'Profit').squeeze()

# Tworzymy listę z nazwami tych krajów
countries_profit = list(countries_with_largest_profit.keys())

# Tworzymy nowego data frame jedynie z państwami o największych dochodzach w 2015
countires_new = pd.DataFrame()
for i in range(len(countries_profit)):
    countires_new = countires_new.append(df.loc[df['Country'] == countries_profit[i]])

# Wykresy
table = countires_new.pivot_table(index='Months', columns='Country', values='Profit', aggfunc=sum)
table.plot(figsize=(40, 25), kind='bar', subplots=True, layout=(5, 2), title="Miesięczny dochów w 2015 w 10 krajach o największym dochodzie")
plt.xlabel("Miesiąc")
plt.ylabel("Dochód")
plt.savefig('najwiekszyDochod.png')

# %% [markdown]
# Dochodzy 10 krajów o najmnijesyzm dochodzi

# %%
from tkinter import *

# Tworzymy tabelę z profitami i krajami
countires = pd.DataFrame(df.groupby(['Country'])['Profit'].sum())

# Wybieramy 10 krajów o największym rocznym popycie, zamieniamy typ z datFrame na Serie, aby łątwiej było nam wyciągnąć listę państw
countries_with_smalest_profit = countires.nsmallest(10, 'Profit').squeeze()

# Tworzymy listę z nazwami tych krajów
countries_profit = list(countries_with_smalest_profit.keys())

# Tworzymy nowego data frame jedynie z państwami o największych dochodzach w 2015
countires_new = pd.DataFrame()
for i in range(len(countries_profit)):
    countires_new = countires_new.append(df.loc[df['Country'] == countries_profit[i]])

# Wykresy
table = countires_new.pivot_table(index='Months', columns='Country', values='Profit', aggfunc=sum)
table.plot(figsize=(40, 25), kind='bar', subplots=True, layout=(5, 2), title="Miesięczny dochów w 2015 w 10 krajach o największym dochodzie")
plt.xlabel("Miesiąc")
plt.ylabel("Dochód")
plt.savefig('najmniejszyDochod.png')

# %% [markdown]
# Ilość produktów z poszczególnej kategorii

# %%

df.groupby(['Product Category'])['Order ID'].count().plot(kind="bar", title="Ilość produktów z poszczególnej kategorii")
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Kategoria produktu")
plt.ylabel("Ilość zamówień")
plt.savefig('zamowieniaKategorie.png')

# %% [markdown]
# Wielkość dochodów z spzredazy akcesoriów samochodowych

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_auto = df.loc[df['Product Category'] == "Auto & Accessories"]
df_2 = df_auto[['Months', 'Profit']]

df_2 = df_2.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))
df_2.reset_index(inplace=True)

sns.lineplot(x='Months', y='Profit', data=df_2).set(title="Dochód z sprzedaży produktów z kategori 'Samochód i Akcesoria'", xlabel="Miesiąc", ylabel="Dochód")
plt.savefig('dochodSamochod.png')

# %% [markdown]
# Wielkość dochodów z sprzedaży elektroniki

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_auto = df.loc[df['Product Category'] == "Electronic"]
df_2 = df_auto[['Months', 'Profit']]

df_2 = df_2.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))
df_2.reset_index(inplace=True)

sns.lineplot(x='Months', y='Profit', data=df_2, err_style='bars').set(title="Dochód z sprzedaży produktów z kategorii 'Elektronika'", xlabel="Miesiąc",
                                                                      ylabel="Dochód")
plt.savefig('dochodelektornika.png')

# %% [markdown]
# Wielkość dochodów z sprzedaży produktów z kategorii "Moda"

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_auto = df.loc[df['Product Category'] == "Fashion"]
df_2 = df_auto[['Months', 'Profit']]

df_2 = df_2.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))
df_2.reset_index(inplace=True)

sns.lineplot(x='Months', y='Profit', data=df_2, err_style='bars').set(title="Dochód z sprzedaży produktów z kategorii 'Moda'", xlabel="Miesiąc",
                                                                      ylabel="Dochód")
plt.savefig('dochodMods.png')

# %% [markdown]
# Wielkość dochodów z sprzedaży produktów z kategorii "Dom i wyposarzenie"

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_auto = df.loc[df['Product Category'] == "Home & Furniture"]
df_2 = df_auto[['Months', 'Profit']]

df_2 = df_2.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))
df_2.reset_index(inplace=True)

sns.lineplot(x='Months', y='Profit', data=df_2, err_style='bars').set(title="Dochód z sprzedaży produktów z kategorii 'Dom i wyposarzenie'", xlabel="Miesiąc",
                                                                      ylabel="Dochód")
plt.savefig('dochodDom.png')

# %% [markdown]
# Stosunek sprzedaży do dochodu w danym miesiącu

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_sales_profit = df[['Months', 'Sales', 'Profit']]
df_sales_profit.groupby('Months').sum().sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x])).plot.bar()

plt.title("Przyrównanie miesięcznej sprzedaży do przychodu")
plt.xlabel("Miesiąc")
plt.ylabel("$")
plt.savefig('sprzedazDochod.png')

# %% [markdown]
# Przychod dla danego semgmentu klientów

# %%
df_segment = df[['Segment', 'Profit']]
df_segment.groupby(['Segment'])['Profit'].count().plot(kind="bar", title="Przychod dla danego semgmentu klientów")
plt.xticks(horizontalalignment="center")
plt.xlabel("Segment")
plt.ylabel("Dochód w $")
plt.savefig('dochodSegment.png')

# %% [markdown]
# Hstogram dla dochodów generowanych przez poszczególne segmenty

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

df = df.sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))

df_segment = df[['Months', 'Segment', 'Profit']]
sns.histplot(data=df_segment, x="Months", hue="Segment", multiple="stack").set(title="Dochód generowany przez poszczególne segmnety", xlabel='Miesiąc',
                                                                               ylabel='Dochód')
plt.savefig('segmentyHistohram.png')

# %% [markdown]
# Średni czas oczekiwania zamówienia na wysyłkę wdanym miesiącu

# %%
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

df = df.sort_values('Months', key=lambda x: x.apply(lambda x: month_dict[x]))

sns.boxplot(x="Months",
            y="Aging",
            data=df)
plt.ylabel("Ilość dni", size=14)
plt.xlabel("Miesiąc", size=14)
plt.title("Średni czas oczekiwania zamówienia na wysyłkę wdanym miesiącu", size=18)
plt.savefig("sredniaAgign.png")




