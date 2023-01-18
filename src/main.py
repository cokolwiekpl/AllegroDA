from src.allegro_api_reader.api_authoriser import get_access_token, generate_token, check_token
from src.allegro_api_reader.api_reader import get_all_categories, get_category_by_category_id, \
    get_category_product_parameters_by_category_id, get_all_sellers_offers, get_category_parameters_by_category_id, \
    get_search_products_results, get_product_data_by_product_id, get_user_list_of_promotions, \
    get_promotion_data_by_promotion_id, get_users_orders, get_order_data_by_order_id

# ACCESS_TOKEN = check_token()

def test_main():
    # print(ACCESS_TOKEN)

    # print("get_all_categories")
    # print(get_all_categories(ACCESS_TOKEN))
    # print("________________")
    #
    # print("get_category_by_category_id")
    # print(get_category_by_category_id(ACCESS_TOKEN, 1))
    # print("________________")
    #
    # print("get_category_product_parameters_by_category_id")
    # print(get_category_product_parameters_by_category_id(ACCESS_TOKEN, 1))
    # print("________________")
    #
    # print("get_category_parameters_by_category_id")
    # print(get_category_parameters_by_category_id(ACCESS_TOKEN, 1))
    # print("________________")
    #
    # print("get_all_sellers_offers")
    # print(get_all_sellers_offers(ACCESS_TOKEN))
    # print("________________")
    #
    # print("get_offer_tags_by_offer_id")
    # print(get_offer_tags_by_offer_id(ACCESS_TOKEN, 1))
    # print("________________")

    print("get_search_products_results")
    print(get_search_products_results())
    print("________________")

    print("get_product_data_by_product_id")
    print(get_product_data_by_product_id(1))
    print("________________")

    # print("get_user_list_of_promotions")
    # print(get_user_list_of_promotions(ACCESS_TOKEN))
    # print("________________")
    #
    # print("get_promotion_data_by_promotion_id")
    # print(get_promotion_data_by_promotion_id(ACCESS_TOKEN, 1))
    # print("________________")
    #
    # print("get_users_orders")
    # print(get_users_orders(ACCESS_TOKEN))
    # print("________________")

    print("get_order_data_by_order_id")
    print(get_order_data_by_order_id(1))
    print("________________")


def main():
    pass


if __name__ == "__main__":
    main()
    test_main()
