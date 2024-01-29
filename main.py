import sys

import requests


def gpt_request(gpt_token, gpt_text, gpt_temp=0.1):
    gpt_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {gpt_token}'
    }

    gpt_data = {
        'model': "gpt-3.5-turbo",
        'messages': {
            'role': 'user',
            'content': gpt_text
        },
        'temperature': gpt_temp
    }

    response = requests.post('https://api.openai.com/v1/chat/completions',
                             headers=gpt_headers,
                             json=gpt_data
                             )
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        gpt_request(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    else:
        gpt_request(sys.argv[1], sys.argv[2])
