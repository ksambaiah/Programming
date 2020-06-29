#!/usr/bin/env python
import urllib3

# This is first program using urllib3




if __name__ == "__main__":
    # Create urllib connection
    http = urllib3.PoolManager(num_pools=1)
    # Get some post httpbin.org
    r = http.request('POST', 'http://httpbin.org', fields={'hello': 'world'})
    # What we get response, data, headers
    print("============= Data =====================")
    print(r.data)
    print("============= Headers =====================")
    print(r.headers)
    print("============= Status =====================")
    print(r.status)
    r.release_conn() 
