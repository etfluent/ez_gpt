import sys
import requests


def gpt_request(gpt_token: str, gpt_text: str, gpt_temp: float = 0.1) -> None:
    gpt_api_url = 'https://api.openai.com/v1/chat/completions'
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

    gpt_response = requests.post(url=gpt_api_url, headers=gpt_headers, json=gpt_data)
    print(gpt_response.text)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        gpt_request(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    else:
        gpt_request(sys.argv[1], sys.argv[2])
