import requests


class GetSource():
    @staticmethod
    def get_source_code(url):

        headers = {
            'user-agent':
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"
        html = response.text
        return html