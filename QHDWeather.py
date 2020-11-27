import json
import os
import requests

postdata = {'location': '秦皇岛', 'key': '39efe9417c00495097f3c118317725c6'}
stra = requests.post('https://free-api.heweather.net/s6/weather/forecast', data=postdata)
json_obj = json.loads(stra.text)
w0 = json_obj['HeWeather6'][0]
city = w0['basic']['location']
weather_0 = w0['daily_forecast'][0]
weather_1 = w0['daily_forecast'][1]
weather_2 = w0['daily_forecast'][2]

outstr = '您好！现在是{0}日，很高兴为您播放天气预报.'.format(weather_0['date'])

outstr_0 = '今天天气{0}转{1},温度{2}到{3}摄氏度,{4},{5}级.'.format( weather_0['cond_txt_d'],
        weather_0['cond_txt_n'], weather_0['tmp_min'], weather_0['tmp_max'],
        weather_0['wind_dir'], weather_0['wind_sc'])

outstr_1 = '明天天气{0}转{1},温度{2}到{3}摄氏度,{4},{5}级.'.format( weather_1['cond_txt_d'],
        weather_1['cond_txt_n'], weather_1['tmp_min'], weather_1['tmp_max'],
        weather_1['wind_dir'], weather_1['wind_sc'])

outstr_2 = '后天天气{0}转{1},温度{2}到{3}摄氏度,{4},{5}级'.format( weather_2['cond_txt_d'],
        weather_2['cond_txt_n'], weather_2['tmp_min'], weather_2['tmp_max'],
        weather_2['wind_dir'], weather_2['wind_sc'])

print(outstr + city + outstr_0 +outstr_1 +outstr_2)
#os.system('/bin/echo "hello,world!" >> /home/pi/xt.txt')


