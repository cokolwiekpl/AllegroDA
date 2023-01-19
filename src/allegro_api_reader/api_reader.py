import requests
import pandas as pd
import urllib3.exceptions
from allegro_api_reader.api_authoriser import check_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def map_to_dataframe(dictionary: dict, orient_param: str = "columns"):
    return pd.DataFrame.from_dict(dictionary, orient=orient_param)


def do_get_request_on_endpoint(url: str):
    token = check_token()
    headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
    return (requests.get(url, headers=headers, verify=False)).json()


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoriesUsingGET
def get_all_categories():
    try:
        categories_dict = do_get_request_on_endpoint("https://api.allegro.pl/sale/categories")
        return map_to_dataframe(categories_dict, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoryUsingGET_1
def get_category_details_by_category_id(category_id):
    try:
        category_dict = do_get_request_on_endpoint(f"https://api.allegro.pl/sale/categories/{category_id}")
        return map_to_dataframe(category_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getFlatProductParametersUsingGET
def get_product_parameters_by_category_id(category_id):
    try:
        product_parameters_dict = do_get_request_on_endpoint(
            f"https://api.allegro.pl/sale/categories/{category_id}/product-parameters")
        return map_to_dataframe(product_parameters_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getCategoryUsingGET_1
def get_category_parameters_by_category_id(category_id):
    try:
        category_parameters_dict = do_get_request_on_endpoint(f"https://api.allegro.pl/sale/categories/{category_id}/parameters")
        return map_to_dataframe(category_parameters_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/searchOffersUsingGET
# Endpoint only works on offers made by the user himself.
def get_all_sellers_offers():
    try:
        offers_dict = do_get_request_on_endpoint("https://api.allegro.pl/sale/offers")
        return map_to_dataframe(offers_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getSaleProducts
def get_search_products_results(keyword: str, language: str = "pl - PL", mode: str = ""):
    try:
        products_dict = do_get_request_on_endpoint(f"https://api.allegro.pl/sale/products?phrase={keyword}&language={language}&mode={mode}")
        # print(products_dict)
        return map_to_dataframe(products_dict, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# Endpoint documentation: https://developer.allegro.pl/documentation#operation/getSaleProduct
def get_product_data_by_product_id(product_id: str, language: str = "pl - PL", category: str = ""):
    try:
        product_dict = do_get_request_on_endpoint(
            f"https://api.allegro.pl/sale/products/{product_id}?language={language}&category.id+{category}")
        return map_to_dataframe(product_dict, "index")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_user_list_of_promotions():
    try:
        promotions_dict = do_get_request_on_endpoint("https://api.allegro.pl/sale/loyalty/promotions")
        print(promotions_dict)
        return map_to_dataframe(promotions_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_promotion_data_by_promotion_id(promotion_id):
    try:
        promotion_dict = do_get_request_on_endpoint(f"https://api.allegro.pl/sale/loyalty/promotions/{promotion_id}")
        print(promotion_dict)
        return map_to_dataframe(promotion_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_users_orders():
    try:
        orders_dict = do_get_request_on_endpoint("https://api.allegro.pl/order/checkout-forms")
        print(orders_dict)
        return map_to_dataframe(orders_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


# TODO {'errors': [{'code': 'VALIDATION_ERROR', 'message': 'Not valid time UUID', 'details': 'Invalid value: 1', 'path': 'getCheckoutForm.id', 'userMessage': 'Not valid time UUID'}]}
def get_order_data_by_order_id(order_id):
    try:
        order_dict = do_get_request_on_endpoint(f"https://api.allegro.pl/order/checkout-forms/{order_id}")
        print(order_dict)
        return map_to_dataframe(order_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
