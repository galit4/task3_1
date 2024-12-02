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

        #визначаємо 1000 днів як максимум старості цве
        for i in range(0, 1000):
            for cve in content["vulnerabilities"]: 
                #визначаємо поріг часу та форматуємо його для порівняння     
                startdate = str(datetime.now()-timedelta(days=i))
                startdate = startdate.split(" ")
                startdate = startdate[0]
                #зберігаємо найновіші цве
                if cve["dateAdded"] == startdate:
                    output.append(cve)
                #обмежуєм по кількості
                if len(output) == 10:
                    return output
        return output
            
