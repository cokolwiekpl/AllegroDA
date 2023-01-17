from src.allegro_api_reader.api_authoriser import get_access_token
from src.allegro_api_reader.api_reader import get_main_categories

ACCESS_TOKEN = get_access_token()


def test_main():
    # access_token = get_access_token()
    print("access token = " + ACCESS_TOKEN)
    main_categories = get_main_categories(ACCESS_TOKEN)
    print(main_categories)


def main():
    pass

if __name__ == "__main__":
    main()
    test_main()
