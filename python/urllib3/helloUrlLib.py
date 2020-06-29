#!/usr/bin/env python
import urllib3

# This is first program using urllib3




if __name__ == "__main__":
    # Create urllib connection
    http = urllib3.PoolManager(num_pools=2)
    # Get some data from google
    # replace google.com with google.hwk what you get
    r = http.request('GET', 'http://www.google.co.in', preload_content=True)
    # What we get response, data, headers
    print("============= Data =====================")
    print(r.data)
    print("============= Headers =====================")
    print(r.headers)
    print("============= Status =====================")
    print(r.status)
    r.release_conn() 
