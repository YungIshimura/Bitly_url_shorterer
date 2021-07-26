import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def configure_parser():
    parser = argparse.ArgumentParser(description=""" 
    Программа для сокращения URL (битлинка) и получения количества переходов по битлинку. 
    Программа взаимодействует с сервисом Bitly.org через API-ключ. 
    При вводе обычной ссылки вы получаете битлинк. 
    При вводе же битлинка получаете количество переходов по нему.
    """)
    parser.add_argument("user_link", nargs="+", help="Cсылка для сокращения или битлинк")

    return parser


def check_link(api_key, user_link):
    link_check = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    parsed_user_link = urlparse(user_link)
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(
        link_check.format(bitlink=f"{parsed_user_link.netloc}{parsed_user_link.path}"),
        headers=headers,
    )
    check = response.ok
    return check


def shorten_link(api_key, user_link):
    bitlink_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"long_url": user_link}
    response = requests.post(bitlink_url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()
    return bitlink["id"]


def count_clicks(api_key, user_link):
    click_url = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    parsed_bitlink = urlparse(user_link)
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "unit": "day",
        "units": -1,
    }
    response = requests.get(
        click_url.format(bitlink=f"{parsed_bitlink.netloc}{parsed_bitlink.path}"),
        params=payload,
        headers=headers,
    )
    response.raise_for_status()
    count_clicks = response.json()
    return count_clicks["total_clicks"]


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("BITLY_API_KEY")
    parser = configure_parser()
    args = parser.parse_args()
    for user_link in args.user_link:
        check = check_link(api_key, user_link)
        try:
            if not check:
                print("Битлинк: ", shorten_link(api_key, user_link))
            else:
                print(f"По вашей ссылке прошли: {count_clicks(api_key, user_link)} раз (а)")
        except requests.exceptions.HTTPError:
                print("Ссылка введена неверно ")