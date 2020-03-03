testbeds = {
    'wbh' : {
        'controller_username': "admin",
        'controller_password': "admin",
        'controller_ip': "10.151.20.86",
        'tenant': "admin",
        'api_version': "18.2.4",
        'vses': {
            'DVWA' : {
                'pool_server_ip': "10.151.80.13",
                'pool_server_port': "80",
                # vip name https://wbh-vs1.local
                'vip_ip': "10.151.80.87",
                'vs_name': "WAF-DVWA-VS",
                'pool_name': "DVWA-Pool",
                'waf_profile_name': "DVWAProfile",
                'waf_policy_name': "DVWAPolicy",
                'error_page_profile_name': "DVWAErrorPage"
            },
            'Hackazon' : {
                'pool_server_ip': "10.151.16.40",
                'pool_server_port': "8888",
                # vip name https://wbh-vs2.local
                'vip_ip': "10.151.80.88",
                'vs_name': "WAF-Hackazon-VS",
                'pool_name': "Hackazon-Pool",
                'waf_profile_name': "HackazonProfile",
                'waf_policy_name': "HackazonPolicy",
                'error_page_profile_name': "HackazonErrorPage"
            }
        }
    },
    'kuchlbaur' : {
        'controller_username': "admin",
        'controller_password': "admin",
        'controller_ip': "10.151.20.97",
        'tenant': "admin",
        'api_version': "18.2.4",
        'vses': {
            'DVWA' : {
                'pool_server_ip': "10.151.80.13",
                'pool_server_port': "80",
                # vip name https://wbh-vs1.local
                'vip_ip': "10.151.80.98",
                'vs_name': "WAF-DVWA-VS",
                'pool_name': "DVWA-Pool",
                'waf_profile_name': "DVWAProfile",
                'waf_policy_name': "DVWAPolicy",
                'error_page_profile_name': "DVWAErrorPage"
            },
            'Hackazon' : {
                'pool_server_ip': "10.151.16.40",
                'pool_server_port': "8888",
                # vip name https://wbh-vs2.local
                'vip_ip': "10.151.80.99",
                'vs_name': "WAF-Hackazon-VS",
                'pool_name': "Hackazon-Pool",
                'waf_profile_name': "HackazonProfile",
                'waf_policy_name': "HackazonPolicy",
                'error_page_profile_name': "HackazonErrorPage"
            }
        }
    },
    'kneitinger' : {
        'controller_username': "admin",
        'controller_password': "admin",
        'controller_ip': "10.151.20.90",
        'tenant': "admin",
        'api_version': "18.2.4",
        'vses': {
            'DVWA' : {
                'pool_server_ip': "10.151.80.13",
                'pool_server_port': "80",
                # vip name https://wbh-vs1.local
                'vip_ip': "10.151.80.91",
                'vs_name': "WAF-DVWA-VS",
                'pool_name': "DVWA-Pool",
                'waf_profile_name': "DVWAProfile",
                'waf_policy_name': "DVWAPolicy",
                'error_page_profile_name': "DVWAErrorPage"
            },
            'Hackazon' : {
                'pool_server_ip': "10.151.16.40",
                'pool_server_port': "8888",
                # vip name https://wbh-vs2.local
                'vip_ip': "10.151.80.92",
                'vs_name': "WAF-Hackazon-VS",
                'pool_name': "Hackazon-Pool",
                'waf_profile_name': "HackazonProfile",
                'waf_policy_name': "HackazonPolicy",
                'error_page_profile_name': "HackazonErrorPage"
            }
        }
    },
    'spital' : {
        'controller_username': "admin",
        'controller_password': "admin",
        'controller_ip': "10.151.20.94",
        'tenant': "admin",
        'api_version': "18.2.3",
        'vses': {
            'DVWA' : {
                'pool_server_ip': "10.151.80.13",
                'pool_server_port': "80",
                # vip name https://wbh-vs1.local
                'vip_ip': "10.151.80.95",
                'vs_name': "WAF-DVWA-VS",
                'pool_name': "DVWA-Pool",
                'waf_profile_name': "DVWAProfile",
                'waf_policy_name': "DVWAPolicy",
                'error_page_profile_name': "DVWAErrorPage"
            },
            'Hackazon' : {
                'pool_server_ip': "10.151.16.40",
                'pool_server_port': "8888",
                # vip name https://wbh-vs2.local
                'vip_ip': "10.151.80.96",
                'vs_name': "WAF-Hackazon-VS",
                'pool_name': "Hackazon-Pool",
                'waf_profile_name': "HackazonProfile",
                'waf_policy_name': "HackazonPolicy",
                'error_page_profile_name': "HackazonErrorPage"
            }
        }
    },
    'diagonalley' : {
        'controller_username': "admin",
        'controller_password': "avi123",
        'controller_ip': "10.79.110.99",
        'tenant': "admin",
        'api_version': "18.2.3",
        'vses': {
            'DVWA' : {
                'pool_server_ip': "100.64.88.14",
                'pool_server_port': "80",
                'vip_ip': "10.79.109.85",
                'vs_name': "WAF-DVWA-VS",
                'pool_name': "DVWA-Pool",
                'waf_profile_name': "DVWAProfile",
                'waf_policy_name': "DVWAPolicy",
                'error_page_profile_name': "DVWAErrorPage"
            },
            'Hackazon' : {
                'pool_server_ip': "100.64.88.14",
                'pool_server_port': "8080",
                'vip_ip': "10.79.109.84",
                'vs_name': "WAF-Hackazon-VS",
                'pool_name': "Hackazon-Pool",
                'waf_profile_name': "HackazonProfile",
                'waf_policy_name': "HackazonPolicy",
                'error_page_profile_name': "HackazonErrorPage"
            }
        }
    }
}
