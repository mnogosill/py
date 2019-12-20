#!/usr/bin/env python

import requests



token='991952168:AAFDCJ3bnrQnf5RcDZAfaK0r6fogu_SQ0_E'



playload ={
    'chat_id': 136090087,
    'text': 'Что там?',
    'reply_to_message_id': 2
}

base_url = f'https://api.telegram.org/bot{token}'
r = requests.post(f'{base_url}/sendMessage', data=playload)
print(r.json())