# -*- coding: utf-8 -*-
#!/usr/bin/python3

# AHT10とBMP180を連続して読み取り
# 温度T、湿度H、気圧PのCSVファィルを読み取り
# そのデータを
# ambientに投げます。

"""
Ambientライブラリのインストール
$ pip3 install git+https://github.com/AmbientDataInc/ambient-python-lib.git

2023/12/9  sensorBox対応のTHP_ambient.pyを改造します。

"""
import os
import time
import datetime
import time
import configparser

path = '/home/pi/sensorHAT/'

# config,iniから値取得
# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read(path + 'config.ini', encoding='utf-8')
# --------------------------------------------------
ch        =  int(config_ini.get('AMBIENT', 'ch'))
write_key =      config_ini.get('AMBIENT', 'write_key')
# --------------------------------------------------

# =================================================
#           ライブラリインポート
import ambient
import requests

# Ambient対応 
"""                チャネルID       ライトキー        """
# am = ambient.Ambient(68358, "3a0553e59b39b1ef")
am = ambient.Ambient(ch, write_key)
""""""""""""""""""""""""""""""""""""""""""""""""""""""


def data_read():
    with open(path + 'temp_data_last.txt', 'r') as file:
        # ファイル全体を読み込む
        temp = file.read()
        temp = int(temp)/10
    with open(path + 'humdy_data_last.txt', 'r') as file:
        # ファイル全体を読み込む
        humdy = file.read()
        humdy = int(humdy)
    with open(path + 'press_data_last.txt', 'r') as file:
        # ファイル全体を読み込む
        press = file.read()
        press = int(press)

    return temp,humdy,press

def ambient(csv_data):
    #print('ambient')
    try:
        res = am.send({"d1": csv_data[1],"d2": csv_data[2],"d3": csv_data[3]})
    except requests.exceptions.RequestException as e:
        print('request failed: ', e)



def main():
    print('start')

    header = ['time_stamp','temp','humdy','press']

    while True:

        if datetime.datetime.now().second > 10: # 10秒を超えたら計測

            try:
                temp,humdy,press = data_read()
            except:
                time.sleep(3)
                try:
                    temp,humdy,press = data_read()
                except:
                    pass

            time_stamp = datetime.datetime.now().strftime('%Y/%m/%dT%H:%M')
            print(time_stamp,' temp:',temp,' humdy:',humdy ,' press:',press)

            csv_data = ['time_stamp','temp','humdy','press']
            csv_data[0] = time_stamp
            csv_data[1] = temp
            csv_data[2] = humdy
            csv_data[3] = press

            ambient(csv_data)

            while datetime.datetime.now().second > 10: # 毎分1回の計測に制限
                time.sleep(1)

        time.sleep(1)

if __name__ == '__main__':
    # try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    # except KeyboardInterrupt:
    #     print('キーボード押されました。')
    # except ValueError as e:
    #     print('err')
