# coding=utf-8

import urllib.parse
from urllib import request
import pprint
import xml
def login():
    login_index = 'http://10.2.46.93:6080/index'
    login_url = 'http://10.2.46.93:6080/j_spring_security_check'
    user_mail = 'admin'
    user_pwd = 'admin'
    # 构造cookie
    cj = cookiejar.CookieJar()
    # 由cookie构造opener
    handler = request.HTTPCookieProcessor(cj)
    opener = request.build_opener(handler)
    # 把 oppner 加载到 request
    request.install_opener(opener)
    # 获取登录结界面的 HTML
    html = request.urlopen(login_url).read()
    # 获取登录界面 input， 添加到 DATA
    data = parse_form(html)
    data['email'] = user_mail
    data['password'] = user_pwd
    encoded_data = parse.urlencode(data).encode('utf-8')
    # 构造请求
    req = request.Request(login_url, encoded_data)
    response = request.urlopen(req)
    # response = request.urlopen(login_url, encoded_data)
    current_url = response.geturl()
    print(current_url)
    return request

'''
def parse_form(html):

    # tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data
'''
if __name__ == "__main__":
    html = urllib.request.urlopen('http://10.2.46.93:6080/index').read()
    form = parse_form(html)
    pprint.pprint(form)
