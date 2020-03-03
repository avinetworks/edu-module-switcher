from avi.sdk.avi_api import ApiSession

from requests.packages import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def testbed_cleanup(testbed):
    api = ApiSession.get_session(
        controller_ip=testbed['controller_ip'],
        username=testbed['controller_username'],
        password=testbed['controller_password'],
        tenant=testbed['tenant'],
        api_version=testbed['api_version']
        )

    for name, vs in testbed['vses'].items():
        print("Cleaning up Demo:" + name)
        try:
            resp = api.delete_by_name('virtualservice', vs['vs_name'])
            print("- Delete Virtual Service:", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('pool', vs['pool_name'])
            print("- Delete Pool:", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('errorpageprofile', vs['error_page_profile_name'])
            print("- Delete ErrorPageProfile", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('wafpolicy', vs['waf_policy_name'])
            print("- Delete WAFPolicy:", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('wafprofile', vs['waf_profile_name'])
            print("- Delete WAFProfile:", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('wafpolicypsmgroup', vs['learning_group_name'])
            print("- Delete LearningGroup:", resp, resp.text)
        except Exception as e:
            print(e)
        try:
            resp = api.delete_by_name('vsdatascriptset', "DS-SET-Request-ID-Header-%s" %vs['waf_policy_name'])
            print("- Delete DataScriptSets:", resp, resp.text)
        except Exception as e:
            print(e)