import json
import urllib.request

import utils.constants
import utils.rate_limiter


def open(url):
    for char in url:
        if char in utils.constants.URL_CODES:
            url = url.replace(char, utils.constants.URL_CODES[char])

    if utils.constants.URL_V1 in url:
        url += f"&apikey={utils.constants.API_KEY}"
    
    req = urllib.request.Request(url, headers={"apikey": utils.constants.API_KEY})
    
    res = urllib.request.urlopen(req, timeout=utils.constants.TIMEOUT)
    
    utils.rate_limiter.limit(res.info())

    return json.loads(res.read().decode("utf-8"))
