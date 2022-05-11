from itertools import tee
from time import sleep
import requests
import re
import datetime


court_lookup = {
    "Rossi Park Court #3": "c408y841"
}


url = "https://www.spotery.com/f/tf-faci-detail/faciDetail?Adf-Window-Id=w1c9ykzjxf2&Adf-Page-Id=0"

headers = {
  'adf-rich-message': 'true',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'JSESSIONID=P3CxLsXZ8lAe8HaLrUWZrHckdpuU-PGBthCDtxbAL6LYR6ZFN-2i!-1771886654; __zjc6185=5190665278; __ZEHIC6201=1652240074',
}

def generate_payload(date):
    return f"pt1:idDate={generate_date(date)}&pt1:pt_soc1=&org.apache.myfaces.trinidad.faces.FORM=f1&Adf-Window-Id=w1c9ykzjxf2&Adf-Page-Id=0&javax.faces.ViewState=!-cw31yef50&event=pt1%3AidDate&event.pt1:idDate=%3Cm+xmlns%3D%22http%3A%2F%2Foracle.com%2FrichClient%2Fcomm%22%3E%3Ck+v%3D%22autoSubmit%22%3E%3Cb%3E1%3C%2Fb%3E%3C%2Fk%3E%3Ck+v%3D%22suppressMessageShow%22%3E%3Cs%3Etrue%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22type%22%3E%3Cs%3EvalueChange%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E&oracle.adf.view.rich.PROCESS=pt1%3AidDate"

def fetch_court_availability(date):
    available_courts = []
    data = requests.request("POST", url, headers=headers, data=generate_payload(date))
    filtered_data = re.findall(r'<update id="pt1:pgl21">(.+?)<\/update>', data.text)
    if len(filtered_data) > 0:
        time_slots = re.findall(r'<span class="xfx">(.+?)<\/span><\/div>', str(filtered_data))
        for time_slot in time_slots:
            if time_slot[-6:] == "&nbsp;":
                available_courts.append(f"{time_slot[:8]} {generate_date(date)}")
    return available_courts
    

def generate_date(date):
    return date.strftime("%-m/%-d/%Y").replace(" ", "%2F")


first_iteration = True
while True:
    open_times = {}
    available_courts = []
    for i in range(9):
        current_date = datetime.datetime.now() + datetime.timedelta(days=i)
        available_courts += fetch_court_availability(current_date)
        
    print(available_courts)

    court_messages = []
    for court in available_courts:
        open_times[court] = True
        
        if not first_iteration:
            court_messages.append(court)
            
    sleep(60)
        