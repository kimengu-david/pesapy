
# mpesa_py   version 1.0.0

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  
mpesa_py is an unofficial M-Pesa API wrapper. Its saves you all the hardwork and pain\
that most developers go through when intergrating the [Safaricom M-Pesa](https://developer.safaricom.co.ke/) API into
their systems.\
This library does all the hardwork for you and exposes a simple interface that easy to use and\
makes your code clean and maintainable.

_M-Pesa is Africa's largest mobile money platform with more than 40 million users \
in seven African countries where it operates, Hence the need to understand its APIs._
#### Covers the following transactions types:


* Mpesa Express/lipa na mpesa online/STK Push
* Reversals
* B2C(Business To Customer)
* B2B(Business To Business)
* C2B(Customer To Business)
* Transaction status
* Account Balance

# Getting Started with mpesa_py

## Installation

Install mpesa_py with pip

```bash
  pip install mpesa_py
```
Navigate to the root folder of your project and create a .env file that will
hold all the environment variables required by mpesa_py.\
For  example on a linux 
system:
```bash
  cd  /path_to_root_folder/
  touch .env
```
_Dont forget the dot (.) before env when creating the .env file_

Using your favorite editor open  the .env file and paste and fill in the following required\
environment variables
```python
BASE_URL=https://api.safaricom.co.ke
CONSUMER_KEY=
CONSUMER_SECRET=
LIPA_NA_MPESA_PASSKEY=
MPESA_EXPRESS_CALLBACK_URL=
MPESA_EXPRESS_BUSINESS_SHORTCODE=

C2B_RESPONSE_TYPE=Completed
C2B_SHORTCODE=600981

B2C_INITIATOR_PASSWORD=
B2C_INITIATOR_NAME=
B2C_SHORTCODE=
B2C_QUEUE_TIMEOUT_URL=
B2C_RESULT_URL=

B2B_INITIATOR_PASSWORD=
B2B_INITIATOR_NAME
B2B_SHORTCODE=
B2B_QUEUE_TIMEOUT_URL=
B2B_RESULT_URL=
B2B_SENDER_TYPE=


REVERSAL_INITIATOR_NAME=
REVERSAL_INITIATOR_PASSWD=
REVERSAL_RECEIVER_PARTY=
REVERSAL_RECEIVER_IDENTIFIER_TYPE=
REVERSAL_RESULT_URL=
REVERSAL_QUEUE_TIMEOUT_URL

TRANS_STATUS_INITIATOR_NAME=
TRANS_STATUS_INITIATOR_PASSWD=
TRANS_STATUS_BUSINESS_SHORTCODE=
TRANS_STATUS_IDENTIFIER_TYPE=
TRANS_STATUS_RESULT_URL=
TRANS_STATUS_QUEUE_TIMEOUT_URL=

ACC_BAL_INITIATOR_NAME=
ACC_BAL_INITIATOR_PASSWD=
ACC_BAL_RESULT_URL=
ACC_BAL_QUEUE_TIMEOUT_URL=

PUBKEY_PATH = 
```

## Environment variables Explanation
***BASE_URL*** --- Is the main URL for Safaricom M-Pesa API.\
_production_: https://api.safaricom.co.ke\
_development_:https://sandbox.safaricom.co.ke
***CONSUMER_KEY and CONSUMER_SECRET*** ---Is your application's consumer key and secret respectively.\
 They are provided by safaricom in the developers portal https://developer.safaricom.co.ke/MyApps. \
 Used to generate access token.\
***MPESA_EXPRESS_API_ENDPOINT*** --- Is Safaricom API endpoint for mpesa express transactions.\
**MPESA_EXPRESS_CALLBACK_URL** --- A CallBack URL is a valid secure URL that is used to receive notifications from M-Pesa API. \
It is the endpoint to which the results will be sent by M-Pesa API.\
***MPESA_EXPRESS_BUSINESS_SHORTCODE*** --- This is organizations shortcode (Paybill or Buygoods - A 5 to 7 digit account number). \
Used to identify an organization and receive the transaction.\
***LIPA_NA_MPESA_PASSKEY*** --- Used to generate the request password in combination with the business shortcode

***C2B_REGISTRATION_API_ENDPOINT*** --- M-pesa api endpoint for customer to business transactions.\
It is used to register both the confirmatation and validation URLs.\
***C2B_RESPONSE_TYPE*** - This parameter specifies what is to happen if for any reason the validation URL is nor reachable.\
 Note that, This is the default action value that determines what MPesa will do in the scenario that your endpoint is \
 unreachable or is unable to respond on time. \
 Only two values are allowed: Completed or Cancelled. \
 Completed means MPesa will automatically complete your transaction, \
 whereas Cancelled means MPesa will automatically cancel the transaction, in the event MPesa is unable to\
  reach your Validation URL.\
***C2B_SHORTCODE*** --- Is the shortcode of the organization. eg 600981\
\
***B2C_INITIATOR_NAME*** --- The username of the M-Pesa Business to Customer(B2C) account API operator. \
 NOTE: the access channel for this operator must be API and the account must be in active status.\
***B2C_INITIATOR_PASSWORD*** --- Used in combination with the public key certificate
to produce the security credentials.\
***B2C_SHORTCODE*** --- This is the B2C organization shortcode from which the money is to be sent.\
***B2C_QUEUE_TIMEOUT_URL*** --- This is the URL to be specified in your request that will be used by API Proxy to send notification \
incase the payment request is timed out while awaiting processing in the queue.\
***B2C_RESULT_URL*** --- This is the URL to be specified in your request that will be used by M-Pesa to send notification upon processing of the payment request
\
\
\
***B2B_INITIATOR_PASSWORD*** ---The password for M-Pesa B2B account API operator\
***B2B_INITIATOR_NAME*** --- The username for M-Pesa B2B account API operator\
***B2B_SHORTCODE*** --- This is the B2B organization shortcode from which the money is to be sent\
***B2B_SENDER_TYPE*** ---  Type of organization sending the transaction\
1 – MSISDN, 2 – Till Number, 4 – Organization short code\
***B2B_RESULT_URL*** --- The path that stores information of transaction after it has been\
processed by M-Pesa\
***B2B_QUEUE_TIMEOUT_URL***---The path that stores information of time out transaction
\
\
***REVERSAL_INITIATOR_NAME*** ---The username for M-Pesa reversal account API operator
***REVERSAL_INITIATOR_PASSWD*** ---The password for M-Pesa reversal account API operator
***REVERSAL_RECEIVER_PARTY*** ---Shortcode for the organization initiating the reversal
***REVERSAL_RECEIVER_IDENTIFIER_TYPE*** ---Type of organization receiving the transaction. Always set to 11.
\
\
***TRANS_STATUS_IDENTIFIER_TYPE*** ---Type of organization sending the transaction
1 – MSISDN, 2 – Till Number, 4 – Organization short code
\
***PUBKEY_PATH*** -- The **absolute** path to the file containing your public key certificate. A pem file. \
This must be downloaded from the daraja api portal:
sandbox [link](https://developer.safaricom.co.ke/api/v1/GenerateSecurityCredential/SandboxCertificate.cer)
,production [link](https://developer.safaricom.co.ke/api/v1/GenerateSecurityCredential/ProductionCertificate.cer)





## Usage/Examples
mpesa_py library contains the following classes each with its own process_transaction
method that processes the transaction.
* C2B
* B2C
* B2B
* TransStatus
* Reversal

1. ### STK push/Mpesa Express/lipa na mpesa online
It is used to send a  payment prompt on the customers phone (Popularly known as STK Push Prompt) \
to your customer's M-PESA registered phone number requesting them to enter their M-PESA pin to \
authorize and complete a payment.

The process_transaction method of MpesaExpress class takes the following key word arguments.

***amount*** --- Money that customer pays to the Shorcode. Only whole numbers are supported.

***customer_phone_no*** ---The phone number sending money. The parameter expected is a Valid Safaricom Mobile Number that is M-Pesa registered. \
Must have the following format 2547XXXXXXXX

***short_code*** ---The organization receiving the funds. The parameter expected is a 5 to 7 Shortcode. \
 This can be the same as BusinessShortCode value.

***account_reference*** --- Account Reference: This is an Alpha-Numeric parameter that is defined by your system as an Identifier \
of the transaction for CustomerPayBillOnline transaction type. \
 Along with the business name, this value is also displayed to the customer in the STK Pin Prompt message. Maximum of 12 characters

***transaction_desc*** --- This is any additional information/comment that can be sent along with the request from your system. \
Maximum of 13 Characters


#### Using mpesa_py in interactive python mode(stk push)
```python
>>>from mpesa_py.mpesa_express import MpesaExpress
>>>MpesaExpress.process_transaction(
    amount="1", phone_number="254741937028", account_reference="test_api",
    transaction_desc="pay school fees")
>>>>

```

## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/mpesaexpress.png)

The return value of the method MpesaExpress.process_transaction is a json string of the
following format on success
```json
{'MerchantRequestID': '117890-42812180-1', 'CheckoutRequestID': 'ws_CO_021020211021428942',
 'ResponseCode': '0', 'ResponseDescription': 'Success. Request accepted for processing', 
 'CustomerMessage': 'Success. Request accepted for processing'
 }
```


#### sample Python script.

```python
from mpesa_py.mpesa_express import MpesaExpress

resp = MpesaExpress.process_transaction(
    amount="1", phone_number="254741937028", account_reference="test_api",
    transaction_desc="pay school fees")
print(resp)

```

2. ### B2C (Business to customer transaction)
B2C API is an API used to make payments from a Business to Customers (Pay Outs).\
Also known as Bulk Disbursements\
B2C API is used in several scenarios by businesses that require to either make Salary Payments, \
Cashback payments, Promotional Payments(e.g. betting winning payouts), winnings, \
financial institutions withdrawal of funds, loan disbursements etc.


The process_transaction method of B2C class takes the following key word arguments.

***command_id*** -- This is a unique command that specifies B2C transaction type \
Sample values include SalaryPayment, BusinessPayment, PromotionPayment

***amount*** -- The amount of money being sent to the customer.

***phone_number*** -- This is the customer mobile number  to receive the amount.\
Must have the following format 2547XXXXXXXX

***remarks*** -- Any additional information to be associated with the transaction

***occasion*** -- Any other additional information to be associated with the transaction.

#### Using mpesa_py in interactive python mode(b2c transaction)
```python
>>>from mpesa_py import B2C
>>> B2C.process_transaction(
    command_id="BusinessPayment", amount=1000, phone_number="254708374149",
    remarks="Requested on Tuesday", occassion="issue closed"
)
>>>

```
## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/b2_c.png)

#### sample python script.
You can save the same transaction in a python script and run the script.
```python
  from mpesa_py.b2c import B2C

  resp = B2C.process_transaction(
    command_id="BusinessPayment", amount=1000, phone_number="254708374149",
    remarks="Requested on Tuesday", occassion="issue closed"
)
print(resp)
```

3. ### C2B (Customer to Business transaction)
Enables Payments from Client to Business. A customer initiates a payment request to your Pay Bill or Buy Goods (Till Number) \
from their phone. Using the Safaricom app or from M-PESA menu in the Sim Tool Kit. 

The process_transaction  method of the C2B class registers your validation URL and\
confirmation url. it takes the following key word arguments.

***confirmation_url*** --	This is the URL that receives the confirmation request from API upon payment completion.  
***validation_url*** -- This is the URL that receives the validation request from API upon payment submission. \
The validation URL is only called if the external validation on the registered shortcode is enabled. (By default External Validation is dissabled)\

Once you have successfully registered your URL's a confirmation request will be sent to\
your confirmation_url whenever a client completes a transaction.

#### Using mpesa_py in interactive python mode(C2B transaction)
```python
    >>>from mpesa_py.c2b import C2B
    >>>C2B.process_transaction(
       confirmation_url="https://secure-headland-36393.herokuapp.com/api/payments/c2b-confirmation/",
       validation_url="https://secure-headland-36393.herokuapp.com/api/payments/c2b-validation/",
       )
    >>>
```
## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/c_2_b.png)

### sample  python script.
```python
from mpesa_py.c2b import C2B
response = C2B.process_transaction(
    confirmation_url="https://secure-headland-36393.herokuapp.com/api/payments/c2b-confirmation/",
    validation_url="https://secure-headland-36393.herokuapp.com/api/payments/c2b-validation/",
)
print(response)
```

You can use the simulate method of C2B class to simulate a situation where a customer\
pays to a paybill from their phone.

```python3
from mpesa_py.c2b import C2B

>>>resp = C2B.simulate(
    amount=350, customer_phone_no=254708374149,
    short_code=600981
     )
>>>print(resp)
```
## Example


![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/c2b_simulate.png)

4. ### B2B (Business to Business transaction)

The Business to Business (B2B) API is used to transfer money from one business to another business.\
This API enables the business to pay other businesses.\
 The transaction flow is the same as the B2C API transaction flow, but this time the Credit Party is another Business/Company/Organization.\
 It requires the same credentials and information as the B2C API.\
 For the API to work, the 2 organizations will need to have the B2B product assigned to them, otherwise the transaction request will fail.

 The process_transaction method of B2B class takes the following key word arguments.\
***command_id**** --- Takes the following values only.\
_BusinessPayBill_ : This is a transfer of funds from one Organization's Working Account to another Organization's Utility Account\
 _BusinessBuyGoods_: A transfer of funds from one Organization's Working Account to another Organization's Merchant Account\
 _DisburseFundsToBusiness_ : A transfer of funds from one Organization's Utility Account to another Organization's Working Account.\
_BusinessToBusinessTransfer_ : A transfer of funds from one Organization's Working Account to another Organization's Working Account.\
_MerchantToMerchantTransfer_: A transfer of funds from one Organization's Merchant Account to another Organization's Merchant Account\
 ***amount*** --- Is the actual transaction amount.

 ***credit_party*** --- Shortcode for the organization receiving the funds.

 ***b2b_receiver_type***  --- Type of organization receving the transaction\

 ***remarks*** --- Remarks about the transaction.

 ***ocassion*** ---Additional information for the transaction. Optional.


 ## EXAMPLE
 ```python
>>>from mpesa_py.b2b import B2B
>>>resp = B2B.process_transaction(
    command_id="BusinessPayBill", amount=1900,  credit_party=600977, b2b_receiver_type=4,
    remarks="Requested on Tuesday", ocassion="issue closed", account_reference="test_api"
    )
>>>print(resp)

 ```



![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/b2b.png)

5. # Reversal

Reverses a B2B, B2C or C2B M-Pesa transaction.\
The process_transaction method of this class reverses the transaction.\
It takes the following key word arguments.\
***transaction_id*** -- Is the actual transaction id of the transaction you want to\
reverse.\
***amount*** -- The amount transacted in the transaction to be reversed , down to the cent\
***remarks*** -- Comments that are sent along with the transaction.\
***occasion*** -- Optional Parameter that contains additional information for the transaction

### Using mpesa_py in interactive python mode(C2B transaction)
```python
>>>from mpesa_py.reversal import Reversal
>>>response = Reversal.process_transaction(
    transaction_id="PIN51HK4SZ",
    amount=900,
    remarks="Double repayment",
    additional_info="first time customer"
    )
>>>print(response)
```

## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/reversl.png)


6. ## Transaction Status
Checks the status of a transaction.\
The process_transaction method of this class takes the following key word arguments.\
***transaction_id*** -- Is the actual transaction id.\
***remarks*** -- Comments that are sent along with the transaction\
***Occasion*** -- Any Additional information. Optional

The result of this transaction will be sent to your rans_status_result_url defined in your\
environment variables file.

```python
>>>from mpesa_py.trans_status import TransStatus
>>>resp = TransStatus.process_transaction(
          transaction_id="PIR81HK5N2",
          remarks="Double repayment",
          Occasion= "First time customer"
          )
>>>print(resp)

```
## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/status.png)

### NOTE: To check the status of an STK push sent to the customer.
You can use the trans_status method of MpesaExpress class.\
The method takes a single argument ie checkout_request_id that is always sent back\
as a response from the STK/M-Pesa express transaction. This is used to query whether \
the customer did actually complete the STK push sent to their phone number.
```python
>>>from mpesa_py.mpesa_express import MpesaExpress
>>>resp = MpesaExpress.trans_status(
          checkout_request_id="ws_CO_270920212251236524"
          )
>>>print(resp)
```
## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/stk_status.png)

The above STK push was cancelled by the user as seen from the ResultDesc property\
of the response.

7. # Account Balance

Checks the account balance of M-Pesa BuyGoods (Till Number)\
The process transaction method of this class takes the followng keyword arguments\
***account_bal_party*** -- Type of organization receiving the transaction eg 600981 for a\
business shortcode

***acc_bal_identifier_type*** --- Identifies the type of organization.\
1 – MSISDN, 2 – Till Number, 4 – Organization short code

***remarks*** -- Comments that are sent along with the transaction

```python
>>>from mpesa_py.account_balance import AccountBalance
>>>resp = AccountBalance.process_transaction(
          account_bal_party=600981,
          remarks="testing remarks",
          acc_bal_identifier_type=4
          )
>>>print(resp)
```
## Example

![App Screenshot](https://mpesapy.s3.amazonaws.com/static_assets/acc_bal.png)




## LICENCE

mpesa_py  is open-sourced software licensed under the [MIT licence](https://choosealicense.com/licenses/mit/)

## CONTRIBUTING

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

  
## AUTHORS

- David Mutune - Full stack Software engineer  [instagram](https://www.instagram.com/david__mutune/)-----[github](https://www.github.com/kimengu-david)-----[twitter](https://twitter.com/David__mutune)

  