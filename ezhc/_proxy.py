

import requests as rq
import urllib

from requests.packages.urllib3.exceptions import InsecureRequestWarning
rq.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Proxy:
    """
    proxy object
    """

    def __init__(self,
                 login=None,
                 pwd=None,
                 proxy_host=None,
                 proxy_port=None):
        """
        """
        self.login = login
        self.pwd = pwd
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxies = None

        if self.pwd:
            self.pwd = urllib.parse.quote(self.pwd)

        if self.login:
            dic = {'login': self.login,
                'pwd': self.pwd,
                'proxy_host': self.proxy_host,
                'proxy_port': self.proxy_port}
            self.proxies = {
                'http': 'http://{login}:{pwd}@{proxy_host}:{proxy_port}'.format(**dic),
                'https': 'https://{login}:{pwd}@{proxy_host}:{proxy_port}'.format(**dic)
            }

