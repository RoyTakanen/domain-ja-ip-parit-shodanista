import imp
import json
import os

from shodan_search import connect_host_to_ip

if not "API_KEY" in os.environ:
    exit("Please specify API key")

SHODAN_API_KEY = os.environ['API_KEY']

print(json.dumps(connect_host_to_ip(api_key=SHODAN_API_KEY, query='org:"Valtti Kumppanit Oy" wilma')))
