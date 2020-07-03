#!/usr/bin/env python

import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

r = http.request('GET', 'https://google.com')
print("========= Status ========")
print(r.status)
print("========= Data ========")
print(r.data)
print("========= Headers ========")
print(r.headers)

r = http.request('GET', 'https://expired.badssl.com')
print("========= Status ========")
print(r.status)
print("========= Data ========")
print(r.data)
print("========= Headers ========")
print(r.headers)


r.release_conn()

