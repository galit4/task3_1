from fastapi import APIRouter
import json
from datetime import datetime, timedelta

#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Get new cve"])

@router.get("/get/")
def getting(key: str):
    #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []#пустий словник для подальшого ретурну
        value = content.get("vulnerabilities")
        #перетворюєм cve в текст і додаєм його у список якщо у ньому є key
        for cve in value:
            if key in str(cve):
                output.append(cve)
        return output
