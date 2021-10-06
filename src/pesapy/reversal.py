import requests
from pesapy.utils.security_credentials import generate_security_credential
from pesapy.utils.access_token import generate_access_token
from pesapy.utils.timestamp import get_timestamp
import os


timestamp = get_timestamp()

access_token = generate_access_token()
reversal_initiator_passwd = os.getenv("REVERSAL_INITIATOR_PASSWD")
assert(reversal_initiator_passwd != None), "Missing reveral_initiator_passwd"
base_url = os.getenv("BASE_URL")
assert(base_url != None), "Missing base_url"
reversal_initiator_name = os.getenv("REVERSAL_INITIATOR_NAME")
assert(reversal_initiator_name != None), "Missing reversal_initiator_name"
reversal_receiver_party = os.getenv("REVERSAL_RECEIVER_PARTY")
assert(reversal_receiver_party != None), "Missing reversal_receiver_party"
security_credentials = generate_security_credential(reversal_initiator_passwd)
receiver_identifier_type = os.getenv("REVERSAL_RECEIVER_IDENTIFIER_TYPE")
assert(receiver_identifier_type != None), "Missing receiver_identifier_id"
reversal_result_url = os.getenv("REVERSAL_RESULT_URL")
assert(reversal_result_url != None), "Missing reversal_result_url"
reversal_queue_timeout_url = os.getenv("REVERSAL_QUEUE_TIMEOUT_URL")
assert(reversal_queue_timeout_url != None), "Missing reversal_queue_timeout_url"


class Reversal:
    """ Reverses B2C, C2B, B2B transactions"""
    @staticmethod
    def process_transaction(**kwargs):
        """
        Processes the reversal transaction.
        :param: kwargs - Key value arguments that must contain the transaction_id, amount, remarks and an
                         optional additional_info parameter.
        :return: Returns a json string showing the result of the transaction processing.
        """
        access_token = generate_access_token()
        transaction_id = kwargs.get("transaction_id")
        assert(transaction_id != None), "Missing transaction_id"
        amount = kwargs.get("amount")
        assert(int(amount) >= 1), "Invalid Amount"
        remarks = kwargs.get("remarks")
        assert(remarks != None), "Missing remarks"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {

            "Initiator": reversal_initiator_name,
            "SecurityCredential": security_credentials,
            "CommandID": "TransactionReversal",
            "TransactionID": transaction_id,
            "Amount": amount,
            "ReceiverParty": reversal_receiver_party,
            "RecieverIdentifierType": receiver_identifier_type,
            "ResultURL": reversal_result_url,
            "QueueTimeOutURL": reversal_queue_timeout_url,
            "Remarks": remarks,
            "Occasion": kwargs.get("additional_info")

        }
        response = requests.post(f"{base_url}/mpesa/reversal/v1/request",
                                 json=payload, headers=headers)
        return response.json()
