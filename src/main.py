from src.allegro_api_reader.api_authoriser import get_access_token
from src.allegro_api_reader.api_reader import get_main_categories


def main():
    access_token = get_access_token()
    print("access token = " + access_token)
    main_categories = get_main_categories(access_token)
    print(type(main_categories))



if __name__ == "__main__":
    main()
