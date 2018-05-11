#!/usr/bin/env python
# coding=utf-8

import requests

url = 'https://a1.go2yd.com/gslb/bucket/get?app=yidian-ios&ver=4.6.2.1&pver=1&d=a1.go2yd.com'

url2 = 'https://a1.go2yd.com/Website/channel/recommend-channel?appid=pro&channel_id=101356040203&cv=4.6.2.1&distribution=com.apple.appstore&group_fromid=g181&group_id=101356040203&net=wifi&platform=0&position=feed_head&reqid=b1uq3vaf_1523938824581_19&version=020600'

jar = requests.cookies.RequestsCookieJar()
jar.set("JSESSIONID", 'YUGGTkH9qKMXH7ZEArPQhg')
# >>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# >>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# >>> url = 'http://httpbin.org/cookies'
# >>> r = requests.get(url, cookies=jar)
# >>> r.t

res = requests.get(url2, cookies=jar)

print(res.status_code)
print res.text

print res.cookies