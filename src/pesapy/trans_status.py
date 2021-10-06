import requests
import os
from pesapy.utils.security_credentials import generate_security_credential
from pesapy.utils.access_token import generate_access_token
from pesapy.utils.timestamp import get_timestamp


timestamp = get_timestamp()

access_token = generate_access_token()
trans_status_initiator_passwd = os.getenv("TRANS_STATUS_INITIATOR_PASSWD")
assert(trans_status_initiator_passwd !=
       None), "Missing trans_status_initiator_passwd"
security_credentials = generate_security_credential(
    trans_status_initiator_passwd)
base_url = os.getenv("BASE_URL")
assert(base_url != None), "Missing base_url"
trans_status_initiator_name = os.getenv("TRANS_STATUS_INITIATOR_NAME")
assert(trans_status_initiator_name != None), "trans_status_initiator_name"
trans_status_business_shortcode = os.getenv("TRANS_STATUS_BUSINESS_SHORTCODE")
assert(trans_status_business_shortcode !=
       None), "Missing trans_status_business_shortcode"
trans_status_identifier_type = os.getenv("TRANS_STATUS_IDENTIFIER_TYPE")
assert(trans_status_identifier_type !=
       None), "Missing trans_status_identifier_type"
trans_status_result_url = os.getenv("TRANS_STATUS_RESULT_URL")
assert(trans_status_result_url != None), "Missing trans_status_result_url"
trans_status_queue_timeout_url = os.getenv("TRANS_STATUS_QUEUE_TIMEOUT_URL")
assert(trans_status_queue_timeout_url !=
       None), "Missing trans_status_queue_timeout_url"


class TransStatus:
    """Handles the transaction status query"""
    @staticmethod
    def process_transaction(**kwargs) -> str:
        """
        Processes the transaction_status transaction
        :param kwargs - A set of keyword arguments containing a mandory transaction_id, remarks and
                        optional additional info parameter.
        """
        access_token = generate_access_token()
        transaction_id = kwargs.get("transaction_id")
        assert(transaction_id != None), "Missing transaction_id"
        remarks = kwargs.get("remarks")
        assert(remarks != None), "Missing remarks"
        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {

            "Initiator": trans_status_initiator_name,
            "SecurityCredential": security_credentials,
            "CommandID": "TransactionStatusQuery",
            "TransactionID": transaction_id,
            "PartyA": trans_status_business_shortcode,
            "IdentifierType": trans_status_identifier_type,
            "ResultURL": trans_status_result_url,
            "QueueTimeOutURL": trans_status_queue_timeout_url,
            "Remarks": remarks,
            "Occasion": kwargs.get("Occasion")

        }
        response = requests.post(f"{base_url}/mpesa/transactionstatus/v1/query",
                                 json=payload, headers=headers)
        return response.json()
