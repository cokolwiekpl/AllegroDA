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


def get_category_by_category_id(token, category_id):
    try:
        url = f"https://api.allegro.pl/sale/categories/{category_id}"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        category_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(category_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_category_product_parameters_by_category_id(token, category_id):
    try:
        url = f"https://api.allegro.pl/sale/categories/{category_id}/product-parameters"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        product_parameters_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(product_parameters_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_category_parameters_by_category_id(token, category_id):
    try:
        url = f"https://api.allegro.pl/sale/categories/{category_id}/parameters"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        category_parameters_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(category_parameters_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_all_sellers_offers(
        token):  # TODO nie działa {'errors': [{'code': 'AccessDenied', 'message': 'Access is denied', 'details': None, 'path': None, 'userMessage': 'Access denied. Contact the author of the application.'}]}
    try:
        url = "https://api.allegro.pl/sale/offers"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        offers_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(offers_dict)
        return map_to_dataframe(offers_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_offer_tags_by_offer_id(
        token, offerId):  # TODO nie działa, error 500 xd
    try:
        url = f"https://api.allegro.pl/sale/offers/{offerId}/tags"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        offer_tags_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(offer_tags_dict)
        return map_to_dataframe(offer_tags_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_search_products_results(
        token):  # TODO nie działa AccessDeniedException
    try:
        url = "https://api.allegro.pl/sale/products"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        products_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(products_dict)
        return map_to_dataframe(products_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_product_data_by_product_id(
        token, productId):  # TODO nie działa AccessDeniedException
    try:
        url = f"https://api.allegro.pl/sale/products/{productId}"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        product_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(product_dict)
        return map_to_dataframe(product_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_user_list_of_promotions(
        token):  # TODO nie działa AccessDeniedException
    try:
        url = "https://api.allegro.pl/sale/loyalty/promotions"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        promotions_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(promotions_dict)
        return map_to_dataframe(promotions_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_promotion_data_by_promotion_id(
        token, promotionId):  # TODO nie działa AccessDeniedException
    try:
        url = f"https://api.allegro.pl/sale/loyalty/promotions/{promotionId}"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        promotion_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(promotion_dict)
        return map_to_dataframe(promotion_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_users_orders(
        token):  # TODO nie działa EmptyUserIdException
    try:
        url = "https://api.allegro.pl/order/checkout-forms"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        orders_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(orders_dict)
        return map_to_dataframe(orders_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_order_data_by_order_id(
        token,
        orderID):  # TODO {'errors': [{'code': 'VALIDATION_ERROR', 'message': 'Not valid time UUID', 'details': 'Invalid value: 1', 'path': 'getCheckoutForm.id', 'userMessage': 'Not valid time UUID'}]}
    try:
        url = f"https://api.allegro.pl/order/checkout-forms/{orderID}"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        order_dict = (requests.get(url, headers=headers, verify=False)).json()
        print(order_dict)
        return map_to_dataframe(order_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
