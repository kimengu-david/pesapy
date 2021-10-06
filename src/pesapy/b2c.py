import os
import requests
from pesapy.utils.security_credentials import generate_security_credential
from pesapy.utils.access_token import generate_access_token


base_url = os.getenv("BASE_URL")
assert(base_url != None), "base_url must be provided"
InitiatorName = os.getenv("B2C_INITIATOR_NAME")
assert(InitiatorName != None), "b2c_initiator_Name  must be provided"
b2c_initiator_password = os.getenv("B2C_INITIATOR_PASSWORD")
assert(b2c_initiator_password != None), "b2c_initiator_password must be provided"
b2c_shortcode = os.getenv("B2C_SHORTCODE")
assert(b2c_shortcode != None), "b2c_shortcode must be provided"
b2c_result_url = os.getenv("B2C_RESULT_URL")
assert(b2c_shortcode != None), "b2c_result_url must be provided"
b2c_queue_timeOut_url = os.getenv("B2C_QUEUE_TIMEOUT_URL")
assert(b2c_queue_timeOut_url != None), "b2c_queue_timeOut_url must be provided"


class B2C:
    @staticmethod
    def process_transaction(**kwargs) -> str:
        """
        Processes a B2C transaction
        :param kwargs - Key word arguments that must contain the command_id, transaction amount,
                      phone_number, remarks and additional information for the 
                      transaction.  Remarks and additional_info are optional.
        :return - Returns a json string on success
        """
        access_token = generate_access_token()
        security_credential = generate_security_credential(
            b2c_initiator_password)
        phone_number = kwargs.get("phone_number")
        assert(len(str(phone_number)) == 12 and str(
            phone_number).startswith("254")), "Invalid Phone Number"
        command_id = kwargs.get("command_id")
        assert(command_id != None), "Command id must be provided"
        amount = kwargs.get("amount")
        assert(int(amount) >= 1), "Invalid Amount"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {
            "InitiatorName": InitiatorName,
            "SecurityCredential": security_credential,
            "CommandID": command_id,
            "Amount": amount,
            "PartyA": b2c_shortcode,
            "PartyB": phone_number,
            "Remarks": kwargs.get("remarks"),
            "QueueTimeOutURL": b2c_queue_timeOut_url,
            "ResultURL": b2c_result_url,
            "Occassion": kwargs.get("occasion")

        }
        response = requests.post(
            f"{base_url}/mpesa/b2c/v1/paymentrequest", json=payload, headers=headers)
        return response.json()
