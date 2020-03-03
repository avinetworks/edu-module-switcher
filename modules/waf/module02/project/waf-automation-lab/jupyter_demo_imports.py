from avi.sdk.avi_api import ApiSession
import datetime, time
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from pprint import pprint
from jupyter_demo_setup import testbed_setup
from jupyter_setup_learning import setup_learning, setup_positive_security_group
from jupyter_spider import run_zap_spider, run_zap_attack
from jupyter_whitelist_examples import add_whitelist_examples
from jupyter_demo_cleanup import testbed_cleanup
from jupyter_demo_helpers import print_loglines, print_learned_data, create_exclusions, print_application_map, print_auto_promoted_rules, send_get, send_post, change_policy_mode, print_log_entry, enable_learning_group, check_setup
