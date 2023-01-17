import requests
import pandas as pd


def map_to_dataframe(dict_test):
    return pd.DataFrame.from_dict(dict_test)


def get_main_categories(token):
    try:
        url = "https://api.allegro.pl/sale/categories"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        main_categories_result = requests.get(url, headers=headers, verify=False)
        main_categories_result = main_categories_result.json()
        df = map_to_dataframe(main_categories_result)
        print(type(main_categories_result))
        print(type(df))

        return main_categories_result
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
