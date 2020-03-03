import json
import pprint
import requests
from requests.packages import urllib3

urllib3.disable_warnings()

def add_whitelist_examples(testbed, headers, proxies):
    print(f"Data for Testbed {testbed['name'].capitalize()}")
    print(f"Controller IP: {testbed['controller_ip']}")
#    print(f"DVWA VIP: {testbed['vses']['DVWA']['vip_ip']}")
#    print(f"Hackazon VIP: {testbed['vses']['Hackazon']['vip_ip']}")

    # SET THESE ITEMS to work on your machine
    server = testbed['controller_ip']
    wafpolicy_name = testbed['vses']['Hackazon']['waf_policy_name']

    # Headers for all REST calls
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'X-AVI-VERSION': '18.2.3'}

    # Get the WAF Policy, where the whitelist should be added
    r = requests.get(f'https://{server}/api/wafpolicy/?name={wafpolicy_name}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False)
    wafpolicy = r.json()['results'][0]


    whitelist = """{
        "rules": [
            {
            "index": 0,
            "name": "whitelist-path-files",
            "match": {
                "path": {
                    "match_criteria": "BEGINS_WITH",
                    "match_case": "INSENSITIVE",
                        "match_str": [
                            "/css"
                        ]
                    }
                },
                "actions": [
                    "WAF_POLICY_WHITELIST_ACTION_ALLOW"
                    ]
            },
            {
                "index": 1,
                "name": "whitelist-example-IPs",
                "match": {
                    "client_ip": {
                        "match_criteria": "IS_IN",
                        "ranges": [
                            {
                                "begin": {
                                    "addr": "192.168.0.0",
                                    "type": "V4"
                                },
                                "end": {
                                    "addr": "192.168.255.255",
                                    "type": "V4"
                                }
                            }
                        ]
                    }
                },
                "actions": [
                    "WAF_POLICY_WHITELIST_ACTION_ALLOW"
                    ]
            },
            {
                "index": 2,
                "name": "Detection mode for /contact",
                "match": {
                    "path": {
                        "match_criteria": "BEGINS_WITH",
                        "match_str": ["/contact"],
                        "match_case": "INSENSITIVE"
                    }
                },
                "actions": [
                    "WAF_POLICY_WHITELIST_ACTION_DETECTION_MODE"
                    ]
            }
        ]
    }"""

    wafpolicy['whitelist'] = json.loads(whitelist)
    print('Adding whitelist entries to WAFPolicy:')
    r = requests.put(f'https://{server}/api/wafpolicy/{wafpolicy["uuid"]}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False, json=wafpolicy)
    wafpolicy = r.json()
    #pprint.pprint(wafpolicy['whitelist'])
    if r.status_code <= 300:
        print(r)
        print("Added Whitelist rules for css files, IPs and Detection mode for /contact")
    else:
        print("An error occured. Please check the Whitelist entries")
        print(r.text)