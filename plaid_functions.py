import os
import plaid
from plaid.api import plaid_api

#sandbox environment
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

#from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest

from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest

from plaid.model.products import Products


def plaid_client():
    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': os.environ['PLAID_CLIENT_ID'],
            'secret': os.environ['PLAID_SECRET'],
        }
    )
    print("plaid client created")
    client = plaid_api.PlaidApi(plaid.ApiClient(configuration))
    return client


def plaid_sandbox_request_public_token():

    client = plaid_client()
    print("pub tok request")
    request = SandboxPublicTokenCreateRequest(
        institution_id='ins_109508',
        initial_products=[Products('transactions')]
    )
    try:
        response = client.sandbox_public_token_create(request) 
    except plaid.ApiException as e:
        print('plaid error: ', e.body)
        raise
    except Exception as e:
        print('error: ', type(e).__name__, e)
        raise
    public_token = response['public_token']
    print(f"Public Token: {public_token}")
    return public_token

def plaid_exchange_public_token(public_token):
    print("tok exchange")
    client = plaid_client()
    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )
    response = client.item_public_token_exchange(request)
    access_token = response['access_token']
    ##add this access token to the database for the user after encrypting it
    ##db.add_access_token(user_id, access_token)
    return access_token

def plaid_get_accounts(access_token):
    print("get accounts")
    client = plaid_client()
    request = AccountsGetRequest(
        access_token=access_token
    )
    response = client.accounts_get(request)
    ##TODO: remove print statements
    for account in response['accounts']:
        print(f"Account: {account['name']}\nType: {account["type"]}\nBalcance: {account['balances']['current']}\n")
    return response['accounts']