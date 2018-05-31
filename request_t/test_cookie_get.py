#!/usr/bin/env python
# coding=utf-8

import requests

# url_source_get = "https://a1.go2yd.com/Website/user/login-as-guest?appid=pro&cv=4.6.2.1&distribution=com.apple.appstore&idfa=5ef9a039be1b5ae299140646e83ce2f5&net=wifi&password=223def41868f65bce07f17cf4415f7729f7749ca&platform=0&reqid=1523942301029_16&secret=e3e00911abb9ad1f4daee4f2c4351b60c5567944&username=HG_37154CD18566&version=020600"
url_simple_get = "https://a1.go2yd.com/Website/user/login-as-guest?appid=pro&password=223def41868f65bce07f17cf4415f7729f7749ca&secret=e3e00911abb9ad1f4daee4f2c4351b60c5567944&username=HG_37154CD18566&version=020600"
# http works too.

r = requests.get(url_simple_get)

print r.status_code

print r.text

print(r.cookies)

print r.cookies["JSESSIONID"]