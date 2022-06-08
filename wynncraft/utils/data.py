import wynncraft.utils.cache as cache
import wynncraft.utils.request as request
from wynncraft.utils.constants import CACHE_TIME

def get(url):
    id = (url.removeprefix("https://api.wynncraft.com/public_api.php?action=")
             .removeprefix("https://api.wynncraft.com/v2/"))
    
    if CACHE_TIME and cache.exists_valid_data(id):
        return cache.read_json()["data"][id]
    else:
        data = request.get(url)
        
        if CACHE_TIME:
            cache.write_json(id, data)
        
        return data
