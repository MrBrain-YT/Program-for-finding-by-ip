import requests
import folium
import pyfiglet


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[ip]': response.get('query'),
            '[side]': response.get('country'),
            '[Region]': response.get('region'),
            '[City]': response.get('city'),
            '[Full name of the region]': response.get('regionName'),
            '[Postcode]': response.get('zip'),
            '[Latitude]': response.get('lat'),
            '[Length]': response.get('lon'),
            '[Time zone]': response.get('timezone'),
            '[Internet provider]': response.get('isp'),
            '[internet provider company]': response.get('as'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except :
        print('[!] Пожалуйста проверьте интернет соединение!')



prewiew_text = pyfiglet.Figlet(font='slant')
print(prewiew_text.renderText('IpHack'))

ip = input('Enter the IP address : ')
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
