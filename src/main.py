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
    print("get_user_list_of_promotions")
    # print(get_user_list_of_promotions())

    ##################

    #
    #
    # print("________________")
    #
    # print("get_offer_tags_by_offer_id")
    # print(get_offer_tags_by_offer_id(ACCESS_TOKEN, 1))
    # print("________________")

    # print("get_search_products_results")
    # print(get_search_products_results("Harry Potter i Książę Półkrwi"))
    # print("________________")
    #
    #
    #
    # print("________________")

    #
    #
    # print("________________")
    #
    # print("get_promotion_data_by_promotion_id")
    # print(get_promotion_data_by_promotion_id(ACCESS_TOKEN, 1))
    # print("________________")
    #
    # print("get_users_orders")
    # print(get_users_orders())
    # print("________________")

    # print("get_order_data_by_order_id")
    # print(get_order_data_by_order_id("29738e61-7f6a-11e8-ac45-09db60ede9d6"))
    # print("________________")


def main():
    pass


if __name__ == "__main__":
    main()
    test_main()
