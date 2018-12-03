import json
import requests
import urllib3
import tkinter

from GUI import GUI
"""Teeest"""
file_object = open("loraurl.txt", "r")
plane = '3'
sensor = '3'
url = file_object.read()
stringen = '%s' %url
headers = {'content-type': 'application/json'}
response = requests.get(url, headers)
data = response.json()
print(data[0]['dd'])
str = 'Våning %s sensor %s:' % (plane, sensor)
strinfo = 'Tid: %s\n timestamp: %s\n Temperature: %s\nHumidity: %s\nLight: %s\n' % (data[0]['time'], data[0]['ts'], data[0]['dd']['temperature'], data[0]['dd']['humidity'], data[0]['dd']['light'])
strinfo = strinfo+'Movement: %s\n Battery: %s\n' %( data[0]['dd']['pir'],  data[0]['dd']['vdd'])

GUI(str, strinfo)