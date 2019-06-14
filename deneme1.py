import requests
def gonderici():
    url="http://192.168.3.142/GeoSOS/Main.asmx"
    headers ={'content-type': 'application/soap+xml'}
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
     <soap12:Body>
      <SendAlert xmlns="http://tempuri.org/">
       <deviceUID>1081CB58-010D-406B-8B68-D582340C02B7</deviceUID>
      </SendAlert>
     </soap12:Body>
    </soap12:Envelope>"""
    response = requests.post(url,data=body,headers=headers)
    print (response.content)
if __name__ == "__main__" :
    gonderici()

    