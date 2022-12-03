import requests
from django.conf import settings

class Paystack:

    paystack_secret_key = settings.PAYSTACK_SECRET_KEY
    base_url = 'https://api.paystack.co'

    def verrify_payment(self, ref):
        link = f'/transaction/verify/{ref}'

        header = {
            "Authorization": f"Bearer {self.paystack_secret_key}",
            "Content-Type": 'application/json'
        }

        url = self.base_url + link

        response = requests.get(url, headers=header)

        if response.status_code == 200:
            data = response.json()

            return data['status']
        data = response.json()
        return data['status']