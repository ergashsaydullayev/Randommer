import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint="Finance/CryptoAddress/Types"
        url=self.get_url()+endpoint  # https://randommer.io/api/Finance/CryptoAddress/Types

        headers={
            "X-Api-Key": api_key
        }

        response=requests.get(url, headers=headers)

        if response.status_code==200:
            return response.json()
        return response.status_code

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        pass

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        pass

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        pass
token = "2d794c6f46094ceb96bd719c1c26c984"
card = Finance()
print(card.get_crypto_address_types(api_key=token))