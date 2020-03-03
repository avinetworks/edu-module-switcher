from pprint import pprint
import requests
from requests.packages import urllib3

urllib3.disable_warnings()

def setup_learning(testbed, headers, proxies):
    print(f"Data for Testbed {testbed['name'].capitalize()}")
    print(f"Controller IP: {testbed['controller_ip']}")
    print(f"DVWA VIP: {testbed['vses']['DVWA']['vip_ip']}")
    print(f"Hackazon VIP: {testbed['vses']['Hackazon']['vip_ip']}")

    # SET THESE ITEMS to work on your machine
    server = testbed['controller_ip']
    wafpolicy_name = testbed['vses']['Hackazon']['waf_policy_name']
    wafprofile_name =  testbed['vses']['Hackazon']['waf_profile_name']

    # Headers for all REST calls
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'X-AVI-VERSION': '18.2.5'}

    print(f"Enable Learning on Policy - {wafpolicy_name} and Profile - {wafprofile_name}")

    # Get the WAF Policy, where the PSM should be added
    r = requests.get(f'https://{server}/api/wafpolicy/?name={wafpolicy_name}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False)
    wafpolicy = r.json()['results'][0]
    wafpolicy['enable_app_learning'] = True
    r = requests.put(f'https://{server}/api/wafpolicy/{wafpolicy["uuid"]}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False, json=wafpolicy)
    #pprint(r.json())

    r = requests.get(f'https://{server}/api/wafprofile/?name={wafprofile_name}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False)
    #print(r.json())
    wafprofile = r.json()['results'][0]
    wafprofile['config'] = {}

    wafprofile['config']['learning_params'] = {}
    wafprofile['config']['learning_params']['sampling_percent'] = 100
    wafprofile['config']['learning_params']['enable_per_uri_learning'] = True
    wafprofile['config']['learning_params']['update_interval'] = 1
    wafprofile['config']['learning_params']['max_params'] = 1000
    wafprofile['config']['learning_params']['max_uris'] = 1000
    wafprofile['config']['learning_params']['min_hits_to_learn'] = 10
    wafprofile['config']['enable_auto_rule_updates'] = True
    r = requests.put(f'https://{server}/api/wafprofile/{wafprofile["uuid"]}', auth=(testbed["controller_username"], testbed["controller_password"]), headers=headers, proxies = proxies, verify=False, json=wafprofile)
    print("Result:", r.status_code, "OK")
    #print("Learning parameters set:")
    #pprint(r.json()['config']['learning_params'])

def setup_positive_security_group(api, demo_env, headers, proxies):
    psmgroup = {
        'enable': True,
        'hit_action': 'WAF_ACTION_ALLOW_PARAMETER',
        'is_learning_group': True,
        'miss_action': 'WAF_ACTION_BLOCK',
        'name': demo_env['vses']['Hackazon']['learning_group_name'],
        'tenant_ref': 'https://10.151.20.90/api/tenant/admin'
    }

    api.post('wafpolicypsmgroup', psmgroup)
    psmgroup = api.get_object_by_name('wafpolicypsmgroup', demo_env['vses']['Hackazon']['learning_group_name'])
    #pprint(psmgroup)

    wafpolicy_object = api.get_object_by_name('wafpolicy', demo_env['vses']['Hackazon']['waf_policy_name'])
    wafpolicy_object['mode'] = "WAF_MODE_ENFORCEMENT"
    wafpolicy_object['enable_app_learning'] = True
    wafpolicy_object['positive_security_model'] = {}
    wafpolicy_object['positive_security_model']['group_refs'] = []
    wafpolicy_object['positive_security_model']['group_refs'].append(psmgroup['url'])

    api.put_by_name('wafpolicy', demo_env['vses']['Hackazon']['waf_policy_name'], wafpolicy_object)
    pprint('PSMGroup ' + demo_env['vses']['Hackazon']['learning_group_name'] + ' has been set.')

