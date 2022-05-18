from bs4 import BeautifulSoup
import requests, re
from time import sleep
from urllib.parse import urlparse

def getLink(url):
    try:
        client = requests.Session()
        res = client.get(url, timeout=5)
        ref = re.findall("action[ ]{0,}=[ ]{0,}['|\"](.*?)['|\"]", res.text)[0]
        h = {'referer': ref}
        res = client.get(url, headers=h)
        bs4 = BeautifulSoup(res.content, 'html.parser')
        inputs = bs4.find_all('input')
        data = { input.get('name'): input.get('value') for input in inputs }
        h = {
            'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
        }
        p = urlparse(url)
        final_url = f'{p.scheme}://{p.netloc}/links/go'
        sleep(3.1)
        res = client.post(final_url, data=data, headers=h).json()
        if res['status'] == 'success':
            return res['url']
        return None
    except Exception as e:
        print(e)
        return None


print(getLink("https://droplink.co/mIIxX"))