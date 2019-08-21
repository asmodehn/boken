import uplink

from .api import Kraken

kraken = Kraken(base_url="https://api.kraken.com/", client=uplink.AiohttpClient())