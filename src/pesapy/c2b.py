import os
import requests
import json
from pesapy.utils.access_token import generate_access_token
from pesapy.utils.validate_url import is_valid_url

access_token = generate_access_token()
c2b_response_type = os.getenv("C2B_RESPONSE_TYPE")
assert(c2b_response_type != None), "Missing c2b_response_type"
short_code = os.getenv("C2B_SHORTCODE")
assert(short_code != None), "Missing c2b_shortcode"
base_url = os.getenv(
    "BASE_URL")
assert(base_url !=
       None), "Missing base_url"


class C2B:
    """Handles C2B transaction"""
    @staticmethod
    def process_transaction(**kwargs):
        """
        :kwargs - A set of keyword arguments that must contain the business shortcode
                  confirmation_url and validation_url
        :return - Returns a json string response.
        """
        confirmation_url = kwargs.get("confirmation_url")
        test = is_valid_url(confirmation_url)
        assert(is_valid_url(confirmation_url) ==
               True), "Invalid confirmation url"
        validation_url = kwargs.get("validation_url")
        assert(is_valid_url(validation_url) ==
               True), "Invalid validation url"

        headers = {"Authorization": "Bearer %s" % access_token,
                   'Content-Type': 'application/json',
                   }

        payload = {
            "ShortCode": short_code,
            "ResponseType": c2b_response_type,
            "ConfirmationURL": confirmation_url,
            "ValidationURL": validation_url
        }

        response = requests.request(
            "POST", f"{base_url}/mpesa/c2b/v1/registerurl", headers=headers, data=json.dumps(payload))
        return response.json()

    @staticmethod
    def simulate(**kwargs):
        """
            Simulates a c2b transaction.
        """
        c2b_api_endpoint = f"{base_url}/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {
            "ShortCode": kwargs.get("short_code"),
            "CommandID": "CustomerPayBillOnline",
            "Amount": kwargs.get("amount"),
            "Msisdn": kwargs.get("customer_phone_no"),
            "BillRefNumber": "00000"
        }
        response = requests.request(
            "POST", c2b_api_endpoint, headers=headers, json=payload)
        return(response.json())
