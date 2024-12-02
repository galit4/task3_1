from fastapi import APIRouter
import json
from datetime import datetime, timedelta

#функція для визначення дати найновішого цве - 5 днів
def get_date(file):
    #берем тисячу днів як максимум віку цве
    for i in range(0, 1000):
        #форматуєм час
        endtime = str((datetime.now() - timedelta(days=i)))
        endtime = endtime.split(" ")
        endtime = endtime[0]
        
        for cve in file["vulnerabilities"]:
            #форматуєм
            cve_time = str(datetime.strptime(cve["dateAdded"], f'%Y-%m-%d'))
            cve_time = cve_time.split(" ")
            cve_time = cve_time[0]
            #знаходим найновіше цве
            if cve_time == endtime:
                cve = datetime.strptime(cve["dateAdded"], f'%Y-%m-%d')
                endtime = (cve - timedelta(days=5))
                return endtime
            
#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["getting all cves from last 5 days in real time"])
last_output = []#пустий словник для подальшого ретурну
@router.get("/get/all")
def getting():
    output = []
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        endtime = get_date(content) 
    #якщо цве входить в проміжок останніх п'яти днів, додаєм його у список
    for cve in content["vulnerabilities"]:
        cve_time = datetime.strptime(cve["dateAdded"], f'%Y-%m-%d')
        if cve_time >= endtime:
            output.append(cve)
        if len(output) >= 40:
            return output
    return output


