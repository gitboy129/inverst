import requests
import uuid

class transferwise :
    def __init__(self) :
        self.headers = {
                        'Accept':          '*/*',
                        'Accept-Encoding': 'gzip, deflate',
                        'Content-Type':    'application/json',
                        'Authorization':   'Bearer ec50cd47-25bc-4db6-9ad0-3b03de013277',
                        }

    def auth(self) :
        r = requests.post('https://api.transferwise.com/oauth/token', data=data, headers=self.headers)

    def get_profile(self) :
        r = requests.get('https://api.transferwise.com/v1/profiles', headers=self.headers)

        return r.json()

    def get_quote(self, profile='', amount=0) :
        data = {'profile':              str(profile),
                'sourceCurrency':       'JPY',
                'targetCurrency':       'USD',
                'sourceAmount':         amount,
                # 'targetAmount':         0
                }

        r = requests.post('https://api.transferwise.com/v2/quotes', json=data, headers=self.headers)
        # r = requests.post('https://api.sandbox.transferwise.tech/v1/quotes', data=data, headers=self.headers)

        return r.json()

    def get_accounts(self, profile='', currency='USD') :
        r = requests.get('https://api.transferwise.com/v1/accounts?profile=' + str(profile) + '&currency=' + currency, headers=self.headers)
        # r = requests.post('https://api.sandbox.transferwise.tech/v1/quotes', data=data, headers=self.headers)

        return r.json()

    def create_transfer(self, quote_id='', account='') :
        data = {'targetAccount':            str(account),
                'quoteUuid':                quote_id,
                'customerTransactionId':    str(uuid.uuid4()),
                'details' : {   'transferPurpose'   : 'verification.transfers.purpose.pay.bills',
                                'sourceOfFunds'     : 'verification.source.of.funds.other'}
                # 'targetAmount':         0
                }

        r = requests.post('https://api.transferwise.com/v1/transfers', json=data, headers=self.headers)

        return r.json()

    def cancel_transfer(self, id) :
        r = requests.put('https://api.transferwise.com/v1/transfers/' + str(id) + '/cancel', headers=self.headers)

        return r.json()

if __name__ == '__main__' :
    tw = transferwise()
    tw.cancel_transfer('112912208')