from flask import Flask
# import jsonify
import json
import requests
#import pandas as pd
app = Flask(__name__)

url = "https://apis.bbvabancomer.com/locations_sbx/v1/branches"

headers = {
    'Content-Type': "application/json",
    'Authorization': "jwt eyJ6aXAiOiJERUYiLCJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ARGX3TQUcHgi539y1fjNaCWJWI17ChyMFwI7PClJucs0jh08M_FsXPTksWCoW7KEns-2P9qtYVveChVXBnsdW5FOyuBiT1qYhTkJLrPAw4fOOlWdEjHmJBYGfr0wyWp-DVsfS_lloj2WZa724D8dhAeR2PbQYyo5wAfNM-8_ZcVVCpXbFGiMuEQb2VLSf6DOsxqI_0w0y-ZC_5V_9FufMyFusar3Yt_ooDPjFNWj4EKO_tGl3RWFsbLO99wY3VtyPLfiD-HHDFUcaPO9vG6vCOqwj1YOG72WRv4NvjBzjh5z8EoXlVaxNlc4jfgGScwB4D4eFM9wwhuq4WzcDgBFlA.e_tKwVU5Wsjd8h0i.yHcwlS0WvPD_ZaNR0dn0aVdwDfwDdumLxi0HUaDGMIydaPbiOq2yawdHDZ4GMMDqjZetUI_P13cuWGT6p7CqE81cxGiSldCOkwS1Hr_qDAGFkSq6Ip5c-WSHpigB_DQlcnI6wyHZStOpMvR5K0WTetMw1-RgzQYXl-UGOxZQUSbnndJC8J1uqvQKaNR6h2GzoXC00N-OjaSe_6NPlFpblwKPXQm8a8ge3QMS2NeVpa8zyajKXpokCo4lDBuzZy9VucnL1HzXdeETOxOFZ_fenS0lmUlMO-F-Mug.zDQ1pTt_YsEWKLpRLoinRw",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "47b99965-5ce7-4af1-ae3f-e37149de9e10,6c737291-7346-4bdd-8d2c-8325f4d4a2cd",
    'Host': "apis.bbvabancomer.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "ak_bmsc=4CF931AB15FDDF4A89036BCA0681B141B81C764DB5560000E1EBC85DC01EFE34~plH/9C2wScSxfCokJHKgbFDGw3E0UtbnzhNQBOQJJe60hRcCgwMgkPoo5XpeR9/OoOQhvJLZX8bQT5pcoSTrNk/+FYhY00vt3aJZ5pbGumATsizIwkHMe/tIEM1XrtbNlAETtc4wN+I3C863D5a9JWp6r/z8+QQuP/n+6WL1+x2GBp1oApdMAohgzjZFkn6EKo6g+i6qHW0n+x78MoWViQnIZwPNOcyupmnzyoaCAxgQRe8/8/OKqK6jktAMI5mcfk; bm_sv=494F50B9ED3CD95420D3FD2849ECCE62~rt93QYpEu9VWR+dOVqkcguH3bUi1Ycr8SGUQjhZi2Zq1jvroFez0XV+z1BAB0gMXfU+Ss8GEJyp5TuozMbsAp++P7F/IRK1gZGaQgeV2MdB0hr2yC/0mna7FI+lMOe73c//87g9Qi42enL5Z7gZfi87S4Zx65JAjdWVX7/TL6LQ=",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
data=response.json()

# print(respose.txt)
# @app.route('/hello/<name>')
# def hello(name):
#     info = requests.get('http://localhost:5000/hello/'+name)
#     return info

# @app.route('/api')
# def api():
#     return data

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=80)