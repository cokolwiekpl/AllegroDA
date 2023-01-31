from allegro_api_reader.api_reader import get_search_products_results, get_category_details_by_category_id


def get_products_data_by_name(name: str) -> list:
    """
    Get product data for a given product name.
    Parameters:
    name (str): The name of the product to search for.
    Returns:
    list: A list of dictionaries containing the id, name, and category of the products matching the search.
    """
    product_list = get_search_products_results(name)["products"]
    products_data_list = []
    for i in product_list:
        single_product_data = {
            "id": i["id"],
            "name": i["name"],
            "category": get_category_details_by_category_id(i["category"]["id"])["name"],
        }
        products_data_list.append(single_product_data)
    return products_data_list
