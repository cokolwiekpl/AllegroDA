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


def get_all_sellers_offers(token):
    try:
        url = "https://api.allegro.pl/sale/offers"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        offers_dict = (requests.get(url, headers=headers, verify=False)).json()
        return map_to_dataframe(offers_dict)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

# TODO
# Get product parameters available in given category
# https://api.{environment}/sale/categories/{categoryId}/product-parameters
# Endpoint pozwoli na pobranie informacji o dostępnych parametrach produktów dla danej kategorii, co pozwoli sklepom na zrozumienie, jakie cechy charakteryzują produkty dla danej kategorii.
#
# Get search products results
# https://api.{environment}/sale/products
# Endpoint pozwoli na pobranie informacji o wynikach wyszukiwania produktów, co pozwoli sklepom na zrozumienie, jakie produkty są poszukiwane przez klientów.
#
# Get all data of the particular product
# https://api.{environment}/sale/products/{productId}
# Endpoint pozwoli na pobranie pełnych danych dotyczących danego produktu, co pozwoli sklepom na zrozumienie, jakie cechy charakteryzują produkt oraz jakie są jego ceny.
#
#
# Get parameters supported by a category
# https://api.{environment}/sale/categories/{categoryId}/parameters
# Endpoint pozwoli na pobranie informacji o parametrach wspieranych przez dana kategorię, co pozwoli sklepom na zrozumienie, jakie cechy produktów są ważne dla klientów dla danej kategorii.
#
# Get the user's tags
# https://api.{environment}/sale/offer-tags
# Endpoint pozwoli na pobranie informacji o tagach użytkownika, co pozwoli sklepom na zrozumienie, jakie tagi są przypisane do ich produktów.
#
# Get tags assigned to an offer
# https://api.{environment}/sale/offers/{offerId}/tags
# Endpoint  pozwoli na pobranie informacji o tagach przypisanych do danej oferty, co pozwoli sklepom na zrozumienie, jakie tagi są przypisane do danego produktu.
#
# Get the user's list of promotions
# https://api.{environment}/sale/loyalty/promotions
# Endpoint pozwoli na pobranie informacji o promocjach użytkownika, co pozwoli sklepom na zrozumienie, jakie promocje są oferowane dla ich produktów.
#
# Get a promotion data by id
# https://api.{environment}/sale/loyalty/promotions/{promotionId}
# Endpoint pozwoli na pobranie informacji o konkretnej promocji na podstawie jej ID, co pozwoli sklepom na zrozumienie, jakie warunki muszą zostać spełnione, aby skorzystać z promocji.
#
# Get the user's orders
# https://api.{environment}/order/checkout-forms
# Endpoint pozwoli na pobranie informacji o zamówieniach użytkownika, co pozwoli sklepom na zrozumienie, jakie produkty zostały zamówione przez klientów.
#
# Get an order's details
# https://api.{environment}/order/checkout-forms/{id}
# Endpoint pozwoli na pobranie szczegółów dotyczących konkretnego zamówienia, co pozwoli sklepom na zrozumienie, jakie produkty zostały zamówione oraz jakie są szczegóły dotyczące dostawy i płatności.
