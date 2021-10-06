import requests
from pesapy.utils.security_credentials import generate_security_credential
from pesapy.utils.access_token import generate_access_token
from pesapy.utils.timestamp import get_timestamp
import os


timestamp = get_timestamp()
access_token = generate_access_token()
acc_bal_initiator_passwd = os.getenv("ACC_BAL_INITIATOR_PASSWD")
assert(acc_bal_initiator_passwd != None), "Missing acc_bal_initiator_passwd"
base_url = os.getenv("BASE_URL")
assert(base_url != None), "Missing base_url"
acc_bal_initiator_name = os.getenv("ACC_BAL_INITIATOR_NAME")
assert(acc_bal_initiator_name !=
       None), "Missing acc_bal_initiator_name"
security_credentials = generate_security_credential(acc_bal_initiator_passwd)
acc_bal_result_url = os.getenv("ACC_BAL_RESULT_URL")
assert(acc_bal_result_url != None), "Missing acc_bal_result_url"
acc_bal_queue_timeout_url = os.getenv("ACC_BAL_QUEUE_TIMEOUT_URL")
assert(acc_bal_queue_timeout_url != None), "Missing acc_bal_queue_timeout_url"


class AccountBalance:
    """ Checks the balance on an M-Pesa BuyGoods(Till Number)"""
    @staticmethod
    def process_transaction(**kwargs):
        """
        Processes the reversal transaction.
        :param: kwargs - Key value arguments that must contain the transaction_id, amount, remarks and an
                         optional additional_info parameter.
        :return: Returns a json string showing the result of the transaction processing.
        """
        access_token = generate_access_token()
        account_bal_party = kwargs.get("account_bal_party")
        assert(account_bal_party !=
               None), "Missing account_balance_receiver_party"
        acc_bal_identifier_type = kwargs.get("acc_bal_identifier_type")
        assert(acc_bal_identifier_type !=
               None), "Missing  acc_bal_identifier_type"
        remarks = kwargs.get("remarks")
        assert(remarks != None), "Missing remarks"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload = {

            "Initiator": acc_bal_initiator_name,
            "SecurityCredential": security_credentials,
            "CommandID": "AccountBalance",
            "PartyA": account_bal_party,
            "IdentifierType": acc_bal_identifier_type,
            "ResultURL": acc_bal_result_url,
            "QueueTimeOutURL": acc_bal_queue_timeout_url,
            "Remarks": remarks,

        }
        response = requests.post(f"{base_url}/mpesa/accountbalance/v1/query",
                                 json=payload, headers=headers)
        return response.json()
