from src.allegro_api_reader.api_reader import *


def test_main():
    print("get_search_products_results")  # ten wydaje się być przydatny
    # print(get_search_products_results("Harry Potter i Książę Półkrwi"))
    print("get_product_data_by_product_id")  # ten również wydaje się być przydatny
    # print(get_product_data_by_product_id("9cb104b3-33d2-4866-8a7a-a626893c746b"))
    print("get_all_categories")
    # print(get_all_categories())
    print("get_category_details_by_category_id")
    # print(get_category_details_by_category_id(1))
    print("get_product_parameters_by_category_id")
    # print(get_product_parameters_by_category_id(1))
    print("get_category_parameters_by_category_id")
    # print(get_category_parameters_by_category_id(1))
    print("get_all_sellers_offers")  # Endpoint działa tylko na ofertach użytkownika, które sam wystawił :/
    # print(get_all_sellers_offers())
    print("get_user_list_of_promotions")  # Endpoint działa tylko na ofertach użytkownika, które sam wystawił :/
    # print(get_user_list_of_promotions())
    print("get_promotion_data_by_promotion_id")  # Endpoint działa tylko na ofertach użytkownika, które sam wystawił :/
    # print(get_promotion_data_by_promotion_id())
    print("get_users_orders")  # Endpoint działa tylko na ofertach użytkownika, które sam wystawił :/
    # print(get_users_orders())
    print("get_order_data_by_order_id")  # Endpoint działa tylko na ofertach użytkownika, które sam wystawił :/
    # print(get_order_data_by_order_id())


def main():
    pass


if __name__ == "__main__":
    main()
    test_main()
