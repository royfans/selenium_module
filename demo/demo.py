# coding=utf-8
import requests

# f=open(r'test.txt','r')#打开所保存的cookies内容文件
# cookies={}#初始化cookies字典变量
# for line in f.read().split(';'):
#     #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     # print(line)
#     # print(line.strip())
#     name,value=line.strip().split('=',1)
#     cookies[name]=value  #为字典cookies添加内容
# print(cookies)
#
# res = requests.get('http://10.2.46.93:6080/index.html', cookies= cookies)
# print(res.text)
s = requests.session()


headers = {
    'Referer':'http://10.2.46.93:6080/login.jsp',
    'Origin':'http://10.2.46.93:6080',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    "cache-control": "no-cache",
    # 'Cookie':'name=admin; 4aLogin=true; RANGERADMINSESSIONID=16C901E83392B7706AB4F5330E084B9E'
}

res = s.get('http://10.2.46.93:6080/login.jsp',headers=headers)
s.cookies.update({
    'name':'admin',
    '4aLogin':'false',
})
res2 = s.post('http://10.2.46.93:6080/j_spring_security_chec',headers=headers, data={'j_username':'admin','j_password':'admin'})
with open('index.html','wb') as f:
    f.write(res.content)
print(res.status_code)