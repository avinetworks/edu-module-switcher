Controller_Version = "18.2.6"

demo_env_kneitinger= {
    'name' : 'kneitinger',
    'controller_username': "admin",
    'controller_password': "admin",
    'controller_ip': "10.151.20.90",
    'tenant': "admin",
    'api_version': Controller_Version,
    'zap_proxy': "http://10.151.16.40:8080",
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
            'pool_server_ip': "10.151.80.13",
            'pool_server_port': "80",
            'vip_ip': "10.151.80.91",
            'vs_name': "WAF-DVWA-VS",
            'pool_name': "DVWA-Pool",
            'waf_profile_name': "DVWAProfile",
            'waf_policy_name': "DVWAPolicy",
            'error_page_profile_name': "DVWAErrorPage",
            'learning_group_name': 'DVWA_Learning_Group_Demo'
        },
        'Hackazon' : {
            'pool_server_ip': "10.151.16.40",
            'pool_server_port': "8888",
            'vip_ip': "10.151.80.92",
            'vs_name': "WAF-Hackazon-VS",
            'pool_name': "Hackazon-Pool",
            'waf_profile_name': "HackazonProfile",
            'waf_policy_name': "HackazonPolicy",
            'error_page_profile_name': "HackazonErrorPage",
            'learning_group_name': 'Hackazon_Learning_Group_Demo'
        }
    }
}

demo_env_wbh= {
    'name' : 'Weissbrauhaus',
    'controller_username': "admin",
    'controller_password': "admin",
    'controller_ip': "10.151.20.86",
    'tenant': "admin",
    'api_version': Controller_Version,
    'zap_proxy': "http://10.151.16.40:8080",
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
            'pool_server_ip': "10.151.80.13",
            'pool_server_port': "80",
            'vip_ip': "10.151.80.87",
            'vs_name': "WAF-DVWA-VS",
            'pool_name': "DVWA-Pool",
            'waf_profile_name': "DVWAProfile",
            'waf_policy_name': "DVWAPolicy",
            'error_page_profile_name': "DVWAErrorPage",
            'learning_group_name': 'DVWA_Learning_Group_Demo'
        },
        'Hackazon' : {
            'pool_server_ip': "10.151.16.40",
            'pool_server_port': "8888",
            'vip_ip': "10.151.80.88",
            'vs_name': "WAF-Hackazon-VS",
            'pool_name': "Hackazon-Pool",
            'waf_profile_name': "HackazonProfile",
            'waf_policy_name': "HackazonPolicy",
            'error_page_profile_name': "HackazonErrorPage",
            'learning_group_name': 'Hackazon_Learning_Group_Demo'
        }
    }
}

demo_env_vmware_us= {
    'name' : 'Stratocaster',
    'controller_username': "admin",
    'controller_password': "admin",
    'controller_ip': "10.79.110.253",
    'tenant': "admin",
    'api_version': Controller_Version,
    'zap_proxy': "http://10.79.111.22:8090",
    'proxies': {
            # Only needed for VMware Lab Testbeds
            "http": "http://aviuser:avi123@10.79.111.22:6666",
            "https": "http://aviuser:avi123@10.79.111.22:6666",
            },
    'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'X-AVI-VERSION': Controller_Version
            },
    'vses': {
        'DVWA' : {
            'pool_server_ip': "100.64.3.12",
            'pool_server_port': "80",
            'vip_ip': "100.64.3.91",
            'vs_name': "WAF-DVWA-VS",
            'pool_name': "DVWA-Pool",
            'waf_profile_name': "DVWAProfile",
            'waf_policy_name': "DVWAPolicy",
            'error_page_profile_name': "DVWAErrorPage",
            'learning_group_name': 'DVWA_Learning_Group_Demo'
        },
        'Hackazon' : {
            'pool_server_ip': "100.64.3.12",
            'pool_server_port': "8888",
            'vip_ip': "100.64.3.92",
            'vs_name': "WAF-Hackazon-VS",
            'pool_name': "Hackazon-Pool",
            'waf_profile_name': "HackazonProfile",
            'waf_policy_name': "HackazonPolicy",
            'error_page_profile_name': "HackazonErrorPage",
            'learning_group_name': 'Hackazon_Learning_Group_Demo'
        }
    }
}

demo_env_diagonalley= {
    'name' : 'diagonalley',
    'controller_username': "admin",
    'controller_password': "avi123",
    'controller_ip': "10.79.110.99",
    'tenant': "admin",
    'api_version': Controller_Version,
    'zap_proxy': "http://10.79.110.113:8080",
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
            'pool_server_ip': "100.64.88.14",
            'pool_server_port': "80",
            'vip_ip': "10.79.109.85",
            'vs_name': "WAF-DVWA-VS",
            'pool_name': "DVWA-Pool",
            'waf_profile_name': "DVWAProfile",
            'waf_policy_name': "DVWAPolicy",
            'error_page_profile_name': "DVWAErrorPage",
            'learning_group_name': 'DVWA_Learning_Group_Demo'
        },
        'Hackazon' : {
            'pool_server_ip': "100.64.88.14",
            'pool_server_port': "8080",
            'vip_ip': "10.79.109.84",
            'vs_name': "WAF-Hackazon-VS",
            'pool_name': "Hackazon-Pool",
            'waf_profile_name': "HackazonProfile",
            'waf_policy_name': "HackazonPolicy",
            'error_page_profile_name': "HackazonErrorPage",
            'learning_group_name': 'Hackazon_Learning_Group_Demo'
        }
    }
}

demo_env_vmware_lab = {
    'name' : 'vmware_lab',
    'controller_username': "admin",
    'controller_password': "VMware1!",
    'controller_ip': "sa-avicon-01.vclass.local",
    'tenant': "admin",
    'api_version': "18.2.6",
    'zap_proxy': "http://172.17.0.3:8080",
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


