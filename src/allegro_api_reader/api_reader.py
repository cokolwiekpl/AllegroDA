import requests
import pandas as pd


def map_to_dataframe(dictionary):
    return pd.DataFrame.from_dict(dictionary)


def get_all_categories(token):
    try:
        url = "https://api.allegro.pl/sale/categories"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        categories_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(categories_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_all_sellers_offers(token):
    try:
        url = "https://api.allegro.pl/sale/categories"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        offers_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(offers_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
