from fastapi import APIRouter
import json
from datetime import datetime, timedelta

#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Get new cve"])

@router.get("/get/new")
def getting():
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []#пустий словник для подальшого ретурну

      #ітеруємся по усіх cve, та в  
        for cve in content["vulnerabilities"]:         
            for j in range(0, len(content["vulnerabilities"])):
                startdate = str(datetime.now()-timedelta(days=j))
                 #форматуємо вивід datetime, аби вигляд був приблизно як "2024-11-25":
                startdate = startdate.split(" ")
                startdate = startdate[0]
                
            
                if (cve["dateAdded"] == str(startdate)):
                
                    output.append(cve)
                    if len(output) == 10:
                        return output
