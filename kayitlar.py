import time
import datetime
from urllib.request import urlopen
import requests

t=bool
def kayitlar():
    while True:
        print("Başladı")
        time.sleep(1800)
        print("30 Dakika Geçti")
        url='http://www.google.com/'
        timeout=5
        try:
            
            _=requests.get(url,timeout=timeout)
            print("Bağlantı Başarılı")
            print(datetime.datetime.now())
            url="http://192.168.3.142/GeoSOS/Main.asmx"
            headers ={'content-type': 'application/soap+xml'}
            body = """<?xml version="1.0" encoding="utf-8"?>
            <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
             <soap12:Body>
              <HeartBeat xmlns="http://tempuri.org/">
               <deviceUID>1081CB58-010D-406B-8B68-D582340C02B7</deviceUID>
               <appVersion>1.0</appVersion>
              </HeartBeat>
             </soap12:Body>
            </soap12:Envelope>"""
            response = requests.post(url,data=body,headers=headers)
            print (response.content)
            t=True
        except requests.ConnectionError:
            print("İnternet Bağlantısı Yok")
            print(datetime.datetime.now())
            t=False

    
if __name__ == "__main__" :
     kayitlar()    

    

        
    