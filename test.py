# Тест на пидора v0.2
import time

print('ТЕСТ НА ПИДОРА v0.3 (делал ziver)')
print('ВАЖНО ПИСАТЬ ВСЁ (КРОМЕ ИМЕНИ) С МАЛЕНЬКОЙ БУКВЫ')

lg = 0
sh = 0

time.sleep(1)
name = input('Как тебя зовут?: ')

print('Привет, ' + name + ' это тест на пидора, здесь ты узнаешь, ебешься ли ты в очко или нет')

sex = input('Ты М или Ж?(Напиши либо man либо woman): ')

if sex == 'man':
    print('Окей ты пацан, поэтому ты можешь быть геем, бисексуалом или натуралом')

    onem = input('И так, первый вопрос, ты когда нибудь дрочил на пацанов?(выбери yes или no): ')
    if onem == 'yes':
        lg = lg + 25


    twom = input('Второй вопрос, целовался ли ты когда нибудь с пацаном?(выбери yes или no): ')
    if twom == 'yes':
        lg = lg + 50

    threem = float(input('Третий вопрос, сколько тебе лет?: '))
    if threem >= float(15):
        sh = sh + 7
    elif threem <= float(15):
        sh = sh + 3

    fourm = input('Четвертый вопрос, у тебя вставал на пацана?(выбери yes или no): ')
    if fourm == 'yes':
        lg = lg + 25

elif sex == 'woman':
    print('О нихуя, ты баба')

    onew = input('И так, первый вопрос, ты когда нибудь дрочила на других девок?(выбери yes или no): ')
    if onew == 'yes':
        lg = lg + 25

    twow = input('Второй вопрос, целовалась ли ты когда нибудь с другой бабой?(выбери yes или no): ')
    if twow == 'yes':
        lg = lg + 25

    threew = float(input('Третий вопрос, сколько тебе лет?: '))
    if threew >= float(15):
        sh = sh + 7
    elif threew <= float(15):
        sh = sh + 3

    fourw = input('Четвертый вопрос, как ты отношися к лгбт?(выбери good или bad): ')
    if fourw == 'good':
        lg = lg + 15
else:
    print('Я не понимаю, пройди тест еще раз')

if sex == 'man':
    print('Процент твоего пидорства равен: ' + str(lg) + '%')
    print('А шанс того что ты станешь пидором равен:' + str(sh) + '%')

elif sex == 'woman':
    print('Процент того что ты лесби равен: ' + str(lg) + '%')
    print('А шанс того что ты станешь лесби: ' + str(sh) + '%')
