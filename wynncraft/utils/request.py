import json
import urllib.request

import utils.constants
import utils.rate_limiter


def open(url):
    for char in url:
        if char in utils.constants.URL_CODES:
            url = url.replace(char, utils.constants.URL_CODES[char])
    
    res = urllib.request.urlopen(url, timeout=utils.constants.DEFAULT_TIMEOUT)

    utils.rate_limiter.limit(res.info())

    return json.loads(res.read().decode("utf-8"))
