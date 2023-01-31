from typing import Union

import requests
import pandas as pd
import urllib3.exceptions
from allegro_api_reader.api_authoriser import check_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def map_to_dataframe(dictionary: dict, orient_param: str) -> pd.DataFrame:
    return pd.DataFrame.from_dict(dictionary, orient=orient_param)


def return_data_by_endpoint_params(data, return_data_type: str, df_orient_param: str = "columns") -> Union[pd.DataFrame, dict]:
    """
    This function returns either a Pandas DataFrame or a dictionary, depending on the value of the "return_data_type"
    parameter. If the value of "return_data_type" is "df", the data is converted to a DataFrame using the
    map_to_dataframe function and the "df_orient_param" parameter, which specifies the orientation of the data in
    the DataFrame. If the value of "return_data_type" is "dict", the data is returned as a dictionary. If the value of
    "return_data_type" is neither "df" nor "dict", a ValueError is raised.

    Args:
        data: The data to be returned in either a DataFrame or dictionary format.
        return_data_type (str): The desired format for the returned data. Must be either "df" or "dict".
        df_orient_param (str, optional): The orientation of the data in the DataFrame. Default value is "columns".

    Returns:
        Union[pd.DataFrame, dict]: The data in either a DataFrame or dictionary format, depending on the value of
                                    the "return_data_type" parameter.

    Raises:
        ValueError: If the value of "return_data_type" is not "df" or "dict".
    """
    if return_data_type == "df":
        return map_to_dataframe(data, df_orient_param)
    elif return_data_type == "dict":
        return data
    else:
        raise ValueError("Invalid value for return_data_type")


def do_request_get_on_endpoint(url: str) -> dict:
    """
     Make a GET request to the specified endpoint with authorization header.

     Parameters:
     url (str): The URL endpoint to be accessed.

     Returns:
     dict: The response of the GET request as a dictionary.
     """
    token = check_token()
    headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
    return (requests.get(url, headers=headers, verify=False)).json()


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoriesUsingGET
def get_all_categories(return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        categories_dict = do_request_get_on_endpoint("https://api.allegro.pl/sale/categories")
        return return_data_by_endpoint_params(categories_dict, return_data_type, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoryUsingGET_1
def get_category_details_by_category_id(category_id, return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        category_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/categories/{category_id}")
        return return_data_by_endpoint_params(category_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getFlatProductParametersUsingGET
def get_product_parameters_by_category_id(category_id, return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        product_parameters_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/categories/{category_id}/product-parameters")
        return return_data_by_endpoint_params(product_parameters_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoryUsingGET_1
def get_category_parameters_by_category_id(category_id, return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        category_parameters_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/categories/{category_id}/parameters")
        return return_data_by_endpoint_params(category_parameters_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/searchOffersUsingGET
# Endpoint only works on offers made by the user himself.
def get_all_sellers_offers(return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        offers_dict = do_request_get_on_endpoint("https://api.allegro.pl/sale/offers")
        return return_data_by_endpoint_params(offers_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getSaleProducts
def get_search_products_results(keyword: str, language: str = "pl - PL", mode: str = "", return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        products_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/products?phrase={keyword}&language={language}&mode={mode}")
        return return_data_by_endpoint_params(products_dict, return_data_type, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getSaleProduct
def get_product_data_by_product_id(product_id: str, language: str = "pl - PL", category: str = "", return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        product_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/products/{product_id}?language={language}&category.id+{category}")
        return return_data_by_endpoint_params(product_dict, return_data_type, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/listSellerPromotionsUsingGET_1
def get_user_list_of_promotions(return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        promotions_dict = do_request_get_on_endpoint("https://api.allegro.pl/sale/loyalty/promotions?")
        return return_data_by_endpoint_params(promotions_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getPromotionUsingGET
def get_promotion_data_by_promotion_id(promotion_id, return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        promotion_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/sale/loyalty/promotions/{promotion_id}")
        return return_data_by_endpoint_params(promotion_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getListOfOrdersUsingGET
# Endpoint only works if user is seller.
def get_users_orders(return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        orders_dict = do_request_get_on_endpoint("https://api.allegro.pl/order/checkout-forms")
        return return_data_by_endpoint_params(orders_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getOrdersDetailsUsingGET
# Endpoint only works if user is seller.
def get_order_data_by_order_id(order_id, return_data_type: str = "dict") -> Union[pd.DataFrame, dict]:
    try:
        order_dict = do_request_get_on_endpoint(f"https://api.allegro.pl/order/checkout-forms/{order_id}")
        return return_data_by_endpoint_params(order_dict, return_data_type)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
