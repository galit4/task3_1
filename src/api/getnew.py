from fastapi import APIRouter
import json
from datetime import datetime, timedelta

router = APIRouter(tags=["Get new cve"])

@router.get("/get/new")
def getting():
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []

  
        for cve in content["vulnerabilities"]:         
            for j in range(0, len(content["vulnerabilities"])):
                startdate = str(datetime.now()-timedelta(days=j))
                startdate = startdate.split(" ")
                startdate = startdate[0]
                
            
                if (cve["dateAdded"] == str(startdate)):
                
                    output.append(cve)
                    if len(output) == 10:
                        return output