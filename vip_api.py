import json
from urllib.parse import urljoin

import requests
import constants


class Vip(object):

    def __init__(self):
        pass

    def get_banner_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.BANNER_V1_URL, verify=False)

        if response.ok:
            return response
        else:
            return None