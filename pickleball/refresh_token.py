import requests
import re

url = "https://www.spotery.com/f/adf.task-flow?adf.tfDoc=%2FWEB-INF%2Ftaskflows%2Ffacility%2Ftf-faci-detail.xml&adf.tfId=tf-faci-detail&psOrgaSk=3333200&_afrLoop=740385461313115&_afrWindowMode=0&Adf-Window-Id=w1c9ykzjxf2&_afrPage=0&_afrFS=16&_afrMT=screen&_afrMFW=766&_afrMFH=1335&_afrMFDW=2560&_afrMFDH=1440&_afrMFC=8&_afrMFCI=0&_afrMFM=0&_afrMFR=96&_afrMFG=0&_afrMFS=0&_afrMFO=1"

payload={}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'JSESSIONID=VAyz5eYC8F9vV_k_g_wa5J712f9lv2dK9l3MqsmOfpe4UCUshK06; __zjc6185=5190665278; __ZEHIC6201=1652240074; JSESSIONID=jEOxRoiVX8zfTQwr9zai2IKcStERiSuFKRB9r1tojM05IWzC3ER5!-1771886654',
}

response = requests.request("GET", url, headers=headers, data=payload)

time_slots = re.findall(r'<span class="xfx">(.+?)<\/span><\/div>', response.text)
for time_slot in time_slots:
    print(time_slot)