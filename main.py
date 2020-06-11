import os
import requests
import argparse
from dotenv import load_dotenv, find_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description='The script creates short links and shows click statistics on a short link.'
    )
    parser.add_argument('link', help='Enter link')
    return parser


def get_header_request(token):
    headers = {
        'User-Agent': 'curl',
        'Authorization': 'Bearer {}'.format(token)
    }
    return headers


def count_clicks(token, bitlink):
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = get_header_request(token)
    params = {
        'unit': 'day',
        'units': -1
    }
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def shorten_link(token, url):
    api_address = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = get_header_request(token)
    payload = {
        'long_url': url
    }
    response = requests.post(api_address, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def get_profile(token):
    url = 'https://api-ssl.bitly.com/v4/user'
    headers = get_header_request(token)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def main():
    load_dotenv(find_dotenv())
    token = os.getenv('ACCESS_TOKEN')
    parser = create_parser()
    args = parser.parse_args()
    user_link = args.link
    if user_link.startswith("bit.ly"):
        try:
            count_link = count_clicks(token, user_link)
            print('Количество кликов: ', count_link)
        except requests.exceptions.HTTPError as error:
            exit(f"Can't get data from server:\n{error}")
    else:
        try:
            bitlink = shorten_link(token, user_link)
            print('Короткая ссылка: ', bitlink)
        except requests.exceptions.HTTPError as error:
            exit(f"Can't get data from server:\n{error}")


if __name__ == "__main__":
    main()
