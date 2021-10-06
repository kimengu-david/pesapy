from requests.sessions import get_environ_proxies
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os


load_dotenv()


def generate_access_token() -> str:
    consumer_key = os.getenv("CONSUMER_KEY")
    assert(consumer_key != None), "consumer_key cannot be empty"
    consumer_secret = os.getenv("CONSUMER_SECRET")
    assert(consumer_secret != None), "consumer_secret cannot be empty"
    base_url = os.getenv("BASE_URL")
    assert(base_url != None), "base_url cannot be empty"
    resp = requests.get(f"{base_url}/oauth/v1/generate?grant_type=client_credentials", auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    if resp.status_code != 200:
        raise ValueError(
            "An error ocurred while generating the access token, check consumer_key and consumer_secret values")
    access_token = resp.json().get("access_token")

    return access_token
