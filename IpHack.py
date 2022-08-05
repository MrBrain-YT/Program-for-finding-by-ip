import requests
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[ip]': response.get('query'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('region'),
            '[Город]': response.get('city'),
            '[Полное название региона]': response.get('regionName'),
            '[Почтовый индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
            '[Временная зона]': response.get('timezone'),
            '[Интернет поставщик]': response.get('isp'),
            '[Компания интернет поставщика]': response.get('as'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except :
        print('[!] Пожалуйста проверьте интернет соединение!')



# prewiew_text = Figlet(font='slant')
print('    ____      __  __           __  ')
print('   /  _/___  / / / /___ ______/ /__')
print('   / // __ \/ /_/ / __ `/ ___/ //_/')
print(' _/ // /_/ / __  / /_/ / /__/ ,<   ')
print('/___/ .___/_/ /_/\__,_/\___/_/|_|  ')
print('   /_/                             ')
print('')

# print(prewiew_text.renderText('IpHack'))
ip = input('Введите IP адрес жертвы : ')
get_info_by_ip(ip=ip)
print()
print()
print('Если вы ввели правильный Ip адрес то:')
print("В папке где находиться программа появился HTML файл с координатами местонахождения жертвы")
print("Если вы скачали данную рограмму из Py_Programs Launcher")
print("                           ______________________________________________________")
print("То фаил находиться по пути | C:\Program Files (x86)\PyProgramsLauncher\Programs |")
print("                           |____________________________________________________|")
input('Press any key to exit ...')
