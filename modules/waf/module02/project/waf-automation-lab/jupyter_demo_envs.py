Controller_Version = "18.2.6"

demo_env_vmware_lab = {
    'name' : 'vmware_lab',
    'controller_username': "admin",
    'controller_password': "VMware1!",
    'controller_ip': "sa-avicon-01.vclass.local",
    'tenant': "admin",
    'api_version': "18.2.6",
    'zap_proxy': "http://sa-avitools-01:8080",
    'proxies': {
            # Only needed for VMware Lab Testbeds
            },
    'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'X-AVI-VERSION': Controller_Version
            },
    'vses': {
        'DVWA' : {
            'pool_server_ip': "172.20.130.102",
            'pool_server_port': "80",
            'vip_ip': "172.20.120.250",
            'vs_name': "WAF-DVWA-VS",
            'pool_name': "WAF-DVWA-Pool",
            'waf_profile_name': "WAF-DVWAProfile",
            'waf_policy_name': "WAF-DVWAPolicy",
            'error_page_profile_name': "WAF-DVWAErrorPage",
            'learning_group_name': 'WAF-DVWA_Learning_Group_Demo',
            'vs_fqdn': "WAF-DVWA-VS.sa.vclass.local"
        },
        'Hackazon' : {
            'pool_server_ip': "172.20.130.102",
            'pool_server_port': "30080",
            'vip_ip': "172.20.120.251",
            'vs_name': "WAF-Hackazon-VS",
            'pool_name': "WAF-Hackazon-Pool",
            'waf_profile_name': "WAF-HackazonProfile",
            'waf_policy_name': "WAF-HackazonPolicy",
            'error_page_profile_name': "WAF-HackazonErrorPage",
            'learning_group_name': 'WAF-Hackazon_Learning_Group_Demo',
            'vs_fqdn': "waf-hackazon-vs.sa.vclass.local"
        }
    }
}


