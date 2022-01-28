import requests
import json


tg_api_token = '5184647613:AAEPob6ZN6Pvm6PlOEbIpdYnjnY21635Mqk'
tg_chat_id = '922463874'

def send_tg_message(text='Cell execution completed.'):
    requests.post(
        'https://api.telegram.org/' +
        'bot{}/sendMessage'.format(tg_api_token),
        params=dict(chat_id=tg_chat_id, text=text)
    )

url = 'https://cms-v3.neuro.net/logs-v2/main?lng=en&agent_uuid=d501d2cc-c0a1-4133-8b17-87b7a92da937&start=26-10-2021%2011:12:27&end=26-01-2022%2011:12:27/latest'
while True:
    r = requests.get(url)
    time.sleep(1)
    print('STATUS_CODE: ', r.status_code)
    if r.status_code >= 300:
        send_tg_message('Error')