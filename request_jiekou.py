import requests


class request_all():
    def get_request(url):
        r = requests.get('%s'%url)
        return r.text

    def post_request(url):
        r = requests.post('%s'%url)
        print(r.text)

