import requests
import pandas as pd


def map_to_dataframe(dictionary):
    return pd.DataFrame.from_dict(dictionary)


def get_main_categories(token):
    try:
        url = "https://api.allegro.pl/sale/categories"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        main_categories_result = (requests.get(url, headers=headers, verify=False)).json()
        main_categories_result = map_to_dataframe(main_categories_result)

        return main_categories_result
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
