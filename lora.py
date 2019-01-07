import json
import requests
import urllib3

from GUI import GUI
"""Teeest"""

str = ""
strinfo = ""

def loraAPIconnection():
    """Hej"""
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


def getsensorAPI():
    url = "http://webplant.azurewebsites.net/api/soilsensordatas"
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers).json()

    return response

#Post to Sensor
def postToSensorAPI():
    url = "http://webplant.azurewebsites.net/api/soilsensordatas"
    dir = {'MoistInt': 1, 'timestamp': 1337}
    headers = {'content-type': 'application/json'}
    post = requests.post(url, data=json.dumps(dir), headers=headers).json()

    return post


#print(getsensorAPI())
GUI(str, strinfo)
