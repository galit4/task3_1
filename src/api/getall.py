from fastapi import APIRouter
import json
from datetime import datetime, timedelta


#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["getting all cves from last 5 in records"])

@router.get("/get/allv2")
def getting():
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        
        startdate = datetime.now()-timedelta(days=5)
        output = []#пустий словник для подальшого ретурну
        for cve in content["vulnerabilities"]:
            #якщо cve новіша за datetime.now()-timedelta(days=5), то список апендиться
            if (cve["dateAdded"] >= str(startdate)):
                output.append(cve)
                if len(output) == 40:
                    break
        return output
    
