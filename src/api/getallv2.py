from fastapi import APIRouter
import json
from datetime import datetime, timedelta


#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["getting all cves from last 5 days in real time"])
flag = 0
last_output = []#пустий словник для подальшого ретурну
@router.get("/get/allv2")
def getting():
     #відкриваєм файл та зберігаємо вміст
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []

  
        for cve in content["vulnerabilities"]:     
            #форматуємо вивід datetime, аби вигляд був приблизно як "2024-11-25":
            for j in range(0, len(content["vulnerabilities"])):
                startdate = str(datetime.now()-timedelta(days=j))
                startdate = startdate.split(" ")
                startdate = startdate[0]
                
            
                if (cve["dateAdded"] == str(startdate)):
                
                    output.append(cve)
                    if len(output) == 40:
                        #присвоєння date значення "dateAdded" для першої cve
                        date = output[0]
                        date = date["dateAdded"]
                        date = datetime.strptime(date, f'%Y-%m-%d')
                        enddate = date - timedelta(days=6)
                        #ітерація по списку з cve, якщо дата входить в задані рамки, то cve додається в новий список
                        print(enddate)
                        for k in output:
                            if not(k["dateAdded"] < str(enddate)):
                                last_output.append(k)
                        return last_output

            
            
            

    return content
                    

        
    
