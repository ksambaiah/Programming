#!/usr/bin/env python
import urllib3
import json


if __name__ == "__main__":
    # Create urllib connection
    http = urllib3.PoolManager(num_pools=1)
    # Get origin IP
    r = http.request('GET', 'http://httpbin.org/ip')
    print(json.loads(r.data.decode('utf-8')))
    r.release_conn()
   
