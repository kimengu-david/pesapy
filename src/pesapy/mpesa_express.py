import os
import requests
from dotenv import load_dotenv
from pesapy.utils.access_token import generate_access_token
from pesapy.utils.request_passwd import generate_request_passwd
from pesapy.utils.timestamp import get_timestamp


load_dotenv()
timestamp = get_timestamp()
access_token = generate_access_token()
base_url = os.getenv("BASE_URL")
assert(base_url != None), "missing base_url"
mpesa_express_business_shortcode = os.getenv(
    "MPESA_EXPRESS_BUSINESS_SHORTCODE")
assert(mpesa_express_business_shortcode !=
       None), "missing mpesa_express_business_shortcode"
mpesa_express_callback_url = os.getenv("MPESA_EXPRESS_CALLBACK_URL")
assert(mpesa_express_callback_url != None), "Missing mpesa_express_callback_url"


class MpesaExpress:
    """Handles Mpesa Express transactions"""
    @staticmethod
    def process_transaction(**kwargs) -> str:
        """
        Processes an mpesa express transaction post request
        :param kwargs: Keyword arguments containing amount, phone_number and transaction description
        :return json string that contains information about the processed transaction.
        """
        phone_number = kwargs.get("phone_number")
        assert(len(str(phone_number)) == 12 and str(
            phone_number).startswith("254")), "Invalid Phone Number"
        amount = kwargs.get("amount")
        assert(int(amount) >= 1), "Invalid Amount"
        account_reference = kwargs.get("account_reference")
        assert(account_reference != None), "Missing account reference"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {
            "BusinessShortCode": mpesa_express_business_shortcode,
            "Password":  generate_request_passwd(timestamp),
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": mpesa_express_business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": mpesa_express_callback_url,
            "AccountReference": account_reference,
            "TransactionDesc": kwargs.get("transaction_desc")
        }
        response = requests.post(f"{base_url}/mpesa/stkpush/v1/processrequest",
                                 json=payload, headers=headers)
        return response.json()

    @staticmethod
    def trans_status(checkout_request_id):
        """
        Checks the status of an Mpesa Express transaction.
        :param checkout_id - This is a global unique identifier of the processed checkout
                                transaction request.
        return - json str response object showing details about the processed transaction.
        """
        headers = {"Authorization": "Bearer %s" % access_token}

        payload = {
            "BusinessShortCode": mpesa_express_business_shortcode,
            "Password":  generate_request_passwd(timestamp),
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id
        }
        response = requests.post(f"{base_url}/mpesa/stkpushquery/v1/query",
                                 json=payload, headers=headers)
        return response.json()
