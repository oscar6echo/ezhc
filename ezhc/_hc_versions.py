
import json
import requests as rq
from ._proxy import Proxy


def get_hc_versions(proxy=None):
    """
    retrieve highcharts versions
    """

    proxies = {}
    if proxy:
        assert isinstance(proxy, Proxy)
        proxies = proxy.proxies

    url = 'https://registry.npmjs.org/highcharts'
    headers = {'Accept': 'application/vnd.npm.install-v1+json'}

    try:
        r = rq.get(url, headers=headers)
        res = json.loads(r.content.decode('utf-8'))
        versions = list(res['versions'].keys())

    except:
        # to be updated from time to time
        versions = [
            '0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6', '0.0.8', '0.0.9', '0.0.10',
            '0.0.11', '4.1.10', '4.2.0', '4.2.1', '4.2.2', '4.2.3', '4.2.4', '4.2.5', '4.2.6',
            '4.2.7', '5.0.0', '5.0.1', '5.0.2', '5.0.3', '5.0.4', '5.0.5', '5.0.6', '5.0.7',
            '5.0.8', '5.0.9', '5.0.10', '5.0.11', '5.0.12', '5.0.13', '5.0.14', '6.0.0', '6.0.1',
            '6.0.2', '6.0.3', '6.0.4', '6.0.5', '6.0.6', '6.0.7', '5.0.15', '6.1.0', '6.1.1',
            '6.1.2']

    return versions
