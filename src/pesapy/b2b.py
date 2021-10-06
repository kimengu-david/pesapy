import os
import requests
from pesapy.utils.security_credentials import generate_security_credential
from pesapy.utils.access_token import generate_access_token


base_url = os.getenv("BASE_URL")
assert(base_url != None), "b2b_api_endpoint must be provided"
InitiatorName = os.getenv("B2B_INITIATOR_NAME")
assert(InitiatorName != None), "b2b_initiator_Name  must be provided"
b2b_initiator_password = os.getenv("B2B_INITIATOR_PASSWORD")
assert(b2b_initiator_password != None), "b2b_initiator_password must be provided"
b2b_shortcode = os.getenv("B2B_SHORTCODE")
assert(b2b_shortcode != None), "b2b_shortcode must be provided"
b2b_result_url = os.getenv("B2B_RESULT_URL")
assert(b2b_shortcode != None), "b2b_result_url must be provided"
b2b_queue_timeOut_url = os.getenv("B2B_QUEUE_TIMEOUT_URL")
assert(b2b_queue_timeOut_url != None), "b2b_queue_timeOut_url must be provided"
access_token = generate_access_token()
b2b_sender_type = os.getenv("B2B_SENDER_TYPE")
assert(b2b_sender_type != None), "Missing b2b_sender_type"


class B2B:
    """Handles B2B transactions"""
    @staticmethod
    def process_transaction(**kwargs):
        """
        Processes the B2B transaction.
        :kwargs: A set of keyword arguments containing the command_id, amount, credit_party, remarks
                and additinal_info. Remarks and additional_info are optional.
        :return: Returns a json string
        """
        security_credential = generate_security_credential(
            b2b_initiator_password)
        command_id = kwargs.get("command_id")
        assert(command_id != None), "Command id must be provided"
        amount = kwargs.get("amount")
        assert(int(amount) >= 1), "Invalid Amount"
        credit_party = kwargs.get("credit_party")
        assert(credit_party != None), "Credit Party cannot be empty"
        b2b_receiver_type = kwargs.get("b2b_receiver_type")
        assert(b2b_receiver_type != None), "b2b_receiver_type must be provided"
        account_reference = kwargs.get("account_reference")
        assert(account_reference != None), "account_reference must be provided"
        remarks = kwargs.get("remarks")
        assert(remarks != None), "remarks must be provided"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {
            "Initiator": InitiatorName,
            "SecurityCredential": security_credential,
            "CommandID": command_id,
            "Amount": amount,
            "PartyA": b2b_shortcode,
            "PartyB":  credit_party,
            "RecieverIdentifierType": b2b_receiver_type,
            "SenderIdentifierType": b2b_sender_type,
            "AccountReference": account_reference,
            "Remarks": remarks,
            "QueueTimeOutURL": b2b_queue_timeOut_url,
            "ResultURL": b2b_result_url,
            "Occassion": kwargs.get("additional_info")



        }
        response = requests.post(
            f"{base_url}/mpesa/b2b/v1/paymentrequest", json=payload, headers=headers)
        return response.json()
