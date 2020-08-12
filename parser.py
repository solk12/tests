import requests
from bs4 import BeautifulSoup

print('Выберите тип прокси')
print('0. HTTPS')
print('1. SOCKS4')
print('2. SOCKS5')
ax = str(input('> '))

print('Как сохранять прокси?')
print('0. IP:Port Time Anonym Country')
print('1. IP:Port Time Anonym')
print('2. IP:Port Time')
print('3. IP:Port')
az = str(input('> '))

headers = {
	'Host':'hidemy.name',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',            
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'identity',
	'Connection':'keep-alive',
	'DNT':'1',
	'CF-Request-ID':'0475e3fb8e00007b237da5e200000001',
	'requests':'',
	'Cookie':'__cfduid=d0d82d405484de16bb5fe86734350143f1596994469; PAPVisitorId=5ea5983fe073f68bf63b2V1wvjHBdxXu; PAPVisitorId=5ea5983fe073f68bf63b2V1wvjHBdxXu; _ym_uid=1596994490223547838; _ym_d=1596994490; _ga=GA1.2.314812144.1596994494; _gid=GA1.2.2105563116.1596994494; _ym_wasSynced=%7B%22time%22%3A1596994494908%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _fbp=fb.1.1596994495158.1272816123; _ym_visorc_42065329=w; _ym_isad=2'
}

url = 'https://hidemy.name/en/proxy-list/?type=s#list'

def get_html(site):
	headers = {
	'Host':'hidemy.name',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',            
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'identity',
	'Connection':'keep-alive',
	'DNT':'1',
	'CF-Request-ID':'0475e3fb8e00007b237da5e200000001',
	'requests':'',
	'Cookie':'__cfduid=d0d82d405484de16bb5fe86734350143f1596994469; PAPVisitorId=5ea5983fe073f68bf63b2V1wvjHBdxXu; PAPVisitorId=5ea5983fe073f68bf63b2V1wvjHBdxXu; _ym_uid=1596994490223547838; _ym_d=1596994490; _ga=GA1.2.314812144.1596994494; _gid=GA1.2.2105563116.1596994494; _ym_wasSynced=%7B%22time%22%3A1596994494908%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _fbp=fb.1.1596994495158.1272816123; _ym_visorc_42065329=w; _ym_isad=2'
}
	r = requests.get(site, headers = headers)
	return r.text



def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	line = soup.find('table').find('tbody').find_all('tr')
	for tr in line:
		td = tr.find_all('td')
		ip = td[0].text
		port = td[1].text
		country = td[2].text.replace('\xa0', '')
		anonym = td[3].text.replace('\r\n        ', '')
		types = td[4].text.replace('\r\n\t\t\t\t\t', '').replace('\r\n        ', '')
		time = td[5].text
		if az == '0':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym + ' \nAnonym: ' + time + ' \nCountry:' + country + ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '1':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym + ' \nAnonym: ' + time + ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '2':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym+ ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '3':
			data = ip + ':' + port
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		else:
			print('Неверная цифра')

	if ax == '0':
		sait = 'https://hidemy.name/en/proxy-list/?type=s&start=64#list'
	elif ax == '1':
		sait = 'https://hidemy.name/en/proxy-list/?type=4&start=64#list'
	elif ax == '2':
		sait = 'https://hidemy.name/en/proxy-list/?type=5&start=64#list'

	r = requests.get(sait, headers = headers)
	soup = BeautifulSoup(r.text, 'lxml')
	line = soup.find('table').find('tbody').find_all('tr')
	for tr in line:
		td = tr.find_all('td')
		ip = td[0].text
		port = td[1].text
		country = td[2].text.replace('\xa0', '')
		anonym = td[3].text.replace('\r\n        ', '')
		types = td[4].text.replace('\r\n\t\t\t\t\t', '').replace('\r\n        ', '')
		time = td[5].text
		if az == '0':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym + ' \nAnonym: ' + time + ' \nCountry:' + country + ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '1':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym + ' \nAnonym: ' + time + ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '2':
			data = ' \n--------------------------------------------------\n' + ip + ':' + port + ' \nTime: ' + anonym+ ' \n--------------------------------------------------'
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		elif az == '3':
			data = ip + ':' + port
			n = open('proxy.txt', 'a', encoding='utf-8')
			n.write(data + '\n')
			n.close()
		else:
			print('Неверная цифра')

def main():
	if ax == '0':
		url = 'https://hidemy.name/en/proxy-list/?type=s#list'
	elif ax == '1':
		url = 'https://hidemy.name/en/proxy-list/?type=4#list'
	elif ax == '2':
		url = 'https://hidemy.name/en/proxy-list/?type=5#list'
	else:
		print('Неверная цифра')
	get_page_data(get_html(url))

if __name__ == '__main__':
	main()

print('Прокси сохранены в proxy.txt')
input('Нажмите Enter чтобы выйти')
