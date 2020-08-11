import urllib3
import requests
from colorama import init, Fore

init()

print('ProxyChecker')
print('Введите тип прокси (http, https)')
q = str(input('> '))

print('Введите тайм-аут в секундах')
out = float(input('> '))

if q == 'http':
    print('Введите прокси лист')
    a = str(input('> '))
    w = open(a, 'r')
    e = w.read()
    url = "http://med.claw.ru/"
    for d in e.split('\n'):
        try:
            proxy = {'http': d}
            sess = requests.session()
            f = sess.get(url, timeout = out, proxies = proxy)
            print(Fore.GREEN + d + ' Прокси работает')
            u = open('http.txt', 'a')
            u.write('\n' + d)
            u.close()
        except:
            print(Fore.RED + d + ' Прокси не работает')
                    
if q == 'https':
    print('Введите прокси лист')
    a = str(input('> '))
    w = open(a, 'r')
    e = w.read()
    url = "https://vk.com"
    for d in e.split('\n'):
        try:
            proxy = {'https': d}
            sess = requests.session()
            f = sess.get(url, timeout = out, proxies = proxy)
            print(Fore.GREEN + d + ' Прокси работает')
            u = open('https.txt', 'a')
            u.write('\n' + d)
            u.close()
        except:
           print(Fore.RED + d + ' Прокси не работает')
print('\nПроверка закончена')
input()
