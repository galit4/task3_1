from fastapi import APIRouter
import json
from datetime import datetime, timedelta


#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["getting all cves from last 5 in records"])

@router.get("/get/allv2")
def getting():
    output = []
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
    #визаначаємо межу по часу
    endtime = (datetime.now() - timedelta(days=5))
    for cve in content["vulnerabilities"]:
        cve_time = datetime.strptime(cve["dateAdded"], f'%Y-%m-%d')
        #зберігаємо цве що лежить у часовому проміжку
        if cve_time >= endtime:
            output.append(cve)
        #обмеження по кількості
        if len(output) == 40:
            return output
    return output
