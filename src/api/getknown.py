from fastapi import APIRouter
import json
from datetime import datetime, timedelta

#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Get new cve"])

@router.get("/get/known")
def getting():
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []#пустий словник для подальшого ретурну

  
        for cve in content["vulnerabilities"]:         
            for j in range(0, len(content["vulnerabilities"])):
                startdate = str(datetime.now()-timedelta(days=j))
                startdate = startdate.split(" ")
                startdate = startdate[0]
                #порівняння ключа cve
                if cve["knownRansomwareCampaignUse"] == "Known":
                    output.append(cve)
                     #обмеження по довжині
                    if len(output) == 10:
                        return output
            
