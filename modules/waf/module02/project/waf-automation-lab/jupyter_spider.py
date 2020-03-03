import sys
import time
from zapv2 import ZAPv2

HELP_STR = '''
Example
    python3 spider.py -t http://10.151.80.88 -k avi123 -p http://docker.avi.works:8080 -l 1
'''

def run_zap_spider(target, proxy, loop, apikey="avi123"):

    # By default ZAP API client will connect to port 8080
    zap = ZAPv2(apikey=apikey, proxies={'http': proxy})
    #zap.core.set_option_use_proxy_chain(boolean=True)
    #zap.core.set_option_proxy_chain_name(string="10.79.111.22")
    #zap.core.set_option_proxy_chain_skip_name(string='127.0.0.1;')
    #zap.core.set_option_proxy_chain_port(integer=6666)
    #zap.core.set_option_use_proxy_chain_auth(boolean=True)
    #zap.core.set_option_proxy_chain_user_name(string="aviuser")
    #zap.core.set_option_proxy_chain_password(string="avi123")

    # Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
    # zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

    # Proxy a request to the target so that ZAP has something to deal with
    print('Accessing target {}'.format(target))
    zap.urlopen(target)
    # Give the sites tree a chance to get updated
    time.sleep(2)

    for loop in range(int(loop)):
        print('Spidering target {}'.format(target))
        scanid = zap.spider.scan(target)
        # Give the Spider a chance to start
        time.sleep(2)
        while (int(zap.spider.status(scanid)) < 100):
            # Loop until the spider has finished
            print('Spider progress %: {}'.format(zap.spider.status(scanid)), end='\r')
            time.sleep(2)
        print("")
        print('Spider completed')
    print('All Spider runs completed')


def run_zap_attack(target, proxy, loop, apikey="avi123"):

    # By default ZAP API client will connect to port 8080
    zap = ZAPv2(apikey=apikey, proxies={'http': proxy})
    #zap.core.set_option_use_proxy_chain(boolean=True)
    #zap.core.set_option_proxy_chain_name(string="10.79.111.22")
    #zap.core.set_option_proxy_chain_skip_name(string='127.0.0.1;')
    #zap.core.set_option_proxy_chain_port(integer=6666)
    #zap.core.set_option_use_proxy_chain_auth(boolean=True)
    #zap.core.set_option_proxy_chain_user_name(string="aviuser")
    #zap.core.set_option_proxy_chain_password(string="avi123")

    # Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
    # zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

    # Proxy a request to the target so that ZAP has something to deal with
    print('Accessing target {}'.format(target))
    zap.urlopen(target)
    # Give the sites tree a chance to get updated
    time.sleep(2)

    for loop in range(int(loop)):
        name = "XSSonly"
        zap.ascan.add_scan_policy(name)
        zap.ascan.disable_all_scanners(name)
        zap.ascan.enable_scanners("40012", name)
        zap.ascan.set_scanner_alert_threshold("40012", "MEDIUM", name)
        zap.ascan.set_scanner_attack_strength("40012", "HIGH", name)

        print('\nSpidering target %s' % target)
        scanid = zap.spider.scan(target)
        # Give the Spider a chance to start
        time.sleep(2)
        while (int(zap.spider.status(scanid)) < 100):
            print('Spider progress %: {}'.format(zap.spider.status(scanid)), end='\r')
            time.sleep(2)

        print('Spider completed\n')
        # Give the passive scanner a chance to finish
        time.sleep(5)

        print('Scanning target %s' % target)
        scanid = zap.ascan.scan(target, scanpolicyname=name)
        #scanid = zap.ascan.scan(target)
        while (int(zap.ascan.status(scanid)) < 100):
            print('Attack progress %: {}'.format(zap.ascan.status(scanid)), end='\r')
            time.sleep(2)

        print('Scan completed\n')

    print('All Attack runs completed')
    