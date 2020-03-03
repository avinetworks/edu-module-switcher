import json

from avi.sdk.avi_api import ApiSession

from requests.packages import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def testbed_setup(testbed):
    print(f"Data for Testbed {testbed['name'].capitalize()}")
    print(f"Controller IP: {testbed['controller_ip']}")
    print(f"DVWA VIP: {testbed['vses']['DVWA']['vip_ip']}")
    print(f"DVWA FQDN: {testbed['vses']['DVWA']['vs_fqdn']}")
    print(f"Hackazon VIP: {testbed['vses']['Hackazon']['vip_ip']}")
    print(f"Hackazon FQDN: {testbed['vses']['Hackazon']['vs_fqdn']}")
    api = ApiSession.get_session(
        controller_ip=testbed['controller_ip'],
        username=testbed['controller_username'],
        password=testbed['controller_password'],
        tenant=testbed['tenant'],
        api_version=testbed['api_version']
        )

    for name, vs in testbed['vses'].items():
        print("Setting up Demo VS:" + name)
        pool_obj = {
            "lb_algorithm": 'LB_ALGORITHM_LEAST_CONNECTIONS',
            "default_server_port": 80,
            "name": vs['pool_name'],
            "servers": [
                {
                    'ip' : {
                        'addr' : vs['pool_server_ip'],
                        'type' : 'V4',
                    },
                    'port' : vs['pool_server_port'],
                }
            ],
            "health_monitor_refs": [],
        }

        resp = api.post('pool', data=json.dumps(pool_obj))
        print('- Create Pool', resp)

        get_pool_obj = api.get_object_by_name('pool', vs['pool_name'])
        pool_ref = api.get_obj_ref(get_pool_obj)

        get_waf_profile = api.get_object_by_name('wafprofile', 'System-WAF-Profile')
        get_waf_profile['name'] = vs['waf_profile_name']
        resp = api.post('wafprofile', get_waf_profile)
        print("- Create new WAF profile", resp)
        get_profile_obj = api.get_object_by_name('wafprofile', vs['waf_profile_name'])
        profile = api.get_obj_ref(get_profile_obj)


        get_waf_obj = api.get_object_by_name('wafpolicy', 'System-WAF-Policy')
        get_waf_obj['name'] = vs['waf_policy_name']
        get_waf_obj['waf_profile_ref'] = profile

        resp = api.post('wafpolicy', get_waf_obj)
        print("- Create new WAF Policy", resp)
        get_waf_obj = api.get_object_by_name('wafpolicy', vs['waf_policy_name'])
        waf_ref = api.get_obj_ref(get_waf_obj)
        # print "WAF", waf_ref

        backupconf = api.get_object_by_name('backupconfiguration', 'Backup-Configuration')
        backupconf['backup_passphrase'] = 'notpresenttoavoiderror'
        resp = api.put('backupconfiguration/%s' %backupconf['uuid'], backupconf)
        # print("Change Backup Configuration defaults", resp.text)

        error_page_body = api.get_object_by_name('errorpagebody', 'Custom-Error-Page')
        error_page_body_ref = api.get_obj_ref(error_page_body)

        error_page_profile = {
            'error_pages': [{
                'enable': True,
                'error_page_body_ref': error_page_body_ref,
                'index': 0,
                'match': {'match_criteria': 'IS_IN', 'status_codes': [403]}}],
            'name': vs['error_page_profile_name'],
        }

        resp = api.post('errorpageprofile', error_page_profile)
        print("- Create new Error Page Profile", resp)

        error_page_profile = api.get_object_by_name('errorpageprofile', vs['error_page_profile_name'])
        error_page_profile_ref = api.get_obj_ref(error_page_profile)

        # Add Datascript for Request-ID response Header
        dsname = "Request-ID-Header-%s" %vs['waf_policy_name']
        dsobject = {
           "evt" :  "VS_DATASCRIPT_EVT_HTTP_RESP",
           "script" : """r = avi.http.get_request_id()
                         if r == nil then
                           r = "none"
                         end
                         avi.http.add_header( "X-Request-Id", r )""",
           "name" : dsname,

        }
        dssetname = "DS-SET-Request-ID-Header-%s" %vs['waf_policy_name']
        dssetobject = {
            'datascript' : [
                dsobject,
            ],
            'name' : dssetname
        }
        resp = api.post('vsdatascriptset', data=json.dumps(dssetobject))
        print("- Create new Response Data Script", resp)

        ds = api.get_object_by_name('vsdatascriptset', dssetname)
        ds_ref = api.get_obj_ref(ds)

        # Creating VS
        services_obj = [{'port': 80, 'enable_ssl': False},{'port': 443, 'enable_ssl': True}]
        vs_obj = {
            'name': vs['vs_name'],
            'type': 'VS_TYPE_NORMAL',
            'vip': [{
                'ip_address': {
                    'addr': vs['vip_ip'],
                    'type': 'V4'
                },}],
            'dns_info': [{
                     'fqdn': vs['vs_fqdn']
            }],
            'enabled': True,
            'services': services_obj,
            'application_profile_name': 'System-HTTP',
            'error_page_profile_ref': error_page_profile_ref,
            'pool_ref': pool_ref,
            'waf_policy_ref' : waf_ref,
            'vs_datascripts' : [
                { 
                    'index' : 1,
                    'vs_datascript_set_ref' : ds_ref
                }
            ],
            'analytics_policy': {
                'udf_log_throttle': 10,
                'full_client_logs': {
                    'duration': 0,
                    'throttle': 10,
                    'enabled': True
                },
                'metrics_realtime_update': {
                    'duration': 0,
                    'enabled': True
                },
                'significant_log_throttle': 10,
                'client_insights': 'NO_INSIGHTS',
                'all_headers': True
            }
        }

        resp = api.post('virtualservice', data=json.dumps(vs_obj))
        print("- Create VS with new WAF Policy", resp) #, resp.text

    print('Setup done.')
