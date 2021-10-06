import base64
import os

mpesa_express_business_shortcode = os.getenv(
    "MPESA_EXPRESS_BUSINESS_SHORTCODE")
assert(mpesa_express_business_shortcode !=
       None), "missing mpesa_express_business_shortcode"
lipa_na_mpesa_passkey = os.getenv("LIPA_NA_MPESA_PASSKEY")
assert(lipa_na_mpesa_passkey != None), "Missing lipa_na_mpesa_passkey"


def generate_request_passwd(timestamp: str) -> str:
    """
    Generates the password used to encrypt the request sent for an STK push transaction.
    :timestamp - This is the Timestamp of the transaction, normaly in the formart of
                 YEAR+MONTH+DATE+HOUR+MINUTE+SECOND (YYYYMMDDHHMMSS)
    :return -  A base64 encoded string
    """
    data_to_encode = mpesa_express_business_shortcode + \
        lipa_na_mpesa_passkey + timestamp
    password = base64.b64encode(data_to_encode.encode("utf-8"))
    password = password.decode("utf-8")

    return password
